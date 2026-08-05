#!/usr/bin/env python3
"""Validate reproducibility manifests (directive Q2).

Checks:
  1. Every reproducibility/manifests/experiments/*.json validates against
     experiment.schema.json.
  2. Every reproducibility/manifests/programs/*.json validates against
     program.schema.json.
  3. Every experiment's code[].path exists in the repo.
  4. Every program's experiments[].id resolves to an experiments/*.json file.
  5. Every depends_on id resolves to an experiments/*.json file (or another
     program-listed id).

Uses the `jsonschema` package when installed; otherwise falls back to a
minimal structural check (required-keys + enum + type spot-check) so this
script has no hard external dependency.

Usage: python3 tools/validate_repro_manifests.py
Exit code: 0 if everything passes, 1 otherwise.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFESTS_DIR = REPO_ROOT / "reproducibility" / "manifests"
EXPERIMENTS_DIR = MANIFESTS_DIR / "experiments"
PROGRAMS_DIR = MANIFESTS_DIR / "programs"

try:
    import jsonschema  # type: ignore

    HAVE_JSONSCHEMA = True
except ImportError:
    HAVE_JSONSCHEMA = False


def load_json(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Minimal structural fallback (used when jsonschema is not installed)
# ---------------------------------------------------------------------------

def structural_check(instance: dict, schema: dict, label: str) -> list[str]:
    errors: list[str] = []
    required = schema.get("required", [])
    for key in required:
        if key not in instance:
            errors.append(f"{label}: missing required field '{key}'")

    props = schema.get("properties", {})
    for key, subschema in props.items():
        if key not in instance:
            continue
        value = instance[key]
        errors.extend(_check_value(value, subschema, f"{label}.{key}"))

    if schema.get("additionalProperties") is False:
        allowed = set(props.keys())
        for key in instance.keys():
            if key not in allowed:
                errors.append(f"{label}: unexpected field '{key}'")

    return errors


def _check_value(value, subschema: dict, label: str) -> list[str]:
    errors: list[str] = []

    if "const" in subschema:
        if value != subschema["const"]:
            errors.append(f"{label}: expected const {subschema['const']!r}, got {value!r}")
        return errors

    if "enum" in subschema:
        if value not in subschema["enum"]:
            errors.append(f"{label}: {value!r} not in enum {subschema['enum']}")

    t = subschema.get("type")
    if t is not None:
        types = t if isinstance(t, list) else [t]
        ok = False
        for ty in types:
            if ty == "string" and isinstance(value, str):
                ok = True
            elif ty == "number" and isinstance(value, (int, float)) and not isinstance(value, bool):
                ok = True
            elif ty == "integer" and isinstance(value, int) and not isinstance(value, bool):
                ok = True
            elif ty == "boolean" and isinstance(value, bool):
                ok = True
            elif ty == "array" and isinstance(value, list):
                ok = True
            elif ty == "object" and isinstance(value, dict):
                ok = True
            elif ty == "null" and value is None:
                ok = True
        if not ok:
            errors.append(f"{label}: type mismatch, expected {types}, got {type(value).__name__}")

    if subschema.get("type") == "array" and isinstance(value, list):
        item_schema = subschema.get("items")
        if item_schema:
            for i, item in enumerate(value):
                if item_schema.get("type") == "object":
                    errors.extend(structural_check(item, item_schema, f"{label}[{i}]"))
                else:
                    errors.extend(_check_value(item, item_schema, f"{label}[{i}]"))
        min_items = subschema.get("minItems")
        if min_items is not None and len(value) < min_items:
            errors.append(f"{label}: expected at least {min_items} items, got {len(value)}")

    if subschema.get("type") == "object" and isinstance(value, dict):
        errors.extend(structural_check(value, subschema, label))

    return errors


def validate_instance(instance: dict, schema: dict, label: str) -> list[str]:
    if HAVE_JSONSCHEMA:
        validator = jsonschema.Draft202012Validator(schema)
        return [f"{label}: {e.message} (at {'/'.join(str(p) for p in e.path)})" for e in validator.iter_errors(instance)]
    return structural_check(instance, schema, label)


# ---------------------------------------------------------------------------
# Main validation pass
# ---------------------------------------------------------------------------

def main() -> int:
    experiment_schema = load_json(MANIFESTS_DIR / "experiment.schema.json")
    program_schema = load_json(MANIFESTS_DIR / "program.schema.json")

    errors: list[str] = []
    warnings: list[str] = []

    experiment_files = sorted(EXPERIMENTS_DIR.glob("*.json"))
    program_files = sorted(PROGRAMS_DIR.glob("*.json"))

    if not experiment_files:
        errors.append("no experiment manifests found in reproducibility/manifests/experiments/")
    if not program_files:
        errors.append("no program manifests found in reproducibility/manifests/programs/")

    experiments: dict[str, dict] = {}
    rows: list[tuple[str, str, str, str]] = []  # id, program, status, est_cost

    for path in experiment_files:
        try:
            data = load_json(path)
        except json.JSONDecodeError as e:
            errors.append(f"{path.relative_to(REPO_ROOT)}: invalid JSON — {e}")
            continue

        label = str(path.relative_to(REPO_ROOT))
        errors.extend(validate_instance(data, experiment_schema, label))

        exp_id = data.get("id")
        if exp_id is None:
            errors.append(f"{label}: missing 'id'")
            continue
        if exp_id != path.stem:
            errors.append(f"{label}: id '{exp_id}' does not match filename '{path.stem}.json'")
        if exp_id in experiments:
            errors.append(f"{label}: duplicate experiment id '{exp_id}'")
        experiments[exp_id] = data

        # code[].path must exist in the repo
        for code_entry in data.get("code", []):
            code_path = code_entry.get("path")
            if not code_path:
                continue
            full = REPO_ROOT / code_path
            if not full.exists():
                errors.append(f"{label}: code[].path does not exist: {code_path}")

        program = data.get("program", "?")
        status = data.get("status", "?")
        est_cost = data.get("reproduction", {}).get("est_cost_usd", "?")
        rows.append((exp_id, program, status, str(est_cost)))

    program_experiment_ids: dict[str, set[str]] = {}

    for path in program_files:
        try:
            data = load_json(path)
        except json.JSONDecodeError as e:
            errors.append(f"{path.relative_to(REPO_ROOT)}: invalid JSON — {e}")
            continue

        label = str(path.relative_to(REPO_ROOT))
        errors.extend(validate_instance(data, program_schema, label))

        prog_id = data.get("id")
        if prog_id != path.stem:
            errors.append(f"{label}: id '{prog_id}' does not match filename '{path.stem}.json'")

        exp_list = data.get("experiments", [])
        ids_here = {e["id"] for e in exp_list if "id" in e}
        program_experiment_ids[prog_id or path.stem] = ids_here

        for entry in exp_list:
            eid = entry.get("id")
            if eid and eid not in experiments:
                errors.append(f"{label}: experiments[].id '{eid}' has no matching manifest in experiments/")
            for dep in entry.get("depends_on", []):
                if dep not in ids_here and dep not in experiments:
                    errors.append(f"{label}: depends_on '{dep}' (from '{eid}') does not resolve to any known experiment id")

    # cross-check: every experiment manifest should be referenced by exactly one program
    referenced = set()
    for ids in program_experiment_ids.values():
        referenced |= ids
    unreferenced = set(experiments.keys()) - referenced
    for eid in sorted(unreferenced):
        warnings.append(f"experiment '{eid}' is not referenced by any program manifest")

    # ------------------------------------------------------------------
    # Report
    # ------------------------------------------------------------------
    print(f"jsonschema available: {HAVE_JSONSCHEMA}")
    print(f"experiment manifests: {len(experiment_files)}")
    print(f"program manifests:    {len(program_files)}")
    print()

    if rows:
        id_w = max(len(r[0]) for r in rows) + 2
        prog_w = max(len(r[1]) for r in rows) + 2
        status_w = max(len(r[2]) for r in rows) + 2
        header = f"{'id':<{id_w}}{'program':<{prog_w}}{'status':<{status_w}}est_cost_usd"
        print(header)
        print("-" * len(header))
        for r in sorted(rows):
            print(f"{r[0]:<{id_w}}{r[1]:<{prog_w}}{r[2]:<{status_w}}{r[3]}")
        print()

    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print(f"FAILED — {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"PASSED — {len(experiment_files)} experiment manifests, {len(program_files)} program manifests, 0 errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
