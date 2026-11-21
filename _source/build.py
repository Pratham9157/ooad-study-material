"""
OOAD study material builder + validator (lesson-per-concept edition).

  python build.py              -> build all HTML pages
  python build.py --check [x]  -> build + compile/run every C++ program (optionally only lessons whose
                                  file name contains x) and compare with the documented output

Markdown dialect:
  ## / ### / ####     headings (the lesson title is generated from COURSE)
  - item / 1. item     lists (indent 2+ spaces to nest)
  | a | b |            tables
  > text               quote / formal definition
  ```cpp / ```output / ```text / ```uml   code blocks
  :::type Title ... :::   boxes: def, analogy, mistakes, exam, key, note, tip, warn, example, summary, q, ans, raw
  <<SVG:name>>         include svg/name.svg
  `code`  **bold**  *italic*  [link](url)

cpp directives (hidden): //@input: text   //@expect: compile-error   //@norun   //@nocheck
"""
import re, html, sys, os, pathlib, subprocess, tempfile, hashlib, json
from concurrent.futures import ThreadPoolExecutor

SRC = pathlib.Path(__file__).resolve().parent
LES = SRC / 'lessons'
OUT = SRC.parent

# (chapter title, [(slug, lesson title, syllabus tag)])
COURSE = [
    ("Start Here", [
        ("00_big_picture", "The Big Picture: What Is OOAD and How to Study It", "Overview"),
    ]),
    ("Chapter 1 · C++ Foundations", [
        ("01_1_first_program", "Your First C++ Program", "Unit 2"),
        ("01_2_variables_types", "Variables, Data Types & Constants", "Unit 2"),
        ("01_3_input_output", "Input and Output (cin / cout)", "Unit 2"),
        ("01_4_operators", "Operators & Expressions", "Unit 2"),
        ("01_5_decisions", "Making Decisions: if, else & switch", "Unit 3"),
        ("01_6_loops", "Loops: Repeating Work", "Unit 3"),
        ("01_7_arrays", "Arrays & C-Strings", "Connected"),
    ]),
    ("Chapter 2 · Functions", [
        ("02_1_functions", "Functions, Top-Down Design & Procedural Abstraction", "Unit 2"),
        ("02_2_scope", "Scope: Local, Global & Static Variables", "Unit 2"),
        ("02_3_pointers_references", "Pointers & References", "Connected"),
        ("02_4_parameter_passing", "Parameter Passing", "Unit 2"),
        ("02_5_overloading", "Function Overloading, Default Arguments & Inline", "Unit 2"),
        ("02_6_recursion", "Recursion", "Unit 2"),
        ("02_7_dynamic_memory", "Dynamic Memory: new & delete", "Connected"),
        ("p1_practice", "✎ Practice Set 1 (Chapters 1–2)", "Practice"),
    ]),
    ("Chapter 3 · OOP Fundamentals", [
        ("03_1_why_oop", "Why OOP? Procedural vs Object-Oriented Thinking", "Unit 1"),
        ("03_2_structures", "Structures: Grouping Different Data", "Unit 3"),
        ("03_3_classes_objects", "Classes and Objects", "Unit 1 · Unit 3"),
        ("03_4_encapsulation", "Encapsulation & Access Specifiers", "Unit 1 · Unit 3"),
        ("03_5_abstraction", "Abstraction", "Unit 1"),
        ("03_6_object_references", "Object References: Pointers, References & Passing Objects", "Unit 1"),
        ("03_7_constructors", "Constructors & Constructor Overloading", "Unit 1 · Unit 3"),
        ("03_8_destructors", "Destructors", "Unit 2"),
    ]),
    ("Chapter 4 · Advanced Class Features", [
        ("04_1_this_pointer", "The this Pointer", "Unit 2"),
        ("04_2_copy_constructor", "Copy Constructor: Shallow vs Deep Copy", "Unit 2"),
        ("04_3_assignment_operator", "Overloading the Assignment Operator", "Unit 2"),
        ("04_4_operator_overloading", "Operator Overloading", "Unit 2"),
        ("04_5_friends", "Friend Functions & Friend Classes", "Unit 2 · Unit 3"),
        ("04_6_static_const", "Static Members, const Members & Recursive Member Functions", "Unit 2"),
        ("p2_practice", "✎ Practice Set 2 (Chapters 1–4)", "Practice"),
    ]),
    ("Chapter 5 · Inheritance & Polymorphism", [
        ("05_1_inheritance", "Inheritance: Reusing Classes", "Unit 3"),
        ("05_2_types_of_inheritance", "Types of Inheritance & the Diamond Problem", "Unit 3"),
        ("05_3_ctor_order_overriding", "Constructors in Inheritance & Function Overriding", "Unit 3"),
        ("05_4_polymorphism_virtual", "Polymorphism & Virtual Functions", "Unit 2"),
        ("05_5_abstract_classes", "Abstract Classes, Interfaces & Virtual Destructors", "Unit 2"),
    ]),
    ("Chapter 6 · Streams, Files & Standard Classes", [
        ("06_1_streams_formatting", "Streams & Formatting Output", "Unit 3"),
        ("06_2_character_io", "Character I/O", "Unit 3"),
        ("06_3_files", "File Handling", "Unit 3"),
        ("06_4_string_vector", "Standard Classes: string & vector", "Unit 3"),
        ("p3_practice", "✎ Practice Set 3 (Part I Complete)", "Practice"),
    ]),
    ("Chapter 7 · Introduction to OOAD", [
        ("07_1_ooa_ood", "What Are OOA and OOD?", "Unit 4"),
        ("07_2_unified_process", "The Unified Process", "Unit 4"),
        ("07_3_uml_intro", "Introduction to UML", "Unit 4"),
    ]),
    ("Chapter 8 · Class Relationships", [
        ("08_1_association", "Association & Multiplicity", "Unit 4"),
        ("08_2_aggregation_composition", "Aggregation & Composition", "Unit 4"),
        ("08_3_dependency_generalization_realization", "Dependency, Generalization & Realization", "Unit 4"),
    ]),
    ("Chapter 9 · Use Cases", [
        ("09_1_use_cases", "Use Cases, Actors & Scenarios", "Unit 4"),
        ("09_2_use_case_diagrams", "Use Case Diagrams: Include, Extend & Generalization", "Unit 4"),
    ]),
    ("Chapter 10 · Class Diagrams & the Domain Model", [
        ("10_1_class_diagrams", "Class Diagrams", "Unit 4"),
        ("10_2_domain_model", "The Domain Model: Finding Conceptual Classes", "Unit 4"),
        ("10_3_associations_attributes", "Domain Model: Associations & Attributes", "Unit 4"),
        ("10_4_domain_refinement", "Domain Model Refinement & Class Hierarchies", "Unit 4"),
        ("p4_practice", "✎ Practice Set 4 (Chapters 7–10)", "Practice"),
    ]),
    ("Chapter 11 · Interaction Diagrams", [
        ("11_1_ssd", "System Sequence Diagrams", "Unit 4 · Unit 5"),
        ("11_2_sequence_diagrams", "Sequence Diagrams", "Unit 5"),
        ("11_3_communication_diagrams", "Communication (Collaboration) Diagrams", "Unit 5"),
    ]),
    ("Chapter 12 · State, Activity & Implementation Diagrams", [
        ("12_1_state_machine", "State Machine Diagrams", "Unit 5"),
        ("12_2_activity", "Activity Diagrams", "Unit 5"),
        ("12_3_implementation_diagrams", "Package, Component & Deployment Diagrams", "Unit 5"),
    ]),
    ("Chapter 13 · Design Principles & GRASP", [
        ("13_1_coupling_cohesion", "Coupling & Cohesion", "Unit 6"),
        ("13_2_grasp_expert_creator", "GRASP: Information Expert & Creator", "Unit 6"),
        ("13_3_grasp_controller", "GRASP: Controller, Low Coupling, High Cohesion (+4 more)", "Unit 6"),
        ("13_4_solid", "Bonus: SOLID Principles", "Connected"),
    ]),
    ("Chapter 14 · Design Patterns", [
        ("14_1_intro_patterns", "Introduction to Design Patterns", "Unit 6"),
        ("14_2_factory_method", "Factory Method Pattern", "Unit 6"),
        ("14_3_singleton", "Singleton Pattern", "Connected"),
        ("14_4_adapter", "Adapter Pattern", "Unit 6"),
        ("14_5_bridge", "Bridge Pattern", "Unit 6"),
        ("14_6_strategy", "Strategy Pattern", "Unit 6"),
        ("14_7_observer", "Observer Pattern", "Unit 6"),
        ("14_8_applying_patterns_mapping", "Applying Patterns & Mapping Design to Code", "Unit 6"),
        ("p5_practice", "✎ Practice Set 5 + Full Mock Paper", "Practice"),
    ]),
]

