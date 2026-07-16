from __future__ import annotations

import hashlib
import json
import subprocess
import tarfile
from argparse import Namespace
from io import BytesIO
from pathlib import Path

import pytest

from tools.prepare_paper_deposit import DepositError, paper_version, prepare, verify_tarball


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_paper_version_accepts_active_versioned_preprint_but_not_comment(tmp_path: Path) -> None:
    tex = tmp_path / "paper.tex"
    tex.write_text("% \\preprint{v0.0.1}\n\\preprint{v1.7.122}\n")
    assert paper_version(tex) == "v1.7.122"

    tex.write_text("% \\preprint{v0.0.1}\n")
    with pytest.raises(DepositError, match="versioned"):
        paper_version(tex)


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
    staging = root / ".deposit-staging" / "P4" / "v1.2.3"
    with pytest.raises(DepositError, match="license decision required"):
        prepare(_args(root, config, commit, write=True))
    assert not staging.exists()


def test_p5_config_is_explicitly_non_release_and_fails_closed() -> None:
    config = json.loads((REPO_ROOT / "tools/paper_deposit_config.json").read_text())
    p5 = config["papers"]["P5"]
    blocker = p5["metadata_blocker"]

    assert p5["metadata_complete"] is False
    assert "Houston manuscript/source license authorization is absent" in blocker
    assert "Paper-IV provenance/completeness gates remain open" in blocker
    assert "license" not in p5["metadata"]
    assert p5["deposit_root"] == ".deposit-staging"
    assert {item["archive_name"] for item in p5["bundle_assets"]} == {
        "p5_desi_chirality.tex",
        "p5_desi_chiralityNotes.bib",
        "fig_p5_vweb_vs_tempel_overlay.png",
        "fig_cw_vs_z.png",
        "fig_z_histogram.png",
        "fig_p5_voids_vs_chirality_skymap.png",
        "fig_p5_cw_vs_density.png",
        "fig_p5_volume_fractions_pie.png",
        "fig_p5_phase2_sensitivity_heatmap.png",
        "fig_p5_cw_by_env_bar.png",
        "fig_p5_healpix_skymap_nside32.png",
    }


def test_p4_config_has_complete_current_standalone_bundle_contract() -> None:
    config = json.loads((REPO_ROOT / "tools/paper_deposit_config.json").read_text())
    p4 = config["papers"]["P4"]
    names = {item["archive_name"] for item in p4["bundle_assets"]}
    names.update(item["archive_name"] for item in p4["bundle_tar_members"])
    assert names == {
        "chirality_catalog_paper.tex",
        "chirality_catalog_paper.bbl",
        "aastex701.cls",
        "fig_raw_vs_eq.png",
        "fig_harmonic_completeness.pdf",
        "fig_class_pie.png",
        "fig_spiral_density.png",
        "fig_confidence_dist.png",
        "fig_sky_map.png",
        "fig_bootstrap_null.png",
        "fig_gallery_cw.png",
        "fig_equivariance_demo.png",
        "fig_gallery_ccw.png",
        "fig_gallery_notspi.png",
        "fig_multipoles.png",
    }
    member = p4["bundle_tar_members"][0]
    assert member["member"] == "./aastex701.cls"
    assert len(member["expected_sha256"]) == 64


def test_p2_config_tracks_exact_v17122_deposit_contract() -> None:
    config = json.loads((REPO_ROOT / "tools/paper_deposit_config.json").read_text())
    p2 = config["papers"]["P2"]
    assert p2["tex"] == "research/focused_paper_source_integration/02_full_draft.tex"
    assert p2["pdf"] == "research/focused_paper_source_integration/02_full_draft.pdf"
    assert p2["standalone_proof"] == (
        "project-context/SSOT/arxiv_tarballs/paper2_arxiv_{version}.proof.json"
    )
    assert p2["tarball_main_tex"] == "02_full_draft.tex"
    assets = {item["archive_name"]: item["source"] for item in p2["bundle_assets"]}
    assert set(assets) == {
        "02_full_draft.tex",
        "focused_paper_refs.bib",
        "fig1_shape_function.png",
        "fig5_inflation_comparison.png",
        "02_full_draft.bbl",
    }
    assert assets["02_full_draft.bbl"].endswith(
        "P2-v1.7.122-CONVENTION-CLARITY-CLOSURE/P2_v1.7.122.bbl"
    )
    assert p2["metadata"]["license"] == "cc-by-4.0"
    assert p2["metadata"]["title"] == (
        "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation "
        "and Conditional Large-Scale-Structure Mapping"
    )
    assert "MegaMapper" not in p2["metadata"]["title"]
    assert "placeholder" not in json.dumps(p2["metadata"]).lower()


def test_p1b_config_is_retention_only_and_fails_closed() -> None:
    config = json.loads((REPO_ROOT / "tools/paper_deposit_config.json").read_text())
    p1b = config["papers"]["P1B"]
    assert p1b["tex"] == "arxiv/paper1b_mcmc_companion.tex"
    assert p1b["pdf"] == "arxiv/paper1b_mcmc_companion.pdf"
    assert p1b["arxiv_tarball"].endswith("_NON_RELEASE.tar.gz")
    assert p1b["standalone_proof"].endswith("_NON_RELEASE.proof.json")
    assert p1b["metadata_complete"] is False
    blocker = p1b["metadata_blocker"]
    assert "NON-RELEASE" in blocker
    assert "physical-spectrum 500-MC" in blocker
    assets = {item["archive_name"] for item in p1b["bundle_assets"]}
    assert assets == {
        "paper1b_mcmc_companion.tex",
        "references.bib",
        "figures/paper1_corner_full_tension.pdf",
        "figures/fig_dneff_viability_two_frozen.pdf",
        "figures/alp_triangle_plot.png",
    }


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
