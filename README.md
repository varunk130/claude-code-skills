# Claude Code Custom Skills

A curated collection of custom skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Anthropic's official CLI for Claude. These skills extend Claude's capabilities with specialized, reusable workflows for product management, engineering, data analysis, financial modeling, GTM, design, and more.

## What Are Skills?

Skills are reusable prompt templates that give Claude Code domain-specific knowledge and structured workflows. Drop them into your `~/.claude/skills/` directory (or a project-local `.claude/skills/` folder) and invoke them with slash commands or natural language.

[![Built with Claude Code](https://img.shields.io/badge/Built_with-Claude_Code-D97757?logo=anthropic&logoColor=white)](https://claude.ai/code)

---

## Custom Skills

These are custom-built skills for specific workflows.

| Skill | Description |
|-------|-------------|
| [ai-agent-financial-analyst](skills/ai-agent-financial-analyst/SKILL.md) | SaaS financial modeling engine for unit economics, ROI calculators, pricing scenarios, and revenue projections |
| [ai-decision-engine](skills/ai-decision-engine/SKILL.md) | Strategic product decision engine with multi-framework analysis and context-aware recommendations |
| [ai-product-strategy](skills/ai-product-strategy/SKILL.md) | AI opportunity assessment with build/buy/partner analysis and data moat evaluation |
| [ai-stakeholder-translator](skills/ai-stakeholder-translator/SKILL.md) | Generates 5 tailored communications from one product update for engineering, executives, board, customers, and sales |
| [api-conventions](skills/api-conventions/SKILL.md) | RESTful API design patterns and consistent error handling conventions |
| [codebase-visualizer](skills/codebase-visualizer/SKILL.md) | Interactive HTML tree visualization of project file structure with file sizes and type colors |
| [data-scientist-analysis](skills/data-scientist-analysis/SKILL.md) | SQL best practices, SaaS metrics definitions, and structured data analysis conventions |
| [deep-research](skills/deep-research/SKILL.md) | Thorough topic research using codebase search and file analysis tools |
| [deploy](skills/deploy/SKILL.md) | Application deployment workflow with test, build, and push steps |
| [explain-code](skills/explain-code/SKILL.md) | Code explanation with analogies, ASCII diagrams, step-by-step walkthroughs, and gotcha highlights |
| [fidelity-scorecard](skills/fidelity-scorecard/SKILL.md) | 3-pass design-to-code fidelity scoring using Figma tokens extraction and Playwright comparison |
| [fix-issue](skills/fix-issue/SKILL.md) | Structured GitHub issue fixing workflow with tests and commits |
| [frontend-design](skills/frontend-design/SKILL.md) | Frontend design patterns for production-grade, accessible, and responsive interfaces |
| [go-to-market-strategy](skills/go-to-market-strategy/SKILL.md) | Complete GTM planning with channels, messaging matrix, launch timeline, and success metrics |
| [gtm-engineering](skills/gtm-engineering/SKILL.md) | Designs the GTM data infrastructure — lead scoring, routing, lifecycle automation, attribution, and reverse ETL contracts |
| [market-sizing](skills/market-sizing/SKILL.md) | TAM/SAM/SOM calculator using both top-down and bottom-up approaches with assumption tracking |
| [pdf-processing](skills/pdf-processing/SKILL.md) | PDF text extraction, form filling, and document merging |
| [pr-summary](skills/pr-summary/SKILL.md) | Pull request change summarization with diff analysis and comment review |
| [pricing-strategy-analyzer](skills/pricing-strategy-analyzer/SKILL.md) | Pricing strategy analysis with competitive positioning, packaging, and revenue modeling |

---

## Plugin Skills

Skills from installed Claude Code plugins. These are managed by the plugin system and provide additional capabilities.

### Document Skills (anthropic-agent-skills)

| Skill | Description |
|-------|-------------|
| [algorithmic-art](plugin-skills/document-skills/algorithmic-art/SKILL.md) | Create generative art using p5.js with seeded randomness and interactive parameter exploration |
| [brand-guidelines](plugin-skills/document-skills/brand-guidelines/SKILL.md) | Apply Anthropic brand colors and typography to artifacts |
| [canvas-design](plugin-skills/document-skills/canvas-design/SKILL.md) | Create museum-quality visual art as .pdf or .png with design philosophy |
| [doc-coauthoring](plugin-skills/document-skills/doc-coauthoring/SKILL.md) | Structured 3-stage workflow for co-authoring documentation |
| [docx](plugin-skills/document-skills/docx/SKILL.md) | Create, read, edit Word documents with tracked changes, comments, and formatting |
| [internal-comms](plugin-skills/document-skills/internal-comms/SKILL.md) | Write internal communications (3P updates, newsletters, FAQs, status reports) |
| [mcp-builder](plugin-skills/document-skills/mcp-builder/SKILL.md) | Guide for creating MCP servers to integrate LLMs with external services |
| [pdf](plugin-skills/document-skills/pdf/SKILL.md) | Full PDF processing: read, merge, split, rotate, watermark, OCR, encrypt, fill forms |
| [pptx](plugin-skills/document-skills/pptx/SKILL.md) | Create, read, edit PowerPoint presentations with design guidelines and visual QA |
| [skill-creator](plugin-skills/document-skills/skill-creator/SKILL.md) | Guide for creating effective Claude Code skills with progressive disclosure |
| [slack-gif-creator](plugin-skills/document-skills/slack-gif-creator/SKILL.md) | Create animated GIFs optimized for Slack with PIL and easing functions |
| [theme-factory](plugin-skills/document-skills/theme-factory/SKILL.md) | 10 pre-set themes with colors/fonts for styling artifacts, plus custom theme generation |
| [web-artifacts-builder](plugin-skills/document-skills/web-artifacts-builder/SKILL.md) | Build multi-component HTML artifacts with React, Tailwind CSS, and shadcn/ui |
| [webapp-testing](plugin-skills/document-skills/webapp-testing/SKILL.md) | Test local web applications using Playwright with server lifecycle management |
| [xlsx](plugin-skills/document-skills/xlsx/SKILL.md) | Create, read, edit spreadsheets with formulas, formatting, and financial modeling conventions |

### Figma Plugin

| Skill | Description |
|-------|-------------|
| [code-connect-components](plugin-skills/figma/code-connect-components/SKILL.md) | Connect Figma design components to code implementations using Code Connect |
| [create-design-system-rules](plugin-skills/figma/create-design-system-rules/SKILL.md) | Generate project-specific design system rules for Figma-to-code workflows |
| [implement-design](plugin-skills/figma/implement-design/SKILL.md) | Translate Figma designs into production-ready code with 1:1 visual fidelity |

### Notion Plugin

| Skill | Description |
|-------|-------------|
| [knowledge-capture](plugin-skills/notion/knowledge-capture/SKILL.md) | Transform conversations into structured Notion documentation with proper organization |
| [meeting-intelligence](plugin-skills/notion/meeting-intelligence/SKILL.md) | Prepare meeting materials with Notion context and Claude research enrichment |
| [research-documentation](plugin-skills/notion/research-documentation/SKILL.md) | Search Notion workspace and synthesize findings into comprehensive research docs |
| [spec-to-implementation](plugin-skills/notion/spec-to-implementation/SKILL.md) | Turn specs into concrete Notion tasks with implementation plans and progress tracking |

### Stripe Plugin

| Skill | Description |
|-------|-------------|
| [stripe-best-practices](plugin-skills/stripe/stripe-best-practices/SKILL.md) | Best practices for Stripe integrations: payments, checkout, subscriptions, Connect platforms |

---

## Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/varunk130/claude-code-skills.git
   ```

2. Copy the custom skills you want into your Claude Code skills directory:
   ```bash
   cp -r claude-code-skills/skills/ai-decision-engine ~/.claude/skills/
   ```

   Or copy all custom skills:
   ```bash
   cp -r claude-code-skills/skills/* ~/.claude/skills/
   ```

3. Restart Claude Code. The skills will be available via slash commands or natural language triggers.

> **Note:** Plugin skills (in `plugin-skills/`) are managed by the Claude Code plugin system. They are included here for reference and documentation purposes.

## Skill Categories

### Product Management & Strategy
- **ai-decision-engine** -- Multi-framework strategic decision-making
- **ai-product-strategy** -- AI opportunity identification and roadmap planning
- **go-to-market-strategy** -- Launch planning and GTM execution
- **market-sizing** -- TAM/SAM/SOM analysis
- **pricing-strategy-analyzer** -- Pricing optimization and competitive analysis

### Financial Modeling
- **ai-agent-financial-analyst** -- Unit economics, ROI, build vs. buy, and revenue forecasting

### Communication
- **ai-stakeholder-translator** -- Multi-audience communication from a single source

### Engineering & Development
- **api-conventions** -- API design standards
- **codebase-visualizer** -- Project structure visualization
- **deploy** -- Deployment workflow
- **explain-code** -- Code explanation with visuals
- **fidelity-scorecard** -- Design-to-code accuracy scoring
- **fix-issue** -- Issue resolution workflow
- **frontend-design** -- UI/UX development patterns
- **pr-summary** -- Pull request summarization

### Data & Analysis
- **data-scientist-analysis** -- SQL, metrics, and analytics conventions
- **deep-research** -- Codebase and topic research

### Document Processing
- **pdf-processing** -- PDF manipulation and extraction
- **docx** -- Word document creation and editing (plugin)
- **pptx** -- PowerPoint presentation creation and editing (plugin)
- **xlsx** -- Excel spreadsheet creation and editing (plugin)
- **pdf** -- Advanced PDF processing with OCR (plugin)

### Design & Figma
- **code-connect-components** -- Figma-to-code component mapping (plugin)
- **create-design-system-rules** -- Design system rule generation (plugin)
- **implement-design** -- Figma design implementation (plugin)

### Notion Integration
- **knowledge-capture** -- Conversation to Notion documentation (plugin)
- **meeting-intelligence** -- Meeting preparation with Notion context (plugin)
- **research-documentation** -- Cross-workspace research synthesis (plugin)
- **spec-to-implementation** -- Spec to task breakdown (plugin)

### Payments
- **stripe-best-practices** -- Stripe integration guidance (plugin)

## Contributing

Feel free to fork this repo and add your own skills. Each skill should have:
- A `SKILL.md` file with frontmatter (`name`, `description`) and the skill prompt
- Any supporting scripts in a `scripts/` subdirectory
- A short usage example in the description so users know when the skill fires

Pull requests are welcome — please keep one skill per PR for easier review.

## License

MIT

---

<sub>Built by [Varun Kulkarni](https://github.com/varunk130) — part of a portfolio of AI agent systems for product teams.</sub>