FLAT = [(c, s, t, u) for c, ls in COURSE for (s, t, u) in ls]

# ----------------------------------------------------------------- inline
def inline(text):
    codes = []
    def stash(m):
        codes.append('<code>' + html.escape(m.group(1), quote=False) + '</code>')
        return f'\x00{len(codes)-1}\x00'
    s = re.sub(r'`([^`]+)`', stash, text)
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?=[^\s*])([^*\n]+?)(?<=[^\s*])\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', s)
    s = s.replace('&lt;br&gt;', '<br>')
    return re.sub(r'\x00(\d+)\x00', lambda m: codes[int(m.group(1))], s)

def slugify(t, used):
    s = re.sub(r'[^a-z0-9]+', '-', t.lower().replace('`', '')).strip('-')[:60] or 'sec'
    base, k = s, 2
    while s in used:
        s = f"{base}-{k}"; k += 1
    used.add(s)
    return s

# ----------------------------------------------------------------- code
CPP_KW = set("""alignas alignof and asm auto bool break case catch char class const constexpr
const_cast continue decltype default delete do double dynamic_cast else enum explicit export
extern false float for friend goto if inline int long mutable namespace new noexcept not nullptr
operator or private protected public register reinterpret_cast return short signed sizeof static
static_assert static_cast struct switch template this throw true try typedef typeid typename union
unsigned using virtual void volatile wchar_t while override final""".split())
CPP_LIB = set("""cout cin endl cerr clog string vector std main getline setw setprecision fixed
setfill left right ifstream ofstream fstream ios showpoint boolalpha noboolalpha scientific hex oct dec
size_t""".split())
TOK = re.compile(r'(?P<com>//[^\n]*|/\*.*?\*/)|(?P<str>"(?:\\.|[^"\\\n])*"|\'(?:\\.|[^\'\\\n])*\')'
                 r'|(?P<pre>^[ \t]*#[^\n]*)|(?P<num>\b\d+(?:\.\d+)?(?:[eE][+-]?\d+)?[fFlLuU]*\b)'
                 r'|(?P<id>\b[A-Za-z_]\w*\b)', re.S | re.M)

