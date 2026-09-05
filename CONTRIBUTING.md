# Contributing to Chartsmith

Thanks for your interest in contributing! Chartsmith is a Claude Code skill, not a Python package — contributions are primarily new chart examples, design improvements, and documentation.

## Adding a New Example

1. Create a script in `examples/python/` following the existing structure:
   - Docstring with chart type and inspiration
   - `CONFIGURATION` block at the top with `DATA`, `CONTENT`, `STYLE`, `OUTPUT` sections
   - `CHART CODE` block below
   - Set `OUTPUT_FILE` to `examples/images/<chart_name>.png`

2. Every script must be independently runnable — no shared utility modules.

3. Run your script and commit the output PNG to `examples/images/`.

4. Add the example to the Examples section in `README.md`.

## Adding a New Chart Type

1. Add chart-type-specific instructions to the relevant section in `SKILL.md`.
2. Create at least one Python example demonstrating the chart type.
3. Follow the design constitution in `CONSTITUTION.md` — every chart should pass all 10 principles.

## Proposing Changes to the Constitution or Palette

Open an issue first to discuss. These are foundational to every chart Chartsmith generates, so changes should be deliberate.

## Style Guidelines

- Use the color tokens from `PALETTE.md` — don't hardcode one-off hex values.
- Keep examples self-contained. A user should be able to copy one script and run it.
- Follow the Storytelling with Data principles: declutter, direct-label, insight titles.

## Pull Request Process

1. Fork the repo and create a branch.
2. Make your changes.
3. Verify all example scripts still run: `for f in examples/python/*.py; do MPLBACKEND=Agg python "$f"; done`
4. Open a PR against `main`.

## Questions?

Open an issue — we're happy to help.
