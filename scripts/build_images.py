#!/usr/bin/env python3
"""Generate the README images in assets/ from the skills on disk.

Writes:
  assets/hero.svg                     header image (1280 x 640, also the social preview)
  assets/categories/<category>.svg    one banner per category (1280 x 280)
  assets/examples/<example>.svg       preview cards for the worked examples (600 x 340)

Skill counts and names are read from skills/, so re-run this after adding a skill:
  python3 scripts/build_images.py
Standard library only.
"""
from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
ASSETS = ROOT / "assets"

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"
ORANGE = "#D97757"
INK = "#f3f6ff"
MUTED = "#b3bed8"
DIM = "#8b97b8"
PANEL = "#141b33"
LINE = "#2a3354"

# Display order, label, color, tagline, icon
CATEGORIES = [
    ("ai-ux-design", "AI UX & Design", "#ec4899",
     "Design how AI products and agents act, ask, fail, and explain themselves.", "ux"),
    ("ai-marketing-growth", "AI Marketing & Growth", "#06b6d4",
     "Position, launch, price, and grow AI products, and show up in AI answers.", "growth"),
    ("product-management", "Product Management", "#3b82f6",
     "Continuous discovery, customer research, prioritization, and product strategy.", "product"),
    ("strategic-management", "Strategic Management", "#a855f7",
     "Industry structure, positioning, market sizing, pricing, and go-to-market.", "strategy"),
    ("financial-analysis", "Financial Analysis", "#22c55e",
     "Valuation, capital allocation, runway, and SaaS unit economics.", "finance"),
    ("game-theory", "Game Theory", "#f59e0b",
     "Equilibria, negotiation, competitive response, and mechanism design.", "game"),
]
SHORT = {
    "ai-ux-design": "AI UX", "ai-marketing-growth": "AI Growth", "product-management": "Product",
    "strategic-management": "Strategy", "financial-analysis": "Finance", "game-theory": "Game Theory",
}


def skills_in(category: str) -> list[str]:
    return sorted(p.parent.name for p in (SKILLS / category).glob("*/SKILL.md"))


def text_width(text: str, size: float, weight: str = "regular", mono: bool = False) -> float:
    factor = 0.61 if mono else (0.6 if weight == "bold" else 0.54)
    return len(text) * size * factor


def t(x, y, text, size=16, fill=INK, weight=400, family=SANS, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{escape(text)}</text>')


def defs(extra: str = "") -> str:
    return f"""<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0a0e1a"/><stop offset="55%" stop-color="#10162c"/><stop offset="100%" stop-color="#0a0e1a"/>
    </linearGradient>
    <radialGradient id="glowA" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{ORANGE}" stop-opacity="0.30"/><stop offset="100%" stop-color="{ORANGE}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowB" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7c5cff" stop-opacity="0.22"/><stop offset="100%" stop-color="#7c5cff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="card" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1c2342"/><stop offset="100%" stop-color="#11172e"/>
    </linearGradient>
    <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ffffff"/><stop offset="65%" stop-color="#ffd9c8"/><stop offset="100%" stop-color="{ORANGE}"/>
    </linearGradient>
    <pattern id="dots" width="32" height="32" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="1" fill="#ffffff" opacity="0.06"/>
    </pattern>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="14"/><feOffset dy="12"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.45"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    {extra}
  </defs>"""


def background(w: int, h: int, glow_a=(160, 120, 340), glow_b=None) -> str:
    gb = glow_b or (w - 160, h - 60, 380)
    return (f'<rect width="{w}" height="{h}" fill="url(#bg)"/><rect width="{w}" height="{h}" fill="url(#dots)"/>'
            f'<circle cx="{glow_a[0]}" cy="{glow_a[1]}" r="{glow_a[2]}" fill="url(#glowA)"/>'
            f'<circle cx="{gb[0]}" cy="{gb[1]}" r="{gb[2]}" fill="url(#glowB)"/>')


def svg(w: int, h: int, label: str, body: str, extra_defs: str = "") -> str:
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" '
            f'role="img" aria-label="{escape(label)}">\n  {defs(extra_defs)}\n  {body}\n</svg>\n')