def hl_cpp(code):
    out, last = [], 0
    for m in TOK.finditer(code):
        out.append(html.escape(code[last:m.start()], quote=False))
        t = m.group(0); e = html.escape(t, quote=False); k = m.lastgroup
        if k == 'id':
            out.append(f'<span class="kw">{e}</span>' if t in CPP_KW else
                       f'<span class="lib">{e}</span>' if t in CPP_LIB else e)
        else:
            out.append(f'<span class="{k}">{e}</span>')
        last = m.end()
    out.append(html.escape(code[last:], quote=False))
    return ''.join(out)

LABELS = {'cpp': 'C++', 'output': 'Output', 'text': '', 'uml': 'Diagram'}

def render_code(lang, lines):
    if lang == 'cpp':
        lines = [l for l in lines if not l.strip().startswith('//@')]
    code = '\n'.join(lines)
    body = hl_cpp(code) if lang == 'cpp' else html.escape(code, quote=False)
    label = LABELS.get(lang, lang)
    lab = f'<div class="codelabel">{label}</div>' if label else ''
    return f'<div class="codewrap {lang or "text"}">{lab}<pre><code>{body}</code></pre></div>'

# ----------------------------------------------------------------- tables / lists
def split_row(line):
    line = line.strip()
    if line.startswith('|'): line = line[1:]
    if line.endswith('|') and not line.endswith('\\|'): line = line[:-1]
    cells, cur, intick, i = [], '', False, 0
    while i < len(line):
        c = line[i]
        if c == '\\' and i + 1 < len(line) and line[i+1] == '|':
            cur += '|'; i += 2; continue
        if c == '`': intick = not intick
        if c == '|' and not intick:
            cells.append(cur.strip()); cur = ''
        else:
            cur += c
        i += 1
    cells.append(cur.strip())
    return cells

