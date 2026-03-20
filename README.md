# Claude Code Custom Skills

A curated collection of custom skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Anthropic's official CLI for Claude. These skills extend Claude's capabilities with specialized workflows for product management, engineering, data analysis, financial modeling, and more.

## What Are Skills?

Skills are reusable prompt templates that give Claude Code domain-specific knowledge and structured workflows. Drop them into your `~/.claude/skills/` directory and invoke them with slash commands or natural language.

## Skills Overview

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
| [market-sizing](skills/market-sizing/SKILL.md) | TAM/SAM/SOM calculator using both top-down and bottom-up approaches with assumption tracking |
| [pdf-processing](skills/pdf-processing/SKILL.md) | PDF text extraction, form filling, and document merging |
| [pr-summary](skills/pr-summary/SKILL.md) | Pull request change summarization with diff analysis and comment review |
| [pricing-strategy-analyzer](skills/pricing-strategy-analyzer/SKILL.md) | Pricing strategy analysis with competitive positioning, packaging, and revenue modeling |

## Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/varunk130/claude-code-skills.git
   ```

2. Copy the skills you want into your Claude Code skills directory:
   ```bash
   cp -r claude-code-skills/skills/ai-decision-engine ~/.claude/skills/
   ```

   Or copy all of them:
   ```bash
   cp -r claude-code-skills/skills/* ~/.claude/skills/
   ```

3. Restart Claude Code. The skills will be available via slash commands or natural language triggers.

## Skill Categories

### Product Management & Strategy
- **ai-decision-engine** — Multi-framework strategic decision-making
- **ai-product-strategy** — AI opportunity identification and roadmap planning
- **go-to-market-strategy** — Launch planning and GTM execution
- **market-sizing** — TAM/SAM/SOM analysis
- **pricing-strategy-analyzer** — Pricing optimization and competitive analysis

### Financial Modeling
- **ai-agent-financial-analyst** — Unit economics, ROI, build vs. buy, and revenue forecasting

### Communication
- **ai-stakeholder-translator** — Multi-audience communication from a single source

### Engineering & Development
- **api-conventions** — API design standards
- **codebase-visualizer** — Project structure visualization
- **deploy** — Deployment workflow
- **explain-code** — Code explanation with visuals
- **fidelity-scorecard** — Design-to-code accuracy scoring
- **fix-issue** — Issue resolution workflow
- **frontend-design** — UI/UX development patterns
- **pr-summary** — Pull request summarization

### Data & Analysis
- **data-scientist-analysis** — SQL, metrics, and analytics conventions
- **deep-research** — Codebase and topic research

### Document Processing
- **pdf-processing** — PDF manipulation and extraction

## Contributing

Feel free to fork this repo and add your own skills. Each skill should have:
- A `SKILL.md` file with frontmatter (`name`, `description`) and the skill prompt
- Any supporting scripts in a `scripts/` subdirectory

## License

MIT