def window(w: int, h: int, title: str) -> str:
    """A card with a title bar; content is drawn by the caller in the same coordinates."""
    return (f'<rect width="{w}" height="{h}" rx="14" fill="url(#card)" stroke="{LINE}"/>'
            f'<path d="M14 0 H{w - 14} A14 14 0 0 1 {w} 14 V40 H0 V14 A14 14 0 0 1 14 0 Z" fill="#0d1226"/>'
            f'<circle cx="20" cy="20" r="5" fill="#ff5f57"/><circle cx="37" cy="20" r="5" fill="#febc2e"/>'
            f'<circle cx="54" cy="20" r="5" fill="#28c840"/>'
            + t(76, 25, title, 13, MUTED, 600, MONO))


# ---------------------------------------------------------------- example visuals

LEVELS = {"L5": ("Act silently", "#22c55e"), "L4": ("Act and report", "#14b8a6"),
          "L3": ("Act with approval", "#f59e0b"), "L2": ("Draft", "#f97316"), "L1": ("Suggest", "#ef4444")}
AUTONOMY = [("Look up order", "L5"), ("Draft reply", "L5"), ("Close ticket", "L4"),
            ("Change shipping address", "L3"), ("Refund up to $50", "L3"),
            ("Send reply", "L2"), ("Refund over $50", "L1")]
PRICING = [("Per seat", 38.2), ("Seat + cap", 53.0), ("Usage", 65.2),
           ("Credits", 58.4), ("Hybrid", 66.9), ("Outcome", 41.8)]
SHARE = [("Kestrel APM", 74.3), ("Driftwatch", 64.3), ("Signalyard", 44.2), ("Tracelight", 34.7)]


def autonomy_rows(x: float, y: float, w: float, rows=AUTONOMY, row_h=34) -> str:
    out = []
    for i, (action, level) in enumerate(rows):
        ry = y + i * row_h
        name, color = LEVELS[level]
        out.append(f'<rect x="{x}" y="{ry}" width="{w}" height="{row_h - 6}" rx="7" fill="#0f1529" stroke="{LINE}"/>')
        mid = ry + (row_h - 6) / 2 + 5
        out.append(t(x + 14, f"{mid:.1f}", action, 13.5, INK, 500))
        chip_w = text_width(f"{level}  {name}", 12, "bold") + 22
        cx = x + w - chip_w - 8
        out.append(f'<rect x="{cx}" y="{ry + 5}" width="{chip_w}" height="{row_h - 16}" rx="9" fill="{color}" fill-opacity="0.16" stroke="{color}" stroke-opacity="0.6"/>')
        out.append(t(f"{cx + 11:.1f}", f"{mid - 0.5:.1f}", f"{level}  {name}", 12, color, 700))
    return "".join(out)