def render_table(rows):
    head = split_row(rows[0])
    sep = len(rows) > 1 and re.match(r'^\s*\|?\s*:?-', rows[1])
    body = [split_row(r) for r in (rows[2:] if sep else rows[1:])]
    h = '<div class="tablewrap"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>'
    for r in body:
        h += '<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>'
    return h + '</tbody></table></div>'

LIST_RE = re.compile(r'^(\s*)([-*]|\d+\.)\s+(.*)$')

def render_list(items):
    def rec(idx, indent):
        tag = 'ol' if items[idx][1] else 'ul'
        s = [f'<{tag}>']
        while idx < len(items) and items[idx][0] >= indent:
            ind, ordered, text = items[idx]
            if ind > indent:
                sub, idx = rec(idx, ind)
                s[-1] = s[-1][:-5] + sub + '</li>'
                continue
            s.append('<li>' + inline(text) + '</li>'); idx += 1
        s.append(f'</{tag}>')
        return ''.join(s), idx
    return rec(0, items[0][0])[0]

# ----------------------------------------------------------------- containers
BOXES = {
    'def':      ('def',      '📘 Exam-Ready Definition'),
    'analogy':  ('analogy',  '🧠 Real-World Analogy'),
    'mistakes': ('mistakes', '⚠️ Common Mistakes Students Make'),
    'exam':     ('exam',     '📝 How This Is Asked in Exams'),
    'key':      ('key',      '🔑 Key Takeaways'),
    'note':     ('note',     '📝 Note'),
    'tip':      ('tip',      '💡 Tip'),
    'warn':     ('warn',     '🚫 Important'),
    'example':  ('example',  '🌍 Example'),
    'summary':  ('summary',  '✅ Quick Revision'),
}

class Ctx:
    def __init__(self): self.used = set(); self.toc = []

def render_container(typ, title, inner, ctx):
    if typ == 'raw':
        return '\n'.join(inner)
    body = parse_blocks(inner, ctx)
    if typ == 'q':
        return f'<div class="q"><div class="qhead">{inline(title)}</div>{body}</div>'
    if typ == 'ans':
        return f'<details class="ans"><summary>{inline(title) if title else "Show Answer"}</summary><div class="ansbody">{body}</div></details>'
    cls, default = BOXES.get(typ, ('note', typ))
    return f'<div class="box {cls}"><div class="boxtitle">{inline(title) if title else default}</div>{body}</div>'

def svg_include(name):
    p = SRC / 'svg' / f'{name}.svg'
    if not p.exists(): raise SystemExit(f'missing svg {name}')
    return f'<div class="svgwrap">{p.read_text(encoding="utf-8")}</div>'

