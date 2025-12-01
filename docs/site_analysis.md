# Stack Overflow Replica — Site Analysis

## Profile
- **Name:** Stack Overflow
- **URL:** https://stackoverflow.com/
- **Type:** Programming Q&A community
- **Layout width:** ~1200px fixed center with gutters
- **Grid:** 2-column main area (content + right sidebar) with stacked cards

## Color Palette (approximated from screenshot)
| Token | Hex | Usage |
| --- | --- | --- |
| `--so-sunrise` | #f48024 | CTA buttons, highlights
| `--so-blue` | #0077cc | Links, hover states
| `--so-navy` | #2d2d2d | Header text, nav
| `--so-body` | #3c4146 | Primary body text
| `--so-muted` | #6a737c | Secondary text
| `--so-border` | #d6d9dc | Card/divider borders
| `--so-bg` | #f8f9f9 | Page background
| `--white` | #ffffff | Cards, header background

## Typography
- **Primary UI Font:** "Roboto", "Segoe UI", system-ui, sans-serif
- **Headings:** 18–24px semi-bold
- **Body copy:** 13px–14px regular
- **Meta text:** 12px uppercase/semibold for badges

## Core Components
1. **Top Utility Bar** — Logo, navigation tabs (Interesting, Featured, Hot, Week, Month), Ask Question CTA, search + profile summary.
2. **Left Sticky Nav** — Questions, Tags, Users, Jobs, etc.
3. **Main Content Feed** — Vertical list of question rows: stats column, summary column, tags, metadata, badges.
4. **Right Sidebar** — Overflow Blog promoting posts, Collections, Hot Network Questions list, etc.
5. **Pagination Footer** — Numbered pager with current page highlighted, site footer with network links.

## Layout Specs
- **Header height:** ~72px (two-row structure: top nav + filter tabs)
- **Content max-width:** 1264px centered
- **Left nav width:** 164px fixed
- **Main feed width:** ~728px
- **Sidebar width:** ~300px
- **Row spacing:** 16px vertical rhythm, 24px between columns

## Interaction Notes
- Hover states lighten backgrounds and underline links.
- Tags use pill styling (#e1ecf4 background, #39739d text).
- Reusable badges for question status (e.g., "Best practices", "Featured").

## Injection Targets
```yaml
injection_targets:
  - name: "question_feed"
    selector: "#question-list"
    description: "Primary list where question rows are appended"
  - name: "sidebar"
    selector: "#sidebar-widgets"
    description: "Right rail widgets"
```
