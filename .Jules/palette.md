## 2025-02-18 - Missing empty states and clear focus indicators
**Learning:** The application lacked friendly empty states for zero-result searches, and interactive elements (like the search button and movie cards) were missing visible keyboard focus indicators (`focus-visible`).
**Action:** Always implement empty states with actionable paths (like 'Clear search') and consistently apply `outline-none focus-visible:ring focus-visible:ring-sky-600` to interactive elements to ensure keyboard accessibility.
