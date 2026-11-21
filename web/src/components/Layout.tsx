import { useCallback, useEffect, useState } from "react";
import { Link, Outlet, useLocation } from "react-router-dom";
import { Eye, EyeOff, GraduationCap, Moon, Sun } from "lucide-react";
import { useDarkMode, useStoredBoolean } from "../hooks";
import { course, findLesson, HOME_SLUG } from "../course";
import { Sidebar } from "./Sidebar";
import { TocPanel } from "./TocPanel";

/** Context passed to lesson pages through <Outlet />. */
export interface LayoutContext {
  showAll: boolean;
}

/**
 * The persistent shell: top bar, course sidebar (left) and "On this page" (right). These live
 * outside <Outlet />, so they stay mounted while the reader moves between lessons. That keeps
 * the course list's scroll position and open chapters intact.
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

  // Ctrl+B / Cmd+B toggles the course sidebar (the common docs/editor shortcut).
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && !e.shiftKey && !e.altKey && e.key.toLowerCase() === "b") {
        e.preventDefault();
        toggleLeft();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [toggleLeft]);

  return (
    <>
      <header className="topbar">
        <Link className="brand" to="/">
          <GraduationCap className="icon" size={20} aria-hidden="true" />
          OOAD Course
        </Link>
        {current && (
          <span className="topbar-sep" aria-hidden="true">
            /
          </span>
        )}
        <span className="ptitle">{current ? current.title : ""}</span>
        <div className="topbar-actions">
          <button type="button" className="btn-ghost" onClick={toggleAnswers} aria-pressed={showAll}>
            {showAll ? (
              <EyeOff className="icon" size={16} aria-hidden="true" />
            ) : (
              <Eye className="icon" size={16} aria-hidden="true" />
            )}
            {showAll ? "Hide answers" : "Show answers"}
          </button>
          <button
            type="button"
            className="icon-btn"
            onClick={toggleDark}
            aria-label={dark ? "Switch to light theme" : "Switch to dark theme"}
            title={dark ? "Light theme" : "Dark theme"}
          >
            {dark ? <Sun className="icon" size={18} aria-hidden="true" /> : <Moon className="icon" size={18} aria-hidden="true" />}
          </button>
        </div>
      </header>
      <div className="layout">
        <Sidebar currentSlug={slug} collapsed={leftCollapsed} onToggle={toggleLeft} />
        <main>
          <div className="content">
            <Outlet context={{ showAll } satisfies LayoutContext} />
          </div>
        </main>
        <TocPanel toc={toc} pageKey={slug} collapsed={rightCollapsed} onToggle={toggleRight} />
      </div>
    </>
  );
}
