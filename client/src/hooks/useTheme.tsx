import { useLayoutEffect, useState } from "react";

export default function useTheme() {
  const [theme, setTheme] = useState("dark");

  useLayoutEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
  }, [theme]);
  return { theme, setTheme };
}
