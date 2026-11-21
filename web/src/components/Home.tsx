import { Link } from "react-router-dom";
import { course, lessonPath } from "../course";
import type { Lesson } from "../types";

const isLesson = (l: Lesson | undefined): l is Lesson => l !== undefined;

/** Course roadmap: one card per chapter, each lesson with its reading time. */
function Roadmap() {
  return (
    <div className="roadmap">
      {course.chapters
        .filter((c) => c.title !== "Start Here")
        .map((chapter) => {
          const lessons = chapter.lessons
            .map((slug) => course.lessons.find((l) => l.slug === slug))
            .filter(isLesson);
          const total = lessons.reduce((sum, l) => sum + l.minutes, 0);
          return (
            <div className="chapter-card" key={chapter.title}>
              <div className="chhead">
                <span>{chapter.title}</span>
                <span className="rt">
                  {lessons.length} lessons · ~{total} min
                </span>
              </div>
              <ul>
                {lessons.map((l) => (
                  <li key={l.slug}>
                    <Link to={lessonPath(l.slug)}>
                      <span className="ln">{l.number}</span> {l.title}
                    </Link>
                    <span className="rt">{l.minutes} min</span>
                  </li>
                ))}
              </ul>
            </div>
          );
        })}
    </div>
  );
}

export function Home() {
  const { beforeRoadmap, afterRoadmap } = course.intro;
  return (
    <>
      <div dangerouslySetInnerHTML={{ __html: beforeRoadmap }} />
      <h2>Course Roadmap</h2>
      <Roadmap />
      <div dangerouslySetInnerHTML={{ __html: afterRoadmap }} />
    </>
  );
}
