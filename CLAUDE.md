# CLAUDE Operating Instructions

## Purpose
Permanent operating guidance for Claude Code when this repository is handed off for implementation.

## Overview
This repository is a pre-implementation engineering package. Use it to understand product scope, repository structure, architecture boundaries, prompt strategy, UI references, testing intent, and release sequencing before any code is written.

## Dependencies
- `README_FIRST.md`
- `PROJECT_CONTEXT.md`
- `MASTER_BUILD_WORKFLOW.md`
- `ARCHITECTURE_REVIEW.md`
- `docs/INDEX.md`

## Implementation Notes
- Do not create application code in this repository.
- Do not silently change requirements.
- If the specifications conflict or overlap, document the issue in `ARCHITECTURE_REVIEW.md`.
- Preserve original terminology unless the architecture review explicitly recommends a change.
- Prefer cross-references over duplication.
- Keep any future implementation aligned to the documented folder structure and module boundaries.

## Future Expansion
- Add implementation task notes only after the repository has been reviewed and approved.

## Related Documents
- `README_FIRST.md`
- `PROJECT_CONTEXT.md`
- `MASTER_BUILD_WORKFLOW.md`
- `ARCHITECTURE_REVIEW.md`
- `REPOSITORY_AUDIT.md`
