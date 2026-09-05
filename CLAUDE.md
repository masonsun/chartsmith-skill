# Chartsmith

This is a Claude Code skill repo, not a Python package.

## Key files

- `SKILL.md` — the main skill file users install
- `CONSTITUTION.md` — 10 design principles governing every chart
- `PALETTE.md` — gray palette + 5 accent color families
- `examples/python/` — standalone example scripts
- `examples/images/` — rendered PNGs from those scripts
- `examples/sample_data.csv` — demo CSV used by `sample_output.py`

## Conventions

- Every example script is independently runnable — no shared utility modules
- All configurable values go in the `CONFIGURATION` block at the top of each script
- Output images go in `examples/images/`
- Scripts are run from the repo root: `python examples/python/<script>.py`
- Use `MPLBACKEND=Agg` for headless rendering
