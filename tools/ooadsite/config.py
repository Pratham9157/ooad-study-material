"""Project paths and the course outline (loaded from ``content/course.json``)."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT_DIR = ROOT / "content"
LESSONS_DIR = CONTENT_DIR / "lessons"
DIAGRAMS_DIR = CONTENT_DIR / "diagrams"
COURSE_FILE = CONTENT_DIR / "course.json"
ASSETS_DIR = ROOT / "src" / "assets"
TEMPLATES_DIR = ROOT / "src" / "templates"
DIST_DIR = ROOT / "dist"
CACHE_DIR = ROOT / ".cache"

INDEX_SLUG = "index"  # content/lessons/index.md is the home page


@dataclass(frozen=True)
class Lesson:
    slug: str
    title: str
    syllabus: str
    chapter: str

    @property
    def source(self) -> Path:
        return LESSONS_DIR / f"{self.slug}.md"

    @property
    def filename(self) -> str:
        return f"{self.slug}.html"


@dataclass(frozen=True)
class Chapter:
    title: str
    lessons: tuple[Lesson, ...]


@dataclass(frozen=True)
class Course:
    title: str
    chapters: tuple[Chapter, ...]

    @property
    def lessons(self) -> list[Lesson]:
        """All lessons in reading order."""
        return [lesson for chapter in self.chapters for lesson in chapter.lessons]


def load_course(path: Path = COURSE_FILE) -> Course:
    data = json.loads(path.read_text(encoding="utf-8"))
    chapters = tuple(
        Chapter(
            title=ch["title"],
            lessons=tuple(
                Lesson(slug=l["slug"], title=l["title"], syllabus=l["syllabus"], chapter=ch["title"])
                for l in ch["lessons"]
            ),
        )
        for ch in data["chapters"]
    )
    return Course(title=data["title"], chapters=chapters)
