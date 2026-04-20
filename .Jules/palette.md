## 2024-05-24 - Consistent Focus Indicators
**Learning:** Interactive elements such as `<button>` and `<a>` must consistently use Tailwind's `outline-none focus:ring focus:ring-sky-600` classes to clearly indicate keyboard focus. This app had many missing focus indicators out-of-the-box.
**Action:** When adding new interactive components or auditing existing ones, automatically apply `outline-none focus:ring focus:ring-[color-value]` and pair it with a visible hover state so keyboard users can navigate confidently.