def parse_blocks(lines, ctx):
    out, para, i, n = [], [], 0, len(lines)
    def flush():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>'); para.clear()
    while i < n:
        line = lines[i]; s = line.strip()
        if s.startswith('```'):
            flush(); lang = s[3:].strip(); j = i + 1; buf = []
            while j < n and lines[j].strip() != '```':
                buf.append(lines[j]); j += 1
            out.append(render_code(lang, buf)); i = j + 1; continue
        if s.startswith(':::') and len(s) > 3:
            flush(); typ, _, title = s[3:].strip().partition(' ')
            depth, j, infence = 1, i + 1, False
            while j < n:
                t = lines[j].strip()
                if t.startswith('```'): infence = not infence
                elif not infence:
                    if t == ':::':
                        depth -= 1
                        if depth == 0: break
                    elif t.startswith(':::'): depth += 1
                j += 1
            if j >= n: raise SystemExit(f"Unclosed container near: {line[:70]}")
            out.append(render_container(typ, title.strip(), lines[i+1:j], ctx)); i = j + 1; continue
        m = re.match(r'^<<SVG:(\w+)>>$', s)
        if m:
            flush(); out.append(svg_include(m.group(1))); i += 1; continue
        if s == '':
            flush(); i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', s)
        if m:
            flush(); lvl = len(m.group(1)); txt = m.group(2); hid = slugify(txt, ctx.used)
            if lvl in (2, 3): ctx.toc.append((lvl, hid, txt))
            out.append(f'<h{lvl} id="{hid}">{inline(txt)}</h{lvl}>'); i += 1; continue
        if s == '---':
            flush(); out.append('<hr>'); i += 1; continue
        if s.startswith('>'):
            flush(); buf = []
            while i < n and lines[i].strip().startswith('>'):
                buf.append(lines[i].strip()[1:].strip()); i += 1
            out.append('<blockquote>' + inline(' '.join(buf)) + '</blockquote>'); continue
        if s.startswith('|'):
            flush(); rows = []
            while i < n and lines[i].strip().startswith('|'):
                rows.append(lines[i]); i += 1
            out.append(render_table(rows)); continue
        if LIST_RE.match(line):
            flush(); items = []
            while i < n:
                mm = LIST_RE.match(lines[i])
                if mm:
                    items.append([len(mm.group(1).expandtabs()), mm.group(2)[0].isdigit(), mm.group(3)]); i += 1
                elif lines[i].strip() and lines[i].startswith('  ') and items:
                    items[-1][2] += ' ' + lines[i].strip(); i += 1
                else:
                    break
            out.append(render_list(items)); continue
        para.append(s); i += 1
    flush()
    return '\n'.join(out)

# ----------------------------------------------------------------- page template
def read_minutes(md):
    prose = re.sub(r'```.*?```', '', md, flags=re.S)
    code_lines = sum(b.count('\n') for b in re.findall(r'```.*?```', md, flags=re.S))
    return max(2, round(len(prose.split()) / 200 + code_lines / 40))

def lesson_number(slug):
    m = re.match(r'(\d\d)_(\d)_', slug)
    return f"{int(m.group(1))}.{m.group(2)}" if m else ''

def sidebar(cur_slug, toc):
    toc_html = ''.join(f'<li class="l{l}"><a href="#{h}">{inline(t)}</a></li>' for l, h, t in toc)
    chapters = []
    for ch, ls in COURSE:
        is_cur = any(s == cur_slug for s, _, _ in ls)
        items = ''.join(
            f'<li{" class=cur" if s == cur_slug else ""}><a href="{s}.html">'
            f'<span class="ln">{lesson_number(s)}</span> {html.escape(t)}</a></li>' for s, t, _ in ls)
        chapters.append(f'<details{" open" if is_cur else ""}><summary>{html.escape(ch)}</summary><ul class="pages">{items}</ul></details>')
    toc_part = f'<div class="sbhead">On this page</div><ul class="toc">{toc_html}</ul>' if toc else ''
    return f'{toc_part}<div class="sbhead">Course</div>{"".join(chapters)}'

def page(title, body, toc, slug, meta_html, prev_link, next_link):
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — OOAD Study Material</title>
<script>if(localStorage.getItem('ooad-theme')==='dark')document.documentElement.classList.add('dark');</script>
<link rel="stylesheet" href="assets/style.css">
</head><body>
<header class="topbar">
  <a class="home" href="index.html">📚 OOAD Course</a>
  <span class="ptitle">{html.escape(title)}</span>
  <span class="tools">
    <button id="toggleAns" type="button">Show all answers</button>
    <button id="toggleTheme" type="button" title="Toggle dark mode">🌓</button>
  </span>
