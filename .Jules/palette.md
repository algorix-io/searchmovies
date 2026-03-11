## 2024-05-18 - Added keyboard focus indicators
**Learning:** Adding consistent focus states (`outline-none focus:ring focus:ring-sky-600`) and ARIA labels to interactive elements makes the app fully accessible for keyboard navigation. By doing it directly with Tailwind classes it avoids complex CSS.
**Action:** Always add focus and hover states along with `outline-none focus:ring focus:ring-sky-600` for links and buttons to establish a reusable UX pattern. Add `aria-label` to form inputs where standard labels are not visible.
