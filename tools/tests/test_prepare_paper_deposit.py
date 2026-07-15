from __future__ import annotations

import hashlib
import json
import subprocess
import tarfile
from argparse import Namespace
from io import BytesIO
from pathlib import Path

import pytest

from tools.prepare_paper_deposit import DepositError, prepare, verify_tarball


def _run(root: Path, *args: str) -> str:
    result = subprocess.run(args, cwd=root, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def _minimal_pdf() -> bytes:
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 72 72] /Contents 4 0 R >>",
        b"<< /Length 0 >>\nstream\n\nendstream",
    ]
    body = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for index, obj in enumerate(objects, 1):
        offsets.append(len(body))
        body.extend(f"{index} 0 obj\n".encode() + obj + b"\nendobj\n")
    xref = len(body)
    body.extend(f"xref\n0 {len(objects) + 1}\n".encode())
    body.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        body.extend(f"{offset:010d} 00000 n \n".encode())
    body.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    )
    return bytes(body)


def _fixture(tmp_path: Path, *, version: str = "v1.2.3") -> tuple[Path, Path, str]:
    root = tmp_path / "repo"
    root.mkdir()
    (root / "paper").mkdir()
    (root / "proofs").mkdir()
    (root / "provenance").mkdir()
    (root / "provenance" / "claim.json").write_text('{"claim":"exact"}\n')
    (root / "paper" / "main.tex").write_text(
        f"\\newcommand{{\\paperVersion}}{{{version}}}\n\\documentclass{{article}}\n\\begin{{document}}x\\end{{document}}\n"
    )
    (root / "paper" / "main.pdf").write_bytes(_minimal_pdf())
    tarball = root / "paper" / f"main_{version}.tar.gz"
    with tarfile.open(tarball, "w:gz") as archive:
        payload = (root / "paper" / "main.tex").read_bytes()
        info = tarfile.TarInfo("main.tex")
        info.size = len(payload)
        archive.addfile(info, BytesIO(payload))
    config = {
        "papers": {
            "P4": {
                "tex": "paper/main.tex",
                "pdf": "paper/main.pdf",
                "arxiv_tarball": "paper/main_{version}.tar.gz",
                "standalone_proof": "proofs/{version}.json",
                "tarball_main_tex": "main.tex",
                "deposit_root": ".deposit-staging",
                "provenance_globs": ["provenance/**/*"],
                "provenance_archive": "P4_v1.2.3_provenance.tar.gz",
                "metadata": {
                    "title": "Synthetic release",
                    "creators": [{"name": "Tester, A"}],
                    "description": "Synthetic exact release.",
                    "upload_type": "publication",
                    "publication_type": "article",
                    "access_right": "open",
                    "license": "cc-by-4.0",
                },
            }
        }
    }
    config_path = root / "config.json"
    config_path.write_text(json.dumps(config))
    _run(root, "git", "init", "-q")
    _run(root, "git", "config", "user.email", "test@example.com")
    _run(root, "git", "config", "user.name", "Test")
    _run(root, "git", "add", ".")
    _run(root, "git", "commit", "-qm", "inputs")
    release_commit = _run(root, "git", "rev-parse", "HEAD")
    proof = {
        "paper_id": "P4",
        "paper_version": version,
        "git_commit": release_commit,
        "tarball_sha256": hashlib.sha256(tarball.read_bytes()).hexdigest(),
        "page_count": 1,
        "status": "pass",
        "engine": "synthetic-test-engine",
        "errors": 0,
        "undefined_references": 0,
    }
    proof_path = root / "proofs" / f"{version}.json"
    proof_path.write_text(json.dumps(proof))
    _run(root, "git", "add", str(proof_path.relative_to(root)))
    _run(root, "git", "commit", "-qm", "proof")
    return root, config_path, release_commit


def _args(root: Path, config: Path, commit: str, **overrides: object) -> Namespace:
    values = {
        "paper": "P4",
        "git_commit": commit,
        "repo": str(root),
        "config": str(config),
        "proof": None,
        "verify_tarball": False,
        "write": False,
    }
    values.update(overrides)
    return Namespace(**values)


def _replace_proof(root: Path, **changes: object) -> None:
    proof = root / "proofs" / "v1.2.3.json"
    payload = json.loads(proof.read_text())
    payload.update(changes)
    proof.write_text(json.dumps(payload))
    _run(root, "git", "add", str(proof.relative_to(root)))
    _run(root, "git", "commit", "-qm", "alter proof")


