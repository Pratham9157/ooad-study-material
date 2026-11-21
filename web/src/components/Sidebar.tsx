import { useEffect, useLayoutEffect, useRef, useState } from "react";
import { Link } from "react-router-dom";
import { course, lessonPath } from "../course";

const SCROLL_KEY = "ooad-sidebar-scroll";

interface SidebarProps {
  currentSlug: string;
}

/** The chapter that contains a lesson, or null for the home page. */
function chapterOf(slug: string): string | null {
  const chapter = course.chapters.find((c) => c.lessons.includes(slug));
  return chapter ? chapter.title : null;
}

/**
 * Left sidebar: the course list. It is the scroll container whose position is kept while the
 * reader moves between lessons. ("On this page" lives in the separate right-hand TocPanel, so
 * the list never shifts when the lesson changes.)
 */
export function Sidebar({ currentSlug }: SidebarProps) {
  const navRef = useRef<HTMLElement>(null);
  const activeChapter = chapterOf(currentSlug);

  // Chapters the reader has opened. The chapter of the current lesson starts open, and the
  // first render already includes it, so the saved scroll position can be restored correctly.
  const [openChapters, setOpenChapters] = useState<Set<string>>(
    () => new Set(activeChapter ? [activeChapter] : []),
  );

  useEffect(() => {
    if (!activeChapter) return;
    setOpenChapters((prev) => (prev.has(activeChapter) ? prev : new Set(prev).add(activeChapter)));
  }, [activeChapter]);

  // Restore the saved scroll position on first mount (for example after a full page reload).
  useLayoutEffect(() => {
    const saved = Number(sessionStorage.getItem(SCROLL_KEY));
    if (navRef.current && Number.isFinite(saved)) navRef.current.scrollTop = saved;
  }, []);

  // Remember the scroll position as the reader scrolls.
  useEffect(() => {
    const nav = navRef.current;
    if (!nav) return;
    const onScroll = () => sessionStorage.setItem(SCROLL_KEY, String(nav.scrollTop));
    nav.addEventListener("scroll", onScroll, { passive: true });
    return () => nav.removeEventListener("scroll", onScroll);
  }, []);

  function toggleChapter(title: string) {
    setOpenChapters((prev) => {
      const next = new Set(prev);
      if (next.has(title)) next.delete(title);
      else next.add(title);
      return next;
    });
  }

  return (
    <aside className="sidebar">
      <nav className="course-nav" ref={navRef} aria-label="Course">
        <div className="sbhead">Course</div>
        {course.chapters.map((chapter) => {
          const open = openChapters.has(chapter.title);
          return (
            <section key={chapter.title} className="chapter-nav">
              <button
                type="button"
                className="chapter-toggle"
                aria-expanded={open}
                onClick={() => toggleChapter(chapter.title)}
              >
                <span className="caret">{open ? "▾" : "▸"}</span> {chapter.title}
              </button>
              {open && (
                <ul className="pages">
                  {chapter.lessons.map((slug) => {
                    const lesson = course.lessons.find((l) => l.slug === slug);
                    if (!lesson) return null;
                    const isCurrent = slug === currentSlug;
                    return (
                      <li key={slug} className={isCurrent ? "cur" : undefined}>
                        <Link to={lessonPath(slug)} aria-current={isCurrent ? "page" : undefined}>
                          <span className="ln">{lesson.number}</span> {lesson.title}
                        </Link>
                      </li>
                    );
                  })}
                </ul>
              )}
            </section>
          );
        })}
      </nav>
    </aside>
  );
}
