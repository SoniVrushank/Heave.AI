from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "source_docs"
DOCS = ROOT / "docs"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\n", "\r\n"), encoding="utf-8")


def title_from_stem(stem: str) -> str:
    stem = re.sub(r"^\d+[._ ]*", "", stem)
    return stem.replace("_", " ").strip()


def read_docx(path: Path):
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
    tree = ET.fromstring(xml)
    blocks = []
    for p in tree.findall(".//w:p", NS):
        style = None
        ppr = p.find("w:pPr", NS)
        if ppr is not None:
            ps = ppr.find("w:pStyle", NS)
            if ps is not None:
                style = ps.attrib.get(f"{{{NS['w']}}}val")
        parts = []
        for node in p.iter():
            tag = node.tag.split("}")[-1]
            if tag == "t" and node.text:
                parts.append(node.text)
            elif tag == "tab":
                parts.append("\t")
            elif tag == "br":
                parts.append("\n")
        text = "".join(parts).strip()
        if text:
            blocks.append((style, text))
    return blocks


def doc_template(title: str, source: str, related: list[str]) -> str:
    related_lines = "\n".join(f"- `{item}`" for item in related)
    return f"""# {title}

## Purpose
Source-of-truth conversion of `{source}`.

## Overview
This document preserves the original specification content and keeps the repository organized for future implementation.

## Dependencies
- `source_docs/{source}`

## Implementation Notes
- Preserve all source meaning.
- Prefer cross-references over duplication.
- Do not add application code here.

## Future Expansion
- Add implementation notes only after the codebase exists.

## Related Documents
{related_lines}
"""


def build_docx_markdown():
    DOCS.mkdir(exist_ok=True)
    manifest = []
    for docx in sorted(SRC.glob("*.docx")):
        blocks = read_docx(docx)
        lines = [f"# {title_from_stem(docx.stem)}", "", "## Purpose", f"Source-of-truth conversion of `{docx.name}`.", "", "## Overview"]
        for style, text in blocks:
            if style and style.startswith("Heading"):
                level = min(int(style.replace("Heading", "") or "1"), 6)
                lines.append("#" * level + " " + text)
            else:
                lines.append(text)
            lines.append("")
        related = ["../README_FIRST.md", "../PROJECT_CONTEXT.md", "../MASTER_BUILD_WORKFLOW.md"]
        lower = docx.stem.lower()
        if "ui" in lower or "design" in lower:
            related += ["../ui_reference/README.md", "../brand/README.md"]
        if "database" in lower or "er" in lower:
            related += ["../database/README.md", "../architecture/database_architecture.md"]
        if "test" in lower or "qa" in lower:
            related += ["../tests/README.md"]
        if "prompt" in lower or "claude" in lower:
            related += ["../prompts/README.md", "../CLAUDE.md"]
        lines += ["## Dependencies", f"- `../source_docs/{docx.name}`", "", "## Implementation Notes", "- Preserve source meaning and terminology.", "- Cross-reference related documents instead of duplicating them.", "", "## Future Expansion", "- Add implementation notes only after the implementation repository exists.", "", "## Related Documents"]
        for item in dict.fromkeys(related):
            lines.append(f"- `{item}`")
        write(DOCS / f"{docx.stem}.md", "\n".join(lines).rstrip() + "\n")
        manifest.append((docx.name, f"{docx.stem}.md"))
    write(DOCS / "INDEX.md", "# HEAVE Documentation Index\n\n## Source Documents\n" + "\n".join(f"- `{a}` → `./{b}`" for a, b in manifest) + "\n")