def test_dry_run_and_write_are_exact_and_no_external_state(tmp_path: Path) -> None:
    root, config, commit = _fixture(tmp_path)
    dry = prepare(_args(root, config, commit))
    output = root / dry["staging_directory"]
    assert dry["dry_run"] is True
    assert dry["external_state_mutated"] is False
    assert not output.exists()

    written = prepare(_args(root, config, commit, write=True))
    assert written["dry_run"] is False
    assert (output / "manifest.json").is_file()
    assert (output / ".zenodo.json").is_file()
    assert (output / "SHA256SUMS").is_file()
    assert (output / "main.pdf").read_bytes() == (root / "paper" / "main.pdf").read_bytes()
    assert "placeholder" not in (output / ".zenodo.json").read_text().lower()
    provenance = output / "P4_v1.2.3_provenance.tar.gz"
    assert provenance.is_file()
    provenance_record = next(item for item in written["assets"] if item["name"] == provenance.name)
    assert provenance_record["sha256"] == hashlib.sha256(provenance.read_bytes()).hexdigest()
    assert provenance_record["source"] == "generated from 1 tracked provenance files"
    with tarfile.open(provenance, "r:gz") as archive:
        assert archive.getnames() == ["provenance/claim.json"]
        assert archive.extractfile("provenance/claim.json").read() == b'{"claim":"exact"}\n'


def test_version_mismatch_fails_closed(tmp_path: Path) -> None:
    root, config, commit = _fixture(tmp_path)
    _replace_proof(root, paper_version="v9.9.9")
    with pytest.raises(DepositError, match="paper_version does not match"):
        prepare(_args(root, config, commit))


def test_tarball_hash_mismatch_fails_closed(tmp_path: Path) -> None:
    root, config, commit = _fixture(tmp_path)
    _replace_proof(root, tarball_sha256="0" * 64)
    with pytest.raises(DepositError, match="tarball_sha256 does not match"):
        prepare(_args(root, config, commit))


def test_missing_versioned_tarball_fails_closed(tmp_path: Path) -> None:
    root, config, commit = _fixture(tmp_path)
    (root / "paper" / "main_v1.2.3.tar.gz").unlink()
    with pytest.raises(DepositError, match="tarball is missing"):
        prepare(_args(root, config, commit))


def test_invalid_pdf_magic_fails_closed(tmp_path: Path) -> None:
    root, config, commit = _fixture(tmp_path)
    (root / "paper" / "main.pdf").write_bytes(b"not a pdf")
    with pytest.raises(DepositError, match="PDF magic"):
        prepare(_args(root, config, commit))


def test_short_or_unknown_commit_fails_closed(tmp_path: Path) -> None:
    root, config, commit = _fixture(tmp_path)
    with pytest.raises(DepositError, match="full lowercase"):
        prepare(_args(root, config, commit[:12]))
    with pytest.raises(DepositError, match="git rev-parse"):
        prepare(_args(root, config, "0" * 40))


def test_explicitly_incomplete_metadata_fails_closed(tmp_path: Path) -> None:
    root, config, commit = _fixture(tmp_path)
    payload = json.loads(config.read_text())
    payload["papers"]["P4"]["metadata_complete"] = False
    payload["papers"]["P4"]["metadata_blocker"] = "license decision required"
    config.write_text(json.dumps(payload))
    _run(root, "git", "add", "config.json")
    _run(root, "git", "commit", "-qm", "block metadata")
    with pytest.raises(DepositError, match="license decision required"):
        prepare(_args(root, config, commit))


def test_verify_tarball_reads_generated_log_for_undefined_references(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    tex = b"\\documentclass{article}\\begin{document}x\\end{document}\n"
    tarball = root / "source.tar.gz"
    with tarfile.open(tarball, "w:gz") as archive:
        info = tarfile.TarInfo("main.tex")
        info.size = len(tex)
        archive.addfile(info, BytesIO(tex))

    monkeypatch.setattr("tools.prepare_paper_deposit.shutil.which", lambda _: "/usr/bin/tectonic")

    class Result:
        returncode = 0
        stdout = b""
        stderr = b""

    def fake_run(cwd: Path, *command: str) -> Result:
        (cwd / "main.pdf").write_bytes(_minimal_pdf())
        (cwd / "main.log").write_text(
            "Package natbib Warning: Citation `missing' undefined.\n"
            "LaTeX Warning: There were undefined references.\n"
        )
        return Result()

    monkeypatch.setattr("tools.prepare_paper_deposit.run", fake_run)
    monkeypatch.setattr("tools.prepare_paper_deposit.pdf_page_count", lambda _root, _pdf: 1)
    with pytest.raises(DepositError, match="undefined="):
        verify_tarball(root, tarball, "main.tex", 1)
