# src/data_generation

This module will contain Python scripts for **generating synthetic CSI-like data** for use in fall detection research.

## Planned Contents

- Synthetic CSI amplitude and phase pattern generators
- Fall event simulation with configurable parameters
- Non-fall activity simulation (walking, sitting, standing)
- Data export utilities for downstream preprocessing

## Current Status

The current synthetic CSI generator is located at `src/simulate_csi.py` (flat module). This submodule directory is a forward-looking placeholder for when the `src/` flat structure is refactored into submodules.

> Migration to this submodule will be done carefully to avoid breaking existing imports.

---

*Part of Phase 1 repository restructuring — see [docs/roadmap.md](../../docs/roadmap.md)*