def build_top_level():
    top = {
        "README_FIRST.md": doc_template("README_FIRST", "README_FIRST.md", ["PROJECT_CONTEXT.md", "MASTER_BUILD_WORKFLOW.md", "CLAUDE.md", "docs/INDEX.md"]),
        "CLAUDE.md": doc_template("CLAUDE", "CLAUDE.md", ["README_FIRST.md", "PROJECT_CONTEXT.md", "MASTER_BUILD_WORKFLOW.md", "ARCHITECTURE_REVIEW.md"]),
        "PROJECT_CONTEXT.md": doc_template("PROJECT_CONTEXT", "PROJECT_CONTEXT.md", ["README_FIRST.md", "MASTER_BUILD_WORKFLOW.md", "TECH_STACK.md", "ROADMAP.md"]),
        "MASTER_BUILD_WORKFLOW.md": doc_template("MASTER_BUILD_WORKFLOW", "MASTER_BUILD_WORKFLOW.md", ["ARCHITECTURE_REVIEW.md", "REPOSITORY_AUDIT.md", "ROADMAP.md"]),
        "TECH_STACK.md": doc_template("TECH_STACK", "TECH_STACK.md", ["architecture/system_architecture.md", "architecture/api_architecture.md", "architecture/database_architecture.md"]),
        "ROADMAP.md": doc_template("ROADMAP", "ROADMAP.md", ["MASTER_BUILD_WORKFLOW.md", "ARCHITECTURE_REVIEW.md", "REPOSITORY_AUDIT.md"]),
        "CHANGELOG.md": doc_template("CHANGELOG", "CHANGELOG.md", ["REPOSITORY_AUDIT.md", "ARCHITECTURE_REVIEW.md"]),
        "LICENSE.md": doc_template("LICENSE", "LICENSE.md", ["CONTRIBUTING.md", "README_FIRST.md"]),
        "CONTRIBUTING.md": doc_template("CONTRIBUTING", "CONTRIBUTING.md", ["CLAUDE.md", "ARCHITECTURE_REVIEW.md", "tests/README.md"]),
        "REPOSITORY_AUDIT.md": doc_template("REPOSITORY_AUDIT", "REPOSITORY_AUDIT.md", ["docs/INDEX.md", "architecture/README.md", "prompts/README.md"]),
        "ARCHITECTURE_REVIEW.md": doc_template("ARCHITECTURE_REVIEW", "ARCHITECTURE_REVIEW.md", ["architecture/README.md", "docs/INDEX.md", "MASTER_BUILD_WORKFLOW.md"]),
    }
    for name, text in top.items():
        write(ROOT / name, text)


def build_architecture():
    titles = [
        "system_architecture", "folder_structure", "data_flow", "ai_router", "memory_engine",
        "workspace_engine", "automation_engine", "desktop_architecture", "android_architecture",
        "api_architecture", "security_architecture", "logging_architecture", "update_architecture",
        "database_architecture", "module_dependencies"
    ]
    write(ROOT / "architecture" / "README.md", "# Architecture\n\n## Related Documents\n" + "\n".join(f"- `{t}.md`" for t in titles) + "\n")
    for name in titles:
        write(ROOT / "architecture" / f"{name}.md", doc_template(title_from_stem(name), f"{name}.md", ["../PROJECT_CONTEXT.md", "../MASTER_BUILD_WORKFLOW.md"]))

    diagrams = {
        "system_architecture_diagram.md": "graph TD\n  A[HEAVE] --> B[Workspace Engine]\n  A --> C[AI Router]\n  A --> D[Memory Engine]\n  A --> E[Automation Engine]\n  A --> F[Desktop]\n  A --> G[Android]\n",
        "folder_structure_diagram.md": "graph TD\n  A[HEAVE] --> B[docs]\n  A --> C[architecture]\n  A --> D[prompts]\n  A --> E[ui_reference]\n  A --> F[brand]\n  A --> G[database]\n  A --> H[tests]\n  A --> I[scripts]\n  A --> J[examples]\n",
        "database_er_diagram.md": "erDiagram\n  USER ||--o{ WORKSPACE : owns\n  WORKSPACE ||--o{ MEMORY : stores\n  WORKSPACE ||--o{ AUTOMATION : contains\n",
        "ai_flow_diagram.md": "flowchart TD\n  A[User Intent] --> B[AI Router]\n  B --> C[Prompt Selection]\n  C --> D[Model Call]\n  D --> E[Response]\n",
        "memory_flow_diagram.md": "flowchart TD\n  A[Context] --> B[Memory Engine]\n  B --> C[Persist]\n  B --> D[Recall]\n",
        "automation_flow_diagram.md": "flowchart TD\n  A[Trigger] --> B[Automation Engine]\n  B --> C[Condition]\n  C --> D[Action]\n",
        "startup_flow_diagram.md": "flowchart TD\n  A[Launch] --> B[Auth]\n  B --> C[Load Workspace]\n  C --> D[Route AI]\n",
        "authentication_flow_diagram.md": "flowchart TD\n  A[Start] --> B[Credentials]\n  B --> C[Verify]\n  C --> D[Session]\n",
        "update_flow_diagram.md": "flowchart TD\n  A[Check] --> B[Validate]\n  B --> C[Download]\n  C --> D[Apply]\n",
        "workspace_flow_diagram.md": "flowchart TD\n  A[Open Workspace] --> B[Load State]\n  B --> C[Navigate]\n  C --> D[Interact]\n",
    }
    for name, body in diagrams.items():
        write(ROOT / "architecture" / name, f"# {title_from_stem(name)}\n\n```mermaid\n{body}```\n")


