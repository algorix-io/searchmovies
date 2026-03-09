## 2025-02-14 - Keyboard Accessibility & Focus States
**Learning:** Found that many interactive elements (buttons, links, movie cards) across the application were lacking clear focus indicators for keyboard users. While hover states existed for some, `focus:ring` was missing, making keyboard navigation difficult.
**Action:** Standardize on `outline-none focus:ring focus:ring-sky-600` with appropriate rounded corners for all interactive elements to ensure clear visible focus indicators that match the app's brand color.
