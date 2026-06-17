## 2025-06-17 - Empty States & Keyboard Focus
**Learning:** Native `focus:ring` applies to mouse clicks as well which can be noisy; using `focus-visible:ring` provides keyboard accessibility without negatively impacting the mouse user experience. Empty states without clear calls-to-action (like "Clear Search") lead to dead-ends.
**Action:** Consistently use `focus-visible` for focus states on interactive elements like cards and buttons. Always provide a clear recovery path in empty states.