def pricing_bars(x: float, y: float, w: float, h: float) -> str:
    out, n = [], len(PRICING)
    gap = 14
    bw = (w - gap * (n - 1)) / n
    scale = h / 80.0
    base = y + h
    for i, (label, value) in enumerate(PRICING):
        bx = x + i * (bw + gap)
        bh = value * scale
        best = label == "Hybrid"
        color = "#22c55e" if best else "#3b4670"
        out.append(f'<rect x="{bx:.1f}" y="{base - bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="5" fill="{color}"/>')
        out.append(t(f"{bx + bw / 2:.1f}", f"{base - bh - 8:.1f}", f"{value:.0f}%", 12.5, INK if best else MUTED, 700, anchor="middle"))
        out.append(t(f"{bx + bw / 2:.1f}", base + 18, label, 11.5, MUTED if not best else INK, 600, anchor="middle"))
    floor_y = base - 50 * scale
    out.append(f'<line x1="{x - 6}" y1="{floor_y:.1f}" x2="{x + w + 6}" y2="{floor_y:.1f}" stroke="{ORANGE}" stroke-width="1.5" stroke-dasharray="5 5"/>')
    out.append(f'<line x1="{x + w - 118}" y1="{y - 18}" x2="{x + w - 96}" y2="{y - 18}" stroke="{ORANGE}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    out.append(t(x + w + 6, y - 14, "50% margin floor", 11, ORANGE, 700, anchor="end"))
    return "".join(out)


def share_bars(x: float, y: float, w: float, row_h: float = 36) -> str:
    out = []
    label_w = 104
    for i, (brand, value) in enumerate(SHARE):
        ry = y + i * row_h
        you = brand == "Tracelight"
        color = "#06b6d4" if you else "#3b4670"
        out.append(t(x, ry + 15, brand, 13, INK if you else MUTED, 700 if you else 500))
        bar_w = (w - label_w - 52) * value / 100
        out.append(f'<rect x="{x + label_w}" y="{ry + 3}" width="{w - label_w - 52}" height="16" rx="8" fill="#0f1529"/>')
        out.append(f'<rect x="{x + label_w}" y="{ry + 3}" width="{bar_w:.1f}" height="16" rx="8" fill="{color}"/>')
        out.append(t(x + w, ry + 16, f"{value:.1f}%", 13, INK if you else MUTED, 700, anchor="end"))
    return "".join(out)


# ---------------------------------------------------------------- hero

def build_hero(counts: dict[str, int]) -> str:
    total = sum(counts.values())
    w, h = 1280, 640
    b = [background(w, h, (180, 150, 380), (1120, 560, 420))]

    # Left column
    pill = "BUILT FOR CLAUDE CODE  ·  OPEN SOURCE  ·  MIT"
    pw = text_width(pill, 12, "bold") + 64
    b.append(f'<rect x="80" y="70" width="{pw:.0f}" height="32" rx="16" fill="#161c30" stroke="{ORANGE}" stroke-opacity="0.55"/>')
    b.append(f'<circle cx="98" cy="86" r="4" fill="{ORANGE}"/>')
    b.append(t(112, 90.5, pill, 12, ORANGE, 700, extra='letter-spacing="1.2"'))
    b.append(t(78, 182, "Claude Code Skills", 66, "url(#title)", 800, extra='letter-spacing="-2"'))
    b.append(t(80, 232, f"{total} expert workflows.", 26, INK, 700))
    b.append(t(80, 266, "Each one ends in a deliverable.", 26, INK, 400))
    b.append(t(80, 306, "Autonomy maps, pricing models, AI search audits, valuations,", 17, MUTED))
    b.append(t(80, 330, "roadmaps, and negotiation plans, run end to end by Claude.", 17, MUTED))

    # Install command
    b.append(f'<rect x="80" y="362" width="500" height="54" rx="12" fill="#0b1022" stroke="{LINE}"/>')
    b.append(t(102, 395, "$", 16, DIM, 700, MONO))
    b.append(t(122, 395, "./install.sh", 16, INK, 600, MONO))
    b.append(t(560, 395, f"✓ {total} skills installed", 15, "#22c55e", 600, MONO, anchor="end"))

    # Category chips, two rows of three so they stay clear of the cards
    x, y = 80, 452
    for i, (cat, _, color, _, _) in enumerate(CATEGORIES):
        if i == 3:
            x, y = 80, 502
        label = f"{SHORT[cat]}  {counts[cat]}"
        cw = text_width(label, 14, "bold") + 40
        b.append(f'<rect x="{x:.0f}" y="{y}" width="{cw:.0f}" height="38" rx="19" fill="{color}" fill-opacity="0.10" stroke="{color}" stroke-opacity="0.55"/>')
        b.append(f'<circle cx="{x + 18:.0f}" cy="{y + 19}" r="4.5" fill="{color}"/>')
        b.append(t(f"{x + 30:.0f}", y + 24, SHORT[cat], 14, INK, 700))
        b.append(t(f"{x + 30 + text_width(SHORT[cat] + '  ', 14, 'bold'):.0f}", y + 24, str(counts[cat]), 14, color, 800))
        x += cw + 12
    b.append(t(80, 588, "github.com/varunk130/claude-code-skills", 14, DIM, 600, MONO))

    # Right column: stacked deliverables
    b.append(f'<g transform="translate(790 70) rotate(5 210 140)" filter="url(#shadow)">'
             + window(420, 230, "ai-search-visibility-optimizer")
             + t(22, 70, "Share of answer across AI assistants", 13, MUTED, 600)
             + share_bars(22, 86, 376, 34) + "</g>")
    b.append(f'<g transform="translate(700 150) rotate(-3 210 150)" filter="url(#shadow)">'
             + window(430, 250, "ai-pricing-margin-modeler")
             + t(22, 70, "Blended gross margin by pricing model", 13, MUTED, 600)
             + pricing_bars(30, 92, 370, 120) + "</g>")
    front_rows = AUTONOMY[:1] + AUTONOMY[2:]
    b.append(f'<g transform="translate(742 268)" filter="url(#shadow)">'
             + window(460, 300, "agent-autonomy-level-mapper")
             + t(22, 68, "Support agent: what may it do on its own?", 14, INK, 700)
             + autonomy_rows(18, 84, 424, front_rows, 35) + "</g>")

    return svg(w, h, f"Claude Code Skills: {total} expert workflows across {len(CATEGORIES)} categories, "
               "each ending in a deliverable.", "\n  ".join(b))


# ---------------------------------------------------------------- category banners

def icon(kind: str, color: str) -> str:
    s = f'stroke="{color}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    f = f'fill="{color}"'
    if kind == "ux":
        return (f'<rect x="22" y="28" width="76" height="56" rx="8" {s}/><path d="M22 42 H98" {s}/>'
                f'<path d="M60 58 L60 92 L69 84 L76 98 L82 95 L75 81 L87 80 Z" {f}/>'
                f'<path d="M92 14 l3 8 8 3 -8 3 -3 8 -3 -8 -8 -3 8 -3 z" {f}/>')
    if kind == "growth":
        return (f'<path d="M20 96 H100" {s}/><path d="M24 84 L48 62 L64 72 L94 36" {s}/>'
                f'<path d="M78 34 H96 V52" {s}/><circle cx="48" cy="62" r="5" {f}/><circle cx="64" cy="72" r="5" {f}/>')
    if kind == "product":
        return (f'<path d="M60 20 L100 40 L60 60 L20 40 Z" {s}/><path d="M20 60 L60 80 L100 60" {s}/>'
                f'<path d="M20 80 L60 100 L100 80" {s}/>')
    if kind == "strategy":
        return (f'<circle cx="60" cy="60" r="38" {s}/><circle cx="60" cy="60" r="22" {s}/>'
                f'<circle cx="60" cy="60" r="7" {f}/><path d="M84 36 L102 18 M92 18 H102 V28" {s}/>')
    if kind == "finance":
        return (f'<path d="M18 100 H102" {s}/><rect x="26" y="66" width="16" height="30" rx="3" {f}/>'
                f'<rect x="52" y="46" width="16" height="50" rx="3" {f}/><rect x="78" y="26" width="16" height="70" rx="3" {f}/>')
    if kind == "game":
        return (f'<rect x="20" y="20" width="80" height="80" rx="8" {s}/><path d="M60 20 V100 M20 60 H100" {s}/>'
                f'<circle cx="40" cy="40" r="7" {f}/><circle cx="80" cy="80" r="7" {f}/>'
                f'<path d="M74 34 L86 46 M86 34 L74 46" {s}/>')
    return ""


def build_banner(cat: str, label: str, color: str, tagline: str, kind: str, names: list[str]) -> str:
    w, h = 1280, 280
    b = [background(w, h, (150, 140, 260), (1150, 260, 300))]
    b.append(f'<radialGradient id="catglow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="{color}" stop-opacity="0.35"/>'
             f'<stop offset="100%" stop-color="{color}" stop-opacity="0"/></radialGradient>')
    b.append('<circle cx="140" cy="140" r="130" fill="url(#catglow)"/>')
    b.append(f'<g transform="translate(80 80)"><rect width="120" height="120" rx="26" fill="#121933" stroke="{color}" stroke-opacity="0.6" stroke-width="1.5"/>'
             f'{icon(kind, color)}</g>')
    b.append(t(236, 100, f"CATEGORY  ·  {len(names)} SKILLS", 13, color, 800, extra='letter-spacing="1.6"'))
    b.append(t(234, 150, label, 46, INK, 800, extra='letter-spacing="-1"'))
    b.append(t(236, 186, tagline, 16, MUTED))
    b.append(t(236, 214, "claude-code-skills", 13, DIM, 600, MONO))

    # Skill list panel
    line_h = 20 if len(names) > 7 else 24
    panel_h = 32 + line_h * len(names)
    py = (h - panel_h) / 2
    b.append(f'<g transform="translate(800 {py:.0f})"><rect width="400" height="{panel_h}" rx="14" fill="#0b1022" fill-opacity="0.85" stroke="{LINE}"/>')
    for i, name in enumerate(names):
        y = 26 + i * line_h
        b.append(t(22, y + 2, "/", 13, color, 700, MONO) + t(34, y + 2, name, 13, INK, 500, MONO))
    b.append("</g>")
    return svg(w, h, f"{label}: {len(names)} Claude Code skills. {tagline}", "\n  ".join(b))


# ---------------------------------------------------------------- example cards

def build_example(kind: str) -> tuple[str, str]:
    w, h = 600, 340
    b = [background(w, h, (80, 40, 220), (560, 320, 240))]
    if kind == "autonomy":
        name, title, sub = "agent-autonomy-level-mapper", "Support agent autonomy map", "10 actions scored on stakes, reversibility, and accuracy"
        body = autonomy_rows(28, 112, 544, AUTONOMY[:1] + AUTONOMY[2:], 36)
    elif kind == "pricing":
        name, title, sub = "ai-pricing-margin-modeler", "Writing assistant pricing model", "Blended gross margin for six packaging options"
        body = pricing_bars(44, 128, 500, 150)
    else:
        name, title, sub = "ai-search-visibility-optimizer", "Developer tool AI search audit", "Share of answer across four AI assistants (illustrative)"
        body = share_bars(36, 126, 528, 46)
    b.append(t(28, 44, name, 13, ORANGE, 700, MONO))
    b.append(t(28, 74, title, 22, INK, 800))
    b.append(t(28, 96 if kind != "autonomy" else 94, sub, 13.5, MUTED))
    b.append(body)
    return name, svg(w, h, f"{title}: worked example of the {name} skill", "\n  ".join(b))


def main() -> None:
    counts = {cat: len(skills_in(cat)) for cat, *_ in CATEGORIES}
    (ASSETS / "categories").mkdir(parents=True, exist_ok=True)
    (ASSETS / "examples").mkdir(parents=True, exist_ok=True)
    (ASSETS / "hero.svg").write_text(build_hero(counts), encoding="utf-8")
    for cat, label, color, tagline, kind in CATEGORIES:
        (ASSETS / "categories" / f"{cat}.svg").write_text(
            build_banner(cat, label, color, tagline, kind, skills_in(cat)), encoding="utf-8")
    for kind in ("autonomy", "pricing", "search"):
        name, content = build_example(kind)
        (ASSETS / "examples" / f"{name}.svg").write_text(content, encoding="utf-8")
    print(f"Wrote hero, {len(CATEGORIES)} category banners, and 3 example cards to {ASSETS}")


if __name__ == "__main__":
    main()