</header>
<div class="layout">
<aside class="sidebar">{sidebar(slug, toc)}</aside>
<main>
{meta_html}
{body}
<div class="pager">{prev_link}<span></span>{next_link}</div>
</main>
</div>
<script src="assets/app.js"></script>
</body></html>"""

def roadmap_html(minutes):
    parts = []
    for ch, ls in COURSE:
        if ch == "Start Here": continue
        total = sum(minutes.get(s, 0) for s, _, _ in ls)
        items = ''.join(
            f'<li><a href="{s}.html"><span class="ln">{lesson_number(s)}</span> {html.escape(t)}</a>'
            f'<span class="rt">{minutes.get(s, 0)} min</span></li>' for s, t, _ in ls)
        parts.append(f'<div class="chapter-card"><div class="chhead"><span>{html.escape(ch)}</span>'
                     f'<span class="rt">{len(ls)} lessons · ~{total} min</span></div><ul>{items}</ul></div>')
    return '<div class="roadmap">' + ''.join(parts) + '</div>'

def build():
    minutes = {}
    sources = {}
    for ch, s, t, u in FLAT:
        p = LES / f'{s}.md'
        if p.exists():
            sources[s] = p.read_text(encoding='utf-8'); minutes[s] = read_minutes(sources[s])
    # lessons
    for k, (ch, s, t, u) in enumerate(FLAT):
        if s not in sources:
            print(f"  (missing) {s}"); continue
        ctx = Ctx()
        body = parse_blocks(sources[s].splitlines(), ctx)
        num = lesson_number(s)
        meta = (f'<div class="crumb">{html.escape(ch)}{" › Lesson " + num if num else ""}</div>'
                f'<h1>{html.escape(t)}</h1>'
                f'<div class="meta"><span>⏱ {minutes[s]} min read</span><span>📚 Syllabus: {html.escape(u)}</span></div>')
        prev_link = next_link = ''
        if k > 0:
            p = FLAT[k-1]; prev_link = f'<a class="nav" href="{p[1]}.html">← {html.escape(p[2])}</a>'
        else:
            prev_link = '<a class="nav" href="index.html">← Course Home</a>'
        if k < len(FLAT) - 1:
            n_ = FLAT[k+1]; next_link = f'<a class="nav" href="{n_[1]}.html">{html.escape(n_[2])} →</a>'
        (OUT / f'{s}.html').write_text(page(t, body, ctx.toc, s, meta, prev_link, next_link), encoding='utf-8')
    # index
    idx = LES / 'index.md'
    if idx.exists():
        ctx = Ctx()
        text = idx.read_text(encoding='utf-8')
        body = parse_blocks(text.splitlines(), ctx).replace('<p>&lt;&lt;ROADMAP&gt;&gt;</p>', roadmap_html(minutes))
        first = FLAT[0][1]
        (OUT / 'index.html').write_text(page('Course Home', body, ctx.toc, 'index', '', '',
                                             f'<a class="nav" href="{first}.html">Start: {html.escape(FLAT[0][2])} →</a>'),
                                        encoding='utf-8')
    print(f"  built {len(sources)} lessons + index ({sum(minutes.values())} min total)")

# ----------------------------------------------------------------- validation
def extract_programs(text):
    lines = text.splitlines(); blocks, i = [], 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith('```'):
            lang = s[3:].strip(); j = i + 1; buf = []
            while j < len(lines) and lines[j].strip() != '```':
                buf.append(lines[j]); j += 1
            blocks.append((i + 1, lang, buf)); i = j + 1
        else:
            i += 1
    progs = []
    for k, (ln, lang, buf) in enumerate(blocks):
        if lang != 'cpp': continue
        code = '\n'.join(buf)
        d = {'input': [], 'expect': None, 'norun': False, 'nocheck': False}
        for l in buf:
            t = l.strip()
            if t.startswith('//@input:'): d['input'].append(t[9:].strip())
            elif t.startswith('//@expect:'): d['expect'] = t[10:].strip()
            elif t == '//@norun': d['norun'] = True
            elif t == '//@nocheck': d['nocheck'] = True
        if d['nocheck'] or not re.search(r'\bint\s+main\s*\(', code): continue
        exp = '\n'.join(blocks[k+1][2]) if k + 1 < len(blocks) and blocks[k+1][1] == 'output' else None
        progs.append((ln, code, exp, d))
    return progs

def norm(s):
    return '\n'.join(l.rstrip() for l in s.replace('\r\n', '\n').split('\n')).rstrip('\n')

GXX_DIR = 'C:/msys64/ucrt64/bin'
ENV = dict(os.environ, PATH=GXX_DIR + os.pathsep + os.environ.get('PATH', ''))

def run_one(args):
    src, ln, code, exp, d, cache = args
    key = hashlib.sha1((code + '\x00' + (exp or '') + json.dumps(d)).encode()).hexdigest()
    if cache.get(key) == 'ok':
        return (src, ln, 'ok', '', key)
    with tempfile.TemporaryDirectory() as td:
        cpp = os.path.join(td, 'p.cpp'); exe = os.path.join(td, 'p.exe')
        open(cpp, 'w', encoding='utf-8').write(code)
        c = subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', '-static', '-o', exe, cpp],
                           capture_output=True, text=True, env=ENV)
        if d['expect'] == 'compile-error':
            return (src, ln, 'FAIL', 'expected compile error but compiled OK', None) if c.returncode == 0 else (src, ln, 'ok', '', key)
        if c.returncode != 0:
            return (src, ln, 'FAIL', 'COMPILE ERROR:\n' + c.stderr[:1500], None)
        if d['norun']:
            return (src, ln, 'ok', '', key)
        try:
            r = subprocess.run([exe], input='\n'.join(d['input']) + '\n', capture_output=True,
                               text=True, timeout=10, cwd=td, env=ENV)
        except subprocess.TimeoutExpired:
            return (src, ln, 'FAIL', 'TIMEOUT', None)
        if exp is None:
            return (src, ln, 'nodoc', norm(r.stdout)[:300], key)
        if norm(r.stdout) != norm(exp):
            return (src, ln, 'FAIL', f'OUTPUT MISMATCH\n--- expected ---\n{norm(exp)}\n--- actual ---\n{norm(r.stdout)}', None)
        return (src, ln, 'ok', '', key)

def check(only=None):
    cache_file = SRC / '.cache.json'
    cache = json.loads(cache_file.read_text()) if cache_file.exists() else {}
    jobs = []
    for _, s, _, _ in FLAT:
        if only and only not in s: continue
        p = LES / f'{s}.md'
        if p.exists():
            for ln, code, exp, d in extract_programs(p.read_text(encoding='utf-8')):
                jobs.append((s, ln, code, exp, d, cache))
    print(f"Checking {len(jobs)} programs...")
    fails = nodoc = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        for src, ln, status, msg, key in ex.map(run_one, jobs):
            if status == 'FAIL':
                fails += 1; print(f"\n[FAIL] {src}.md:{ln}\n{msg}")
            else:
                if key: cache[key] = 'ok'
                if status == 'nodoc':
                    nodoc += 1; print(f"[no output block] {src}.md:{ln} -> prints: {msg!r}")
    cache_file.write_text(json.dumps(cache))
    print(f"\nDone: {len(jobs)} programs, {fails} failures, {nodoc} without documented output.")
    return fails

if __name__ == '__main__':
    os.chdir(SRC)
    build()
    if '--check' in sys.argv:
        i = sys.argv.index('--check')
        sys.exit(1 if check(sys.argv[i+1] if len(sys.argv) > i + 1 else None) else 0)
