import { useCallback, useEffect, useState } from "react";

const THEME_KEY = "ooad-theme";

/** Dark mode, persisted in localStorage and applied to <html class="dark">. */
export function useDarkMode(): [boolean, () => void] {
  const [dark, setDark] = useState<boolean>(() => localStorage.getItem(THEME_KEY) === "dark");

  useEffect(() => {
    document.documentElement.classList.toggle("dark", dark);
    localStorage.setItem(THEME_KEY, dark ? "dark" : "light");
  }, [dark]);

  const toggle = useCallback(() => setDark((d) => !d), []);
  return [dark, toggle];
}

/** A boolean kept in localStorage, e.g. whether a sidebar is collapsed. */
export function useStoredBoolean(key: string, initial = false): [boolean, () => void] {
  const [value, setValue] = useState<boolean>(() => {
    const stored = localStorage.getItem(key);
    return stored === null ? initial : stored === "1";
  });

  useEffect(() => {
    localStorage.setItem(key, value ? "1" : "0");
  }, [key, value]);

  const toggle = useCallback(() => setValue((v) => !v), []);
  return [value, toggle];
}
