from __future__ import annotations

import json

import pytest

from namaster_proof.cli import main
from namaster_proof.receipts import publish_json


def test_verify_and_validate_commands(tmp_path, capsys):
    result = tmp_path / "shard.json"
    publish_json(result, {"values": [1, 2]}, {"suite": "example", "n_real": 2})

    assert main(["verify", str(result)]) == 0
    verify_output = json.loads(capsys.readouterr().out)
    assert verify_output["status"] == "PASS"

    assert (
        main(
            [
                "validate",
                str(result),
                "--expect",
                "suite=example",
                "--expect",
                "n_real=2",
            ]
        )
        == 0
    )
    validate_output = json.loads(capsys.readouterr().out)
    assert validate_output["status"] == "PASS"


def test_validate_command_rejects_mismatch_and_duplicate_keys(tmp_path):
    result = tmp_path / "shard.json"
    publish_json(result, {"values": [1]}, {"suite": "example"})
    with pytest.raises(ValueError, match="suite"):
        main(["validate", str(result), "--expect", "suite=wrong"])
    with pytest.raises(ValueError, match="duplicate"):
        main(
            [
                "validate",
                str(result),
                "--expect",
                "suite=example",
                "--expect",
                "suite=example",
            ]
        )
