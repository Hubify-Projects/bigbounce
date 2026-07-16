from __future__ import annotations

import json

import pytest

import namaster_proof.receipts as receipts_module
from namaster_proof.receipts import (
    publish_json,
    receipt_path,
    validate_json_receipt,
    verify_json_receipt,
)


def test_publish_and_validate_round_trip(tmp_path):
    result = tmp_path / "shard.json"
    receipt = publish_json(
        result,
        {"values": [1.0, 2.0]},
        {"suite": "c10", "n_real": 2, "seed_start": 42, "seed_end": 43},
    )
    payload, validated = validate_json_receipt(
        result,
        expected={"suite": "c10", "n_real": 2},
        expected_seed_start=42,
    )
    assert payload == {"values": [1.0, 2.0]}
    assert validated == receipt


def test_result_mutation_is_rejected(tmp_path):
    result = tmp_path / "shard.json"
    publish_json(result, {"values": [1]}, {"suite": "test"})
    result.write_text('{"values":[2]}\n', encoding="utf-8")
    with pytest.raises(ValueError, match="invalid receipt"):
        verify_json_receipt(result)


def test_receipt_mutation_and_wrong_expectation_are_rejected(tmp_path):
    result = tmp_path / "shard.json"
    publish_json(result, {"values": [1]}, {"suite": "test"})
    sidecar = receipt_path(result)
    receipt = json.loads(sidecar.read_text(encoding="utf-8"))
    receipt["result_sha256"] = "0" * 64
    sidecar.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match="result_sha256"):
        verify_json_receipt(result)

    publish_json(result, {"values": [1]}, {"suite": "test"})
    with pytest.raises(ValueError, match="suite"):
        validate_json_receipt(result, expected={"suite": "other"})


def test_metadata_cannot_override_content_binding(tmp_path):
    with pytest.raises(ValueError, match="protected receipt fields"):
        publish_json(
            tmp_path / "shard.json",
            {"values": [1]},
            {"result_sha256": "attacker-controlled"},
        )


def test_publish_rejects_nonfinite_payload_and_metadata_before_writing(tmp_path):
    result = tmp_path / "shard.json"
    with pytest.raises(ValueError, match="Out of range float values"):
        publish_json(result, {"value": float("nan")}, {"suite": "test"})
    assert not result.exists()
    assert not receipt_path(result).exists()

    with pytest.raises(ValueError, match="Out of range float values"):
        publish_json(result, {"value": 1.0}, {"suite": "test", "metric": float("inf")})
    assert not result.exists()
    assert not receipt_path(result).exists()


def test_verify_rejects_nonstandard_json_constants(tmp_path):
    result = tmp_path / "shard.json"
    result.write_text('{"value": NaN}\n', encoding="utf-8")
    receipt_path(result).write_text("{}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="non-standard JSON constant"):
        verify_json_receipt(result)


def test_concurrent_pair_replacement_cannot_mix_payload_generations(
    tmp_path, monkeypatch
):
    result = tmp_path / "shard.json"
    publish_json(result, {"generation": 1}, {"suite": "test", "generation": 1})
    original_read = receipts_module._read_bytes
    switched = False

    def racing_read(path):
        nonlocal switched
        snapshot = original_read(path)
        if path == result and not switched:
            switched = True
            publish_json(
                result,
                {"generation": 2},
                {"suite": "test", "generation": 2},
            )
        return snapshot

    monkeypatch.setattr(receipts_module, "_read_bytes", racing_read)
    with pytest.raises(ValueError, match="invalid receipt"):
        verify_json_receipt(result)


def test_concurrent_publishers_cannot_cross_bind_metadata_and_bytes(
    tmp_path, monkeypatch
):
    result = tmp_path / "shard.json"
    original_write = receipts_module._atomic_write
    interleaved = False

    def racing_write(path, data):
        nonlocal interleaved
        original_write(path, data)
        if path == result and not interleaved:
            interleaved = True
            competing = b'{\n  "generation": 2\n}\n'
            original_write(result, competing)

    monkeypatch.setattr(receipts_module, "_atomic_write", racing_write)
    publish_json(
        result,
        {"generation": 1},
        {"suite": "test", "generation": 1},
    )
    with pytest.raises(ValueError, match="invalid receipt"):
        validate_json_receipt(
            result,
            expected={"suite": "test", "generation": 1},
        )
