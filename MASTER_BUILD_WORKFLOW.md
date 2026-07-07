# MASTER_BUILD_WORKFLOW

## Purpose
Defines the implementation order Claude Code should follow when the repository is converted into product code.

## Overview
This workflow is designed to reduce rework and keep the implementation sequence grounded in the repository’s documentation.

Recommended order:
1. Confirm the repository audit and architecture review.
2. Validate the normalized documentation set in `docs/`.
3. Confirm the architecture layer and module boundaries.
4. Confirm data model, storage rules, and retention assumptions.
5. Confirm prompt strategy and AI routing expectations.
6. Confirm UI references, motion language, and brand rules.
7. Confirm security, logging, and update behavior.
8. Confirm acceptance criteria, regression scope, and performance expectations.
9. Only then begin implementation planning in the target codebase.

## Dependencies
- `PROJECT_CONTEXT.md`
- `ARCHITECTURE_REVIEW.md`
- `REPOSITORY_AUDIT.md`
- `architecture/README.md`
- `docs/INDEX.md`
- `tests/README.md`

## Implementation Notes
- Keep execution order explicit and linear.
- Do not begin product code before the architecture and test expectations are understood.
- Treat this file as the contract for implementation sequencing.

## Future Expansion
- Add milestone-level task groupings once implementation planning begins.

## Related Documents
- `README_FIRST.md`
- `ROADMAP.md`
- `CHANGELOG.md`
- `REPOSITORY_AUDIT.md`
