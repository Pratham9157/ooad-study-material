import { useEffect, useState } from "react";
import type { TocEntry } from "../types";

interface TocPanelProps {
  /** Headings of the current page. Changing this (a new lesson) resets the highlighted section. */
  toc: TocEntry[];
  /** Key that changes on every page, so the scroll-spy re-attaches to the new headings. */
  pageKey: string;
}

/** Right-hand "On this page" navigation with a scroll-spy that highlights the section in view. */
export function TocPanel({ toc, pageKey }: TocPanelProps) {
  const [activeId, setActiveId] = useState<string | null>(toc[0]?.id ?? null);

  useEffect(() => {
    setActiveId(toc[0]?.id ?? null);
    if (toc.length === 0) return;

    const headings = toc
      .map((entry) => document.getElementById(entry.id))
      .filter((el): el is HTMLElement => el !== null);

    // A heading counts as "current" once it crosses the upper part of the viewport.
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible.length > 0) setActiveId(visible[0].target.id);
      },
      { rootMargin: "-70px 0px -65% 0px", threshold: 0 },
    );
    headings.forEach((h) => observer.observe(h));
    return () => observer.disconnect();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pageKey]);

  if (toc.length === 0) return null;

  return (
    <aside className="toc-aside" aria-label="On this page">
      <div className="sbhead">On this page</div>
      <ul className="toc">
        {toc.map((entry) => (
          <li key={entry.id} className={`l${entry.level}${entry.id === activeId ? " active" : ""}`}>
            <a
              href={`#${entry.id}`}
              aria-current={entry.id === activeId ? "location" : undefined}
              dangerouslySetInnerHTML={{ __html: entry.html }}
            />
          </li>
        ))}
      </ul>
    </aside>
  );
}
