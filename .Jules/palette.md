## 2023-10-24 - Empty States with Reset Paths
**Learning:** Empty states without explicit alternative paths or reset actions leave users stranded. A static text message is insufficient for good UX.
**Action:** Always provide an explicit, keyboard-accessible reset or alternative path (e.g., a "Clear search" button) in empty states, utilizing standard focus indicators (`focus-visible:ring`).