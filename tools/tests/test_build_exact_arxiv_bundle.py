from __future__ import annotations

import hashlib
import io
import json
import subprocess
import tarfile
from argparse import Namespace
from pathlib import Path

import pytest

from tools.build_exact_arxiv_bundle import build
from tools.prepare_paper_deposit import DepositError


def _run(root: Path, *args: str) -> str:
    return subprocess.run(args, cwd=root, check=True, capture_output=True, text=True).stdout.strip()


def _fixture(tmp_path: Path) -> tuple[Path, Path, str, bytes]:
    root = tmp_path / "repo"
    (root / "paper").mkdir(parents=True)
    (root / "vendor").mkdir()
    tex = b"\\newcommand{\\paperVersion}{v1.2.3}\nbody\n"
    cls = b"exact class bytes\n"
    (root / "paper/main.tex").write_bytes(tex)
    (root / "paper/figure.pdf").write_bytes(b"figure bytes\n")
    with tarfile.open(root / "vendor/upstream.tar.gz", "w:gz") as archive:
        info = tarfile.TarInfo("tex/aastex701.cls")
        info.size = len(cls)
        archive.addfile(info, io.BytesIO(cls))
    config = {
        "papers": {"P4": {
            "tex": "paper/main.tex", "pdf": "paper/figure.pdf",
            "arxiv_tarball": "unused", "standalone_proof": "unused",
            "tarball_main_tex": "main.tex", "deposit_root": ".stage", "metadata": {},
            "bundle_assets": [
                {"source": "paper/main.tex", "archive_name": "main.tex"},
                {"source": "paper/figure.pdf", "archive_name": "figures/figure.pdf"},
            ],
            "bundle_tar_members": [
                {"source_tarball": "vendor/upstream.tar.gz", "member": "tex/aastex701.cls",
                 "archive_name": "aastex701.cls", "expected_sha256": hashlib.sha256(cls).hexdigest()},
            ],
        }}
    }
    config_path = root / "config.json"
    config_path.write_text(json.dumps(config))
    _run(root, "git", "init", "-q")
    _run(root, "git", "config", "user.email", "test@example.com")
    _run(root, "git", "config", "user.name", "Test")
    _run(root, "git", "add", ".")
    _run(root, "git", "commit", "-qm", "fixture")
    return root, config_path, _run(root, "git", "rev-parse", "HEAD"), cls


def _args(root: Path, config: Path, commit: str, output: str, write: bool = False) -> Namespace:
    return Namespace(paper="P4", git_commit=commit, repo=str(root), config=str(config), output=output, write=write)


def test_deterministic_bytes_and_receipt(tmp_path: Path) -> None:
    root, config, commit, _ = _fixture(tmp_path)
    first = build(_args(root, config, commit, "out/one.tar.gz", True))
    second = build(_args(root, config, commit, "out/two.tar.gz", True))
    assert (root / "out/one.tar.gz").read_bytes() == (root / "out/two.tar.gz").read_bytes()
    assert first["bundle_sha256"] == second["bundle_sha256"]
    assert first["assets"] == second["assets"]
    with tarfile.open(root / "out/one.tar.gz", "r:gz") as archive:
        assert archive.getnames() == ["aastex701.cls", "figures/figure.pdf", "main.tex"]
        for member in archive.getmembers():
            assert (member.mtime, member.uid, member.gid, member.mode) == (0, 0, 0, 0o644)


def test_dry_run_writes_nothing_and_output_is_repo_confined(tmp_path: Path) -> None:
    root, config, commit, _ = _fixture(tmp_path)
    receipt = build(_args(root, config, commit, "out/dry.tar.gz"))
    assert receipt["dry_run"] is True
    assert not (root / "out/dry.tar.gz").exists()
    with pytest.raises(DepositError, match="escapes repository"):
        build(_args(root, config, commit, "../escape.tar.gz"))


@pytest.mark.parametrize("mutation", ["dirty", "untracked"])
def test_dirty_or_untracked_source_fails_closed(tmp_path: Path, mutation: str) -> None:
    root, config, commit, _ = _fixture(tmp_path)
    if mutation == "dirty":
        (root / "paper/main.tex").write_text("dirty")
    else:
        (root / "paper/new.tex").write_text("new")
        payload = json.loads(config.read_text())
        payload["papers"]["P4"]["bundle_assets"][0]["source"] = "paper/new.tex"
        config.write_text(json.dumps(payload))
        _run(root, "git", "add", "config.json")
        _run(root, "git", "commit", "-qm", "point to untracked source")
        commit = _run(root, "git", "rev-parse", "HEAD")
    with pytest.raises(DepositError, match="differs from commit|not tracked"):
        build(_args(root, config, commit, "out.tar.gz"))


def test_unsafe_tar_member_and_hash_mismatch_fail_closed(tmp_path: Path) -> None:
    root, config, commit, _ = _fixture(tmp_path)
    payload = json.loads(config.read_text())
    extracted = payload["papers"]["P4"]["bundle_tar_members"][0]
    extracted["member"] = "../aastex701.cls"
    config.write_text(json.dumps(payload))
    _run(root, "git", "add", "config.json")
    _run(root, "git", "commit", "-qm", "unsafe config")
    commit = _run(root, "git", "rev-parse", "HEAD")
    with pytest.raises(DepositError, match="unsafe tar member"):
        build(_args(root, config, commit, "unsafe.tar.gz"))

    extracted["member"] = "tex/aastex701.cls"
    extracted["expected_sha256"] = "0" * 64
    config.write_text(json.dumps(payload))
    _run(root, "git", "add", "config.json")
    _run(root, "git", "commit", "-qm", "bad member hash")
    commit = _run(root, "git", "rev-parse", "HEAD")
    with pytest.raises(DepositError, match="tar member hash mismatch"):
        build(_args(root, config, commit, "hash.tar.gz"))


def test_overwrite_refused(tmp_path: Path) -> None:
    root, config, commit, _ = _fixture(tmp_path)
    output = root / "existing.tar.gz"
    output.write_bytes(b"keep me")
    with pytest.raises(DepositError, match="refusing to overwrite"):
        build(_args(root, config, commit, "existing.tar.gz", True))
    assert output.read_bytes() == b"keep me"


def test_direct_cli_execution_loads_sibling_module(tmp_path: Path) -> None:
    root, config, commit, _ = _fixture(tmp_path)
    script = Path(__file__).resolve().parents[1] / "build_exact_arxiv_bundle.py"
    result = subprocess.run(
        [
            "python3", str(script), "--paper", "P4", "--git-commit", commit,
            "--repo", str(root), "--config", str(config), "--output", "cli.tar.gz",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["dry_run"] is True
