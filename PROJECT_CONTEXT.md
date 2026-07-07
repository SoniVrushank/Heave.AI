# PROJECT_CONTEXT

## Purpose
Defines the project context for the entire HEAVE repository.

## Overview
HEAVE is a premium AI operating workspace intended to combine assistant intelligence, workspace management, messaging-like interaction patterns, glass-forward design language, structured memory, automation, and professional release discipline. The target surfaces are Windows Desktop and Android Companion.

The repository is intentionally documentation-first. It packages the provided specifications into a clean handoff package so Claude Code can begin implementation with a stable understanding of the product.

## Dependencies
- `source_docs/`
- `docs/INDEX.md`
- `architecture/README.md`
- `prompts/README.md`
- `brand/README.md`
- `database/README.md`
- `tests/README.md`

## Implementation Notes
- Treat the source documents as authoritative.
- Use architecture pages to understand ownership boundaries.
- Use prompt pages to keep implementation and review behavior consistent.
- Use UI, brand, database, and testing documents as implementation constraints, not as optional reference material.

## Future Expansion
- Add product decisions, release notes, and implementation tickets only after architecture review.

## Related Documents
- `README_FIRST.md`
- `MASTER_BUILD_WORKFLOW.md`
- `TECH_STACK.md`
- `ROADMAP.md`
- `REPOSITORY_AUDIT.md`