def build_prompts():
    items = ["master_prompt.md", "coding.md", "ui.md", "research.md", "debugging.md", "marketing.md", "hirvi_personality.md"]
    write(ROOT / "prompts" / "README.md", "# Prompts\n\n## Related Documents\n" + "\n".join(f"- `{item}`" for item in items) + "\n")
    for item in items:
        write(ROOT / "prompts" / item, doc_template(title_from_stem(item), item, ["../CLAUDE.md", "../PROJECT_CONTEXT.md"]))


def build_reference_sections():
    sections = {
        "ui_reference/README.md": ["desktop/README.md", "mobile/README.md", "components/README.md", "animations/README.md", "glass_effects/README.md", "navigation/README.md"],
        "brand/README.md": ["colors.md", "typography.md", "icons.md", "glass_design_rules.md", "motion_rules.md", "spacing.md", "design_tokens.md"],
        "database/README.md": ["schema.sql", "database_dictionary.md", "migration_strategy.md"],
        "tests/README.md": ["acceptance_criteria.md", "regression_checklist.md", "performance_checklist.md", "security_checklist.md"],
        "scripts/README.md": ["development_scripts.md", "build_scripts.md", "deployment_scripts.md"],
        "examples/README.md": ["example_projects.md", "example_workspaces.md", "example_memory.md", "example_automations.md"],
    }
    for path, items in sections.items():
        write(ROOT / path, "# " + title_from_stem(Path(path).stem) + "\n\n## Related Documents\n" + "\n".join(f"- `{item}`" for item in items) + "\n")
        for item in items:
            target = ROOT / Path(path).parent / item
            if item.endswith(".sql"):
                write(target, "-- schema.sql\n-- Documentation placeholder only.\n")
            else:
                write(target, doc_template(title_from_stem(item), item, ["../README.md"]))

    placeholder_map = {
        "ui_reference/desktop": ["home_screen_reference.md", "workspace_shell_reference.md", "settings_panel_reference.md"],
        "ui_reference/mobile": ["mobile_home_reference.md", "quick_actions_reference.md", "sync_status_reference.md"],
        "ui_reference/components": ["cards_reference.md", "buttons_reference.md", "modals_reference.md"],
        "ui_reference/animations": ["launch_animation_reference.md", "transition_reference.md", "microinteraction_reference.md"],
        "ui_reference/glass_effects": ["glass_panel_reference.md", "blur_layer_reference.md", "transparency_state_reference.md"],
        "ui_reference/navigation": ["nav_rail_reference.md", "command_palette_reference.md", "tab_switching_reference.md"],
    }
    for folder, files in placeholder_map.items():
        for file_name in files:
            write(
                ROOT / folder / file_name,
                doc_template(
                    title_from_stem(file_name),
                    file_name,
                    ["../README.md", "../../brand/README.md"]
                )
            )


if __name__ == "__main__":
    build_docx_markdown()
    build_top_level()
    build_architecture()
    build_prompts()
    build_reference_sections()
