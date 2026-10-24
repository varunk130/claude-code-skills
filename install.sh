#!/usr/bin/env bash
# Install skills from this library into Claude Code.
#
# Claude Code discovers skills one level deep (<skills-dir>/<skill-name>/SKILL.md),
# so this script flattens the category folders when copying.
#
# Usage:
#   ./install.sh                           # all skills, user-level (~/.claude/skills)
#   ./install.sh --project                 # all skills, current project (.claude/skills)
#   ./install.sh ai-ux-design game-theory  # only the named categories
#   ./install.sh --list                    # list categories and skills
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
skills_root="$repo_dir/skills"
dest="${HOME}/.claude/skills"
categories=()

for arg in "$@"; do
  case "$arg" in
    --project) dest="$(pwd)/.claude/skills" ;;
    --list)
      for cat_dir in "$skills_root"/*/; do
        echo "$(basename "$cat_dir")"
        for skill_dir in "$cat_dir"*/; do
          [ -f "$skill_dir/SKILL.md" ] && echo "  $(basename "$skill_dir")"
        done
      done
      exit 0
      ;;
    -h|--help) sed -n '2,11p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    -*) echo "Unknown option: $arg" >&2; exit 1 ;;
    *) categories+=("$arg") ;;
  esac
done

if [ ${#categories[@]} -eq 0 ]; then
  for cat_dir in "$skills_root"/*/; do categories+=("$(basename "$cat_dir")"); done
fi

mkdir -p "$dest"
count=0
for category in "${categories[@]}"; do
  if [ ! -d "$skills_root/$category" ]; then
    echo "Unknown category: $category (run ./install.sh --list)" >&2
    exit 1
  fi
  for skill_dir in "$skills_root/$category"/*/; do
    [ -f "$skill_dir/SKILL.md" ] || continue
    name="$(basename "$skill_dir")"
    rm -rf "${dest:?}/$name"
    cp -R "$skill_dir" "$dest/$name"
    count=$((count + 1))
  done
done

echo "Installed $count skills into $dest"
echo "Restart Claude Code, then type / to see them."
