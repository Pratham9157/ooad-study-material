# OOAD Study Material

A static, lesson-by-lesson study site for an Object-Oriented Analysis & Design course:
C++ foundations, OOP, UML, GRASP and GoF design patterns. Every C++ example is compiled
and run by the validator, and its output is checked against the documented output.

## Layout

```
content/
  course.json        course outline: chapters, lesson slugs, titles, syllabus mapping
  lessons/           one Markdown file per lesson (plus index.md for the home page)
  diagrams/          SVG diagrams, inlined with <<SVG:name>>
src/
  assets/            style.css and app.js, copied as-is
  templates/         page.html, the HTML shell every page is rendered into
tools/
  ooad.py            command-line entry point (build | check | serve)
  ooadsite/          Markdown renderer, site builder, C++ validator
dist/                generated site (not committed)
```

## Usage

Requires Python 3.10+. The build uses only the standard library.

```bash
python tools/ooad.py build          # render the site into dist/
python tools/ooad.py serve 8000     # build and preview at http://localhost:8000
python tools/ooad.py check          # compile and run all C++ examples (needs g++)
python tools/ooad.py check 05_      # only lessons whose file name contains "05_"
```

The validator looks for `g++` on `PATH`. Set `OOAD_GXX` to a full compiler path to override.

## Writing a lesson

1. Add the lesson's slug, title and syllabus tag to `content/course.json`.
2. Create `content/lessons/<slug>.md`. Use the Markdown dialect documented in `tools/ooadsite/markdown.py`.
3. Run `python tools/ooad.py check <slug>` if the lesson contains C++.

## Deployment

Vercel runs `python3 tools/ooad.py build` and serves `dist/` (see `vercel.json`).
