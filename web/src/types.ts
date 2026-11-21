/** Shape of web/src/data/lessons.json, written by `python tools/ooad.py export`. */

export interface TocEntry {
  level: 2 | 3;
  id: string;
  html: string;
}

export interface Lesson {
  slug: string;
  number: string;
  title: string;
  chapter: string;
  syllabus: string;
  minutes: number;
  html: string;
  toc: TocEntry[];
}

export interface Chapter {
  title: string;
  lessons: string[];
}

export interface CourseData {
  courseTitle: string;
  intro: {
    beforeRoadmap: string;
    afterRoadmap: string;
    toc: TocEntry[];
  };
  chapters: Chapter[];
  lessons: Lesson[];
}
