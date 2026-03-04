## 2025-05-18 - Tailwind Preflight and Keyboard Accessibility
**Learning:** Tailwind CSS preflight removes all default browser outlines. This makes interactive elements completely invisible to keyboard navigation (tabbing) unless explicit focus states are added. This app heavily relies on custom anchors and buttons that were missing these explicit states.
**Action:** Always include explicit focus states (e.g., `outline-none focus:ring focus:ring-sky-600`) and appropriate hover states for all interactive elements (links, buttons) when building or modifying components in this application.
