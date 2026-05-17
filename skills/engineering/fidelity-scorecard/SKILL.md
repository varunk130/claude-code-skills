---
name: fidelity-scorecard
description: "3-pass Design-to-Code Fidelity Scorecard. Extracts Figma tokens via MCP, generates React/Tailwind component, then scores fidelity with Playwright."
---

# Design-to-Code Fidelity Scorecard

Run this when asked for a "fidelity check", "design scorecard", or "design-to-code comparison".

## Prerequisites

- Dev server running: `npm run dev` (localhost:5173)
- Playwright installed: `npx playwright install chromium`

## PASS 1: Extract Design Tokens from Figma

1. Ask for the Figma file URL (extract fileKey and nodeId)
2. Call `get_variable_defs` with fileKey and nodeId to load design variables
3. Call `get_design_context` with fileKey and nodeId for the full component tree
4. Extract ALL tokens: colors, typography, spacing, border-radius, shadows, opacity, dimensions
5. Write to `src/data/figma-tokens.json`
6. Report: "Pass 1 complete. Extracted N tokens from [frame name]."

## PASS 2: Generate React Component

1. Read tokens from `src/data/figma-tokens.json`
2. Generate a React component using EXACT token values (not approximate Tailwind classes)
3. Save to `src/components/generated/[ComponentName].jsx`
4. Update `src/pages/Preview.jsx` to import and render the component
5. Ensure dev server is running
6. Report: "Pass 2 complete. Component at [path]. Preview: http://localhost:5173/preview"

## PASS 3: Score Fidelity

1. Run: `node scripts/extract-styles.js` (Playwright extracts computed CSS)
2. Run: `node scripts/compare-fidelity.js` (compares against tokens, writes scorecard)
3. Read `src/data/scorecard-results.json` and present results as a table:

| Dimension | Figma | Rendered | Match |
|-----------|-------|----------|-------|

4. Show PM decision: ACCEPT (>=95%), REVIEW (80-94%), or FIX (<80%)
5. List specific fix recommendations
6. If REVIEW or FIX, offer to re-run Pass 2 with corrections
