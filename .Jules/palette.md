## 2025-03-05 - Explicit Focus Rings in Dark Mode
**Learning:** Default browser focus rings are often nearly invisible against this app's dark background (`bg-slate-950`). Users relying on keyboard navigation easily lose their place because elements like links, buttons, and cards do not have clear visual indicators of focus.
**Action:** Always manually add explicit focus ring classes (`outline-none focus:ring focus:ring-sky-600`) along with hover states (`transition`) to all interactive elements to ensure high visibility and accessibility in dark mode themes.
