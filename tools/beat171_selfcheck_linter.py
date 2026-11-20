#!/usr/bin/env python3
"""BEAT171 answer-card structural linter.

PASS scope is deliberately narrow: parseable card + concrete-looking, non-slot
pointer syntax + executable falsifier binding. It does not resolve remote
pointers and does not certify scientific claims.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

POINTER_RE = re.compile(r"\b(?P<kind>artifact|art|run|commit|git)://[^\s`）)，。；;|]+")
SHA40_RE = re.compile(r"\b[0-9a-fA-F]{40}\b")
PLACEHOLDER_RE = re.compile(r"<[^>\n]+>|\*|\b(?:TBD|TODO|XXX)\b", re.I)
SLOT_RE = re.compile(r"占位|槽位|待回填|不虚构|不臆造|非伪造实体|实际值以|格式约定")
FALSIFIER_RE = re.compile(r"证伪|反例|falsif", re.I)
EXEC_RE = re.compile(r"(?:^|\s|`)(?:python3?\s+\S+|pytest\s+\S+|lake\s+env\s+lean\s+\S+|lean\s+\S+|z3\s+\S+)", re.I)
DEFER_RE = re.compile(r"拟|待|草案|桩|stub|未接|可用后", re.I)
ENGINE_RE = re.compile(r"^引擎:\s*\S+/([^\s]+)", re.M)
TRACK_RE = re.compile(r"CLASSIFY:.*?(vinf代铸轨SEMANTIC-RESPONDER-01)")


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def line_no(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def pointer_section(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    starts = [i for i, s in enumerate(lines) if "可审计" in s and ("指针" in s or "artifact" in s)]
    if not starts:
        return "", 0
    start = starts[0]
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r"^\s*(?:##\s*|\*\*)[②③]", lines[i]):
            end = i
            break
    return "\n".join(lines[start:end]), start + 1


def lint(text: str) -> dict:
    lines = text.splitlines()
    failures = []
    checks = {}

    classify_lines = [i + 1 for i, s in enumerate(lines) if s.startswith("CLASSIFY:")]
    section_lines = {
        "1": [i + 1 for i, s in enumerate(lines) if re.match(r"^\s*(?:##\s*|\*\*)①", s)],
        "2": [i + 1 for i, s in enumerate(lines) if re.match(r"^\s*(?:##\s*|\*\*)②", s)],
        "3": [i + 1 for i, s in enumerate(lines) if re.match(r"^\s*(?:##\s*|\*\*)③", s)],
    }
    machine_ok = len(classify_lines) == 1 and all(len(v) == 1 for v in section_lines.values())
    checks["machine_readable"] = {
        "pass": machine_ok,
        "classify_lines": classify_lines,
        "section_lines": section_lines,
    }
    if not machine_ok:
        failures.append({"check": "machine_readable", "lines": classify_lines, "reason": "require exactly one CLASSIFY and sections ①②③"})

    section, section_start = pointer_section(text)
    pointer_rows = []
    slot_context = bool(SLOT_RE.search(section))
    for match in POINTER_RE.finditer(section):
        token = match.group(0).rstrip(".:")
        kind = match.group("kind")
        local_line = section.count("\n", 0, match.start()) + 1
        absolute_line = section_start + local_line - 1 if section_start else 0
        token_line = section.splitlines()[local_line - 1]
        placeholder = bool(PLACEHOLDER_RE.search(token))
        line_slot = bool(SLOT_RE.search(token_line))
        shape_ok = True
        shape_reason = "scheme token present"
        if kind in {"commit", "git"}:
            shape_ok = bool(re.search(r"@[0-9a-fA-F]{40}(?::|$|/)", token))
            shape_reason = "commit/git pointer requires @<40-hex-sha>"
        elif kind in {"artifact", "art", "run"}:
            shape_ok = bool(re.search(r"/[A-Za-z0-9][A-Za-z0-9_.-]*$", token))
            shape_reason = "artifact/run pointer requires concrete terminal identifier"
        concrete = shape_ok and not placeholder and not slot_context and not line_slot
        reasons = []
        if placeholder:
            reasons.append("placeholder_or_wildcard")
        if slot_context or line_slot:
            reasons.append("declared_slot_or_format_not_entity")
        if not shape_ok:
            reasons.append(shape_reason)
        pointer_rows.append({"token": token, "kind": kind, "line": absolute_line, "concrete": concrete, "reasons": reasons})
    concrete_pointers = [p for p in pointer_rows if p["concrete"]]
    pointer_ok = bool(section) and bool(concrete_pointers)
    checks["pointer_traceable_syntax"] = {
        "pass": pointer_ok,
        "section_start_line": section_start,
        "slot_context": slot_context,
        "pointers": pointer_rows,
        "concrete_count": len(concrete_pointers),
        "resolution": "NOT_RUN_STRUCTURAL_LINT_ONLY",
    }
    if not pointer_ok:
        failures.append({
            "check": "pointer_traceable_syntax",
            "line": section_start,
            "reason": "no concrete non-slot artifact/run/commit pointer; remote resolution not attempted",
        })

    sec2_start = section_lines["2"][0] - 1 if len(section_lines["2"]) == 1 else None
    sec3_start = section_lines["3"][0] - 1 if len(section_lines["3"]) == 1 else len(lines)
    sec2_lines = lines[sec2_start:sec3_start] if sec2_start is not None else []
    falsifier_lines = [i + 1 for i, s in enumerate(lines) if FALSIFIER_RE.search(s)]
    executable_bindings = []
    for i in range(sec2_start or 0, sec3_start):
        s = lines[i]
        if FALSIFIER_RE.search(s) and EXEC_RE.search(s) and not DEFER_RE.search(s):
            executable_bindings.append({"line": i + 1, "text": s.strip()})
    # A separately labelled falsifier command may occupy the following line.
    for i in range(sec2_start or 0, max(sec2_start or 0, sec3_start - 1)):
        if FALSIFIER_RE.search(lines[i]) and EXEC_RE.search(lines[i + 1]) and not DEFER_RE.search(lines[i + 1]):
            row = {"line": i + 2, "text": lines[i + 1].strip()}
            if row not in executable_bindings:
                executable_bindings.append(row)
    falsifier_ok = bool(executable_bindings) and bool(concrete_pointers)
    checks["executable_falsifier_binding"] = {
        "pass": falsifier_ok,
        "falsifier_mention_lines": falsifier_lines,
        "executable_bindings": executable_bindings,
        "requires_concrete_pointer": True,
        "scope": "machine-auditable answer-card criterion, not a general definition of scientific falsifiability",
    }
    if not falsifier_ok:
        failures.append({
            "check": "executable_falsifier_binding",
            "lines": falsifier_lines,
            "reason": "falsifier narrative is not bound to both an executable command and a concrete pointer",
        })

    engine = ENGINE_RE.search(text)
    track = TRACK_RE.search(text)
    formal_tokens = {}
    for name, pattern in {
        "lean": r"\blean\s+\S+|\.lean\b|lake\s+env\s+lean",
        "z3": r"\bz3\b",
        "pytest": r"\bpytest\b",
        "assert": r"^\s*assert\s+",
        "sha40": r"\b[0-9a-fA-F]{40}\b",
    }.items():
        formal_tokens[name] = [i + 1 for i, s in enumerate(lines) if re.search(pattern, s, re.I | re.M)]
    return {
        "verdict": "PASS" if not failures else "FAIL",
        "scope": "STRUCTURAL_LINT_ONLY_NOT_REMOTE_RESOLUTION_NOT_SCIENTIFIC_VALIDATION",
        "checks": checks,
        "failures": failures,
        "provenance": {
            "engine": engine.group(1) if engine else None,
            "responder_track": track.group(1) if track else None,
            "formal_or_executable_evidence_lines": formal_tokens,
        },
    }


def lint_file(path: Path) -> dict:
    raw = path.read_bytes()
    result = lint(raw.decode("utf-8"))
    result.update({"file": str(path), "bytes": len(raw), "sha256": sha256(raw)})
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cards", nargs="+")
    ap.add_argument("--output")
    args = ap.parse_args()
    results = [lint_file(Path(p)) for p in args.cards]
    report = {
        "schema": "BEAT171-SELFCHECK-LINTER-01",
        "scope": "STRUCTURAL_LINT_ONLY",
        "counts": {
            "total": len(results),
            "pass": sum(r["verdict"] == "PASS" for r in results),
            "fail": sum(r["verdict"] == "FAIL" for r in results),
        },
        "results": results,
    }
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(payload)
    else:
        print(payload, end="")
    return 0 if all(r["verdict"] == "PASS" for r in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
