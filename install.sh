#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="chartsmith"
SKILL_FILE="SKILL.md"

usage() {
  echo "Usage: $0 [--global]"
  echo "  --global  Install to ~/.claude/skills/ (all projects)"
  echo "  default   Install to .claude/skills/ (current project)"
  exit 1
}

SCOPE="project"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --global) SCOPE="global"; shift ;;
    -h|--help) usage ;;
    *) echo "Unknown option: $1"; usage ;;
  esac
done

if [[ "$SCOPE" == "global" ]]; then
  TARGET_DIR="$HOME/.claude/skills/$SKILL_NAME"
else
  TARGET_DIR=".claude/skills/$SKILL_NAME"
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [[ -f "$SCRIPT_DIR/$SKILL_FILE" ]]; then
  SOURCE="$SCRIPT_DIR/$SKILL_FILE"
else
  echo "Error: $SKILL_FILE not found. Run this script from the chartsmith-skill repo root."
  exit 1
fi

mkdir -p "$TARGET_DIR"
cp "$SOURCE" "$TARGET_DIR/$SKILL_FILE"

echo "Chartsmith installed to $TARGET_DIR/$SKILL_FILE"
echo ""
echo "You can also install with: npx skills add masonsun/chartsmith-skill"
