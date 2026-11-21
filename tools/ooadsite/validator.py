"""Compile and run every C++ program in the lessons and compare it with the documented output.

Directives (written as ``//@...`` comments inside a ```cpp block, hidden on the rendered page):
  //@input: text         line fed to stdin (repeat for several lines)
  //@expect: compile-error   the program must FAIL to compile
  //@norun               compile only (e.g. intentionally infinite loops)
  //@nocheck             skip the block entirely

A program is any ```cpp block containing ``int main``. If the next fenced block is ```output,
the program's stdout must match it exactly (trailing whitespace ignored).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path

from . import config

# Fallback compiler locations, tried only when g++ is not on PATH (override with OOAD_GXX).
_FALLBACK_COMPILERS = ["C:/msys64/ucrt64/bin/g++.exe", "C:/msys64/mingw64/bin/g++.exe"]


@dataclass
class Program:
    lesson: str
    line: int
    code: str
    expected: str | None
    inputs: list[str]
    expect_compile_error: bool
    compile_only: bool


@dataclass
class Result:
    program: Program
    status: str  # ok | fail | nodoc
    message: str = ""


def find_compiler() -> str:
    for candidate in (os.environ.get("OOAD_GXX"), shutil.which("g++"), *_FALLBACK_COMPILERS):
        if not candidate:
            continue
        if Path(candidate).exists():
            return candidate
        found = shutil.which(candidate)
        if found:
            return found
    raise RuntimeError("g++ not found: install it, or set OOAD_GXX to its full path")


def extract_programs(lesson: str, text: str) -> list[Program]:
    lines = text.splitlines()
    blocks: list[tuple[int, str, list[str]]] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("```"):
            lang, j, buf = s[3:].strip(), i + 1, []
            while j < len(lines) and lines[j].strip() != "```":
                buf.append(lines[j])
                j += 1
            blocks.append((i + 1, lang, buf))
            i = j + 1
        else:
            i += 1

    programs = []
    for k, (line_no, lang, buf) in enumerate(blocks):
        if lang != "cpp":
            continue
        code = "\n".join(buf)
        directives = [l.strip() for l in buf if l.strip().startswith("//@")]
        if "//@nocheck" in directives or not re.search(r"\bint\s+main\s*\(", code):
            continue
        expected = "\n".join(blocks[k + 1][2]) if k + 1 < len(blocks) and blocks[k + 1][1] == "output" else None
        programs.append(Program(
            lesson=lesson, line=line_no, code=code, expected=expected,
            inputs=[d[len("//@input:"):].strip() for d in directives if d.startswith("//@input:")],
            expect_compile_error="//@expect: compile-error" in directives,
            compile_only="//@norun" in directives,
        ))
    return programs


def _normalize(s: str) -> str:
    return "\n".join(l.rstrip() for l in s.replace("\r\n", "\n").split("\n")).rstrip("\n")


def _run_one(program: Program, compiler: str, env: dict[str, str], cache: dict[str, str]) -> tuple[Result, str | None]:
    key = hashlib.sha1(json.dumps([program.code, program.expected, program.inputs,
                                   program.expect_compile_error, program.compile_only]).encode()).hexdigest()
    if cache.get(key) == "ok":
        return Result(program, "ok"), key
    with tempfile.TemporaryDirectory() as tmp:
        source, exe = os.path.join(tmp, "p.cpp"), os.path.join(tmp, "p.exe")
        Path(source).write_text(program.code, encoding="utf-8")
        built = subprocess.run([compiler, "-std=c++17", "-Wall", "-Wextra", "-static", "-o", exe, source],
                               capture_output=True, text=True, env=env)
        if program.expect_compile_error:
            if built.returncode == 0:
                return Result(program, "fail", "expected a compile error but it compiled"), None
            return Result(program, "ok"), key
        if built.returncode != 0:
            return Result(program, "fail", "COMPILE ERROR:\n" + built.stderr[:1500]), None
        if program.compile_only:
            return Result(program, "ok"), key
        try:
            run = subprocess.run([exe], input="\n".join(program.inputs) + "\n", capture_output=True,
                                 text=True, timeout=10, cwd=tmp, env=env)
        except subprocess.TimeoutExpired:
            return Result(program, "fail", "TIMEOUT"), None
        if program.expected is None:
            return Result(program, "nodoc", _normalize(run.stdout)[:300]), key
        if _normalize(run.stdout) != _normalize(program.expected):
            return Result(program, "fail",
                          f"OUTPUT MISMATCH\n--- expected ---\n{_normalize(program.expected)}"
                          f"\n--- actual ---\n{_normalize(run.stdout)}"), None
        return Result(program, "ok"), key


def check(only: str | None = None, workers: int = 8) -> int:
    """Run the validator. Returns the number of failing programs."""
    course = config.load_course()
    programs: list[Program] = []
    for lesson in course.lessons:
        if only and only not in lesson.slug:
            continue
        if lesson.source.exists():
            programs += extract_programs(lesson.slug, lesson.source.read_text(encoding="utf-8"))

    compiler = find_compiler()
    env = dict(os.environ, PATH=str(Path(compiler).parent) + os.pathsep + os.environ.get("PATH", ""))
    config.CACHE_DIR.mkdir(exist_ok=True)
    cache_file = config.CACHE_DIR / "validated.json"
    cache = json.loads(cache_file.read_text()) if cache_file.exists() else {}

    print(f"Checking {len(programs)} programs with {compiler} ...")
    failures = undocumented = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for result, key in pool.map(lambda p: _run_one(p, compiler, env, cache), programs):
            where = f"{result.program.lesson}.md:{result.program.line}"
            if result.status == "fail":
                failures += 1
                print(f"\n[FAIL] {where}\n{result.message}")
            else:
                if key:
                    cache[key] = "ok"
                if result.status == "nodoc":
                    undocumented += 1
                    print(f"[no output block] {where} -> prints: {result.message!r}")
    cache_file.write_text(json.dumps(cache))
    print(f"\nDone: {len(programs)} programs, {failures} failures, {undocumented} without documented output.")
    return failures
