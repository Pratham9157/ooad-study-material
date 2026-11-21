import { useCallback, useState } from "react";
import { Link, Outlet, useLocation } from "react-router-dom";
import { useDarkMode, useStoredBoolean } from "../hooks";
import { course, findLesson, HOME_SLUG } from "../course";
import { Sidebar } from "./Sidebar";
import { TocPanel } from "./TocPanel";

/** Context passed to lesson pages through <Outlet />. */
export interface LayoutContext {
  showAll: boolean;
}

/**
 * The persistent shell. The topbar, the left course sidebar and the answer toggle live here,
 * outside <Outlet />, so they stay mounted while the reader moves between lessons. That keeps the
 * sidebar's scroll position and its open chapters intact. The right-hand "On this page" panel
 * lists the headings of whichever page is showing.
 */
export function Layout() {
  const [dark, toggleDark] = useDarkMode();
  const [showAll, setShowAll] = useState(false);
  const [leftCollapsed, toggleLeft] = useStoredBoolean("ooad-left-collapsed");
  const [rightCollapsed, toggleRight] = useStoredBoolean("ooad-right-collapsed");
  const { pathname } = useLocation();

  const slug = pathname === "/" ? HOME_SLUG : pathname.replace(/^\//, "");
  const current = findLesson(slug);
  const toc = current ? current.toc : slug === HOME_SLUG ? course.intro.toc : [];

  const toggleAnswers = useCallback(() => setShowAll((s) => !s), []);

  return (
    <>
      <header className="topbar">
        <button
          type="button"
          className="tool-left panel-toggle"
          onClick={toggleLeft}
          aria-pressed={!leftCollapsed}
          aria-label={leftCollapsed ? "Show course list" : "Hide course list"}
          title={leftCollapsed ? "Show course list" : "Hide course list"}
        >
          <span aria-hidden="true">☰</span> Course
        </button>
        <Link className="home" to="/">
          📚 OOAD Course
        </Link>
        <span className="ptitle">{current ? current.title : "Course Home"}</span>
        <span className="tools">
          <button
            type="button"
            className="tool-right panel-toggle"
            onClick={toggleRight}
            disabled={toc.length === 0}
            aria-pressed={!rightCollapsed}
            aria-label={rightCollapsed ? "Show on this page" : "Hide on this page"}
            title={rightCollapsed ? "Show 'On this page'" : "Hide 'On this page'"}
          >
            On this page <span aria-hidden="true">☰</span>
          </button>
          <button type="button" onClick={toggleAnswers}>
            {showAll ? "Hide all answers" : "Show all answers"}
          </button>
          <button type="button" onClick={toggleDark} title="Toggle dark mode" aria-label="Toggle dark mode">
            {dark ? "☀️" : "🌓"}
          </button>
        </span>
      </header>
      <div className={`layout${leftCollapsed ? " left-collapsed" : ""}${rightCollapsed ? " right-collapsed" : ""}`}>
        <Sidebar currentSlug={slug} collapsed={leftCollapsed} />
        <main>
          <Outlet context={{ showAll } satisfies LayoutContext} />
        </main>
        <TocPanel toc={toc} pageKey={slug} collapsed={rightCollapsed} />
      </div>
    </>
  );
}
