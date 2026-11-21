"""Build the static site: render every lesson to ``dist/`` and copy the static assets."""
from __future__ import annotations

import html
import re
import shutil
from pathlib import Path
from string import Template

from . import config
from .config import Course, Lesson
from .markdown import inline, render_markdown

ROADMAP_PLACEHOLDER = "<p>&lt;&lt;ROADMAP&gt;&gt;</p>"


def reading_minutes(markdown: str) -> int:
    """Rough reading time: ~200 words/min of prose plus 1 min per 40 lines of code."""
    prose = re.sub(r"```.*?```", "", markdown, flags=re.S)
    code_lines = sum(block.count("\n") for block in re.findall(r"```.*?```", markdown, flags=re.S))
    return max(2, round(len(prose.split()) / 200 + code_lines / 40))


def lesson_number(slug: str) -> str:
    """'03_4_encapsulation' -> '3.4'; practice sets and the intro page have no number."""
    m = re.match(r"(\d\d)_(\d)_", slug)
    return f"{int(m.group(1))}.{m.group(2)}" if m else ""


def render_sidebar(course: Course, current_slug: str, toc: list[tuple[int, str, str]]) -> str:
    toc_html = "".join(f'<li class="l{lvl}"><a href="#{hid}">{inline(text)}</a></li>' for lvl, hid, text in toc)
    chapters = []
    for chapter in course.chapters:
        is_current = any(l.slug == current_slug for l in chapter.lessons)
        items = "".join(
            f'<li{" class=cur" if l.slug == current_slug else ""}><a href="{l.filename}">'
            f'<span class="ln">{lesson_number(l.slug)}</span> {html.escape(l.title)}</a></li>'
            for l in chapter.lessons
        )
        chapters.append(
            f'<details{" open" if is_current else ""}><summary>{html.escape(chapter.title)}</summary>'
            f'<ul class="pages">{items}</ul></details>'
        )
    toc_part = f'<div class="sbhead">On this page</div><ul class="toc">{toc_html}</ul>' if toc else ""
    return f'{toc_part}<div class="sbhead">Course</div>{"".join(chapters)}'


def render_roadmap(course: Course, minutes: dict[str, int]) -> str:
    cards = []
    for chapter in course.chapters:
        if chapter.title == "Start Here":
            continue
        total = sum(minutes.get(l.slug, 0) for l in chapter.lessons)
        items = "".join(
            f'<li><a href="{l.filename}"><span class="ln">{lesson_number(l.slug)}</span> {html.escape(l.title)}</a>'
            f'<span class="rt">{minutes.get(l.slug, 0)} min</span></li>'
            for l in chapter.lessons
        )
        cards.append(
            f'<div class="chapter-card"><div class="chhead"><span>{html.escape(chapter.title)}</span>'
            f'<span class="rt">{len(chapter.lessons)} lessons · ~{total} min</span></div><ul>{items}</ul></div>'
        )
    return '<div class="roadmap">' + "".join(cards) + "</div>"


def _nav_link(lesson: Lesson | None, *, prev: bool) -> str:
    if lesson is None:
        return ""
    label = html.escape(lesson.title)
    return (f'<a class="nav" href="{lesson.filename}">← {label}</a>' if prev
            else f'<a class="nav" href="{lesson.filename}">{label} →</a>')


def build(course: Course | None = None, out_dir: Path = config.DIST_DIR) -> dict[str, int]:
    """Render the whole site into ``out_dir`` and return the reading time per lesson."""
    course = course or config.load_course()
    template = Template((config.TEMPLATES_DIR / "page.html").read_text(encoding="utf-8"))

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    shutil.copytree(config.ASSETS_DIR, out_dir / "assets")

    lessons = course.lessons
    sources = {l.slug: l.source.read_text(encoding="utf-8") for l in lessons if l.source.exists()}
    missing = [l.slug for l in lessons if l.slug not in sources]
    if missing:
        raise FileNotFoundError(f"lessons listed in course.json but missing on disk: {missing}")
    minutes = {slug: reading_minutes(text) for slug, text in sources.items()}

    for k, lesson in enumerate(lessons):
        body, ctx = render_markdown(sources[lesson.slug])
        number = lesson_number(lesson.slug)
        meta = (
            f'<div class="crumb">{html.escape(lesson.chapter)}{" › Lesson " + number if number else ""}</div>'
            f"<h1>{html.escape(lesson.title)}</h1>"
            f'<div class="meta"><span>⏱ {minutes[lesson.slug]} min read</span>'
            f"<span>📚 Syllabus: {html.escape(lesson.syllabus)}</span></div>"
        )
        prev_link = (_nav_link(lessons[k - 1], prev=True) if k > 0
                     else '<a class="nav" href="index.html">← Course Home</a>')
        next_link = _nav_link(lessons[k + 1], prev=False) if k < len(lessons) - 1 else ""
        page = template.substitute(
            title=html.escape(lesson.title), sidebar=render_sidebar(course, lesson.slug, ctx.toc),
            meta=meta, body=body, prev_link=prev_link, next_link=next_link,
        )
        (out_dir / lesson.filename).write_text(page, encoding="utf-8")

    home_source = config.LESSONS_DIR / f"{config.INDEX_SLUG}.md"
    body, ctx = render_markdown(home_source.read_text(encoding="utf-8"))
    body = body.replace(ROADMAP_PLACEHOLDER, render_roadmap(course, minutes))
    first = lessons[0]
    home = template.substitute(
        title="Course Home", sidebar=render_sidebar(course, config.INDEX_SLUG, ctx.toc),
        meta="", body=body, prev_link="",
        next_link=f'<a class="nav" href="{first.filename}">Start: {html.escape(first.title)} →</a>',
    )
    (out_dir / "index.html").write_text(home, encoding="utf-8")
    return minutes
