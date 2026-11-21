import { useCallback, useState } from "react";
import { Link, Outlet, useLocation } from "react-router-dom";
import { useDarkMode } from "../hooks";
import { course, findLesson, HOME_SLUG } from "../course";
import { Sidebar } from "./Sidebar";

/** Context passed to lesson pages through <Outlet />. */
export interface LayoutContext {
  showAll: boolean;
}

/**
 * The persistent shell. The sidebar, topbar and answer toggle live here, outside <Outlet />,
 * so they stay mounted while the reader moves between lessons. That keeps the sidebar's
 * scroll position and its open chapters intact.
 */
export function Layout() {
  const [dark, toggleDark] = useDarkMode();
  const [showAll, setShowAll] = useState(false);
  const { pathname } = useLocation();

  const slug = pathname === "/" ? HOME_SLUG : pathname.replace(/^\//, "");
  const current = findLesson(slug);
  const toc = current ? current.toc : slug === HOME_SLUG ? course.intro.toc : [];

  const toggleAnswers = useCallback(() => setShowAll((s) => !s), []);

  return (
    <>
      <header className="topbar">
        <Link className="home" to="/">
          📚 OOAD Course
        </Link>
        <span className="ptitle">{current ? current.title : "Course Home"}</span>
        <span className="tools">
          <button type="button" onClick={toggleAnswers}>
            {showAll ? "Hide all answers" : "Show all answers"}
          </button>
          <button type="button" onClick={toggleDark} title="Toggle dark mode" aria-label="Toggle dark mode">
            {dark ? "☀️" : "🌓"}
          </button>
        </span>
      </header>
      <div className="layout">
        <Sidebar currentSlug={slug} toc={toc} />
        <main>
          <Outlet context={{ showAll } satisfies LayoutContext} />
        </main>
      </div>
    </>
  );
}
