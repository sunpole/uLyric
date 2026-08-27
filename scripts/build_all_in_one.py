from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = [
    "00_MASTER_AGENT.md",
    "AGENTS.md",
    "01_PROJECT_SYSTEM.md",
    "02_ORCHESTRATOR_AGENT.md",
    "03_RHYME_AGENT.md",
    "04_RHYTHM_METER_AGENT.md",
    "05_SEMANTIC_STYLE_AGENT.md",
    "06_LINE_CONSTRUCTOR_AGENT.md",
    "07_POETIC_EDITOR_AGENT.md",
    "08_QA_CRITIC_AGENT.md",
    "09_SCORING_RUBRIC.md",
    "10_OUTPUT_TEMPLATES.md",
    "11_TEST_SUITE.md",
    "12_NORMATIVE_SOURCES.md",
    "13_RUSSIAN_PHONETICS.md",
    "14_BIBLE_CHECK_AGENT.md",
    "15_AI_STYLE_CHECK_AGENT.md",
    "16_USER_MODES.md",
    "17_CONTEXT_MANAGER.md",
    "18_FEEDBACK_LOOP.md",
    "19_FAILURE_RECOVERY.md",
    "20_USER_GUIDE.md",
]

parts = ["# uLyric — полный комплект агентов и правил\n"]

for name in FILES:
    path = ROOT / name
    if not path.exists():
        raise SystemExit(f"Missing required file: {name}")
    text = path.read_text(encoding="utf-8").rstrip()
    parts.append(f"\n\n---\n\n## FILE: {name}\n\n{text}\n")

output = ROOT / "ALL_IN_ONE.md"
output.write_text("".join(parts), encoding="utf-8")
print(f"Generated {output} from {len(FILES)} files")
