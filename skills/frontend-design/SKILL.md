---
name: frontend-design
description: Frontend design patterns and UI conventions for building production-grade interfaces
---

When building frontend interfaces:

## Design Quality
- Create distinctive, polished UI — avoid generic AI aesthetics
- Use consistent spacing, typography, and color systems
- Ensure visual hierarchy guides the user's eye
- Design mobile-first, then scale up to larger viewports

## Component Patterns
- Build reusable, composable components
- Keep components focused on a single responsibility
- Use consistent naming conventions for components and props
- Separate presentational components from logic/data-fetching

## Styling Conventions
- Use a utility-first approach (e.g., Tailwind CSS) or CSS modules for scoping
- Maintain a consistent design token system (colors, spacing, font sizes)
- Avoid inline styles except for truly dynamic values
- Support dark mode where applicable

## Accessibility
- Use semantic HTML elements (nav, main, section, button — not div for everything)
- Include proper ARIA labels and roles where semantic HTML isn't sufficient
- Ensure keyboard navigation works for all interactive elements
- Maintain sufficient color contrast ratios (WCAG AA minimum)

## Performance
- Lazy-load heavy components and images
- Minimize re-renders with proper state management
- Use optimistic UI updates where appropriate
- Keep bundle size in check — avoid unnecessary dependencies

## Responsive Design
- Use fluid layouts with relative units (rem, %, vh/vw)
- Define clear breakpoints and test at each
- Ensure touch targets are at least 44x44px on mobile
- Handle text overflow and long content gracefully
