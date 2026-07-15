from __future__ import annotations

import unittest
from pathlib import Path

from tools.paper_registry import CANONICAL_IDS, load_registry


ROOT = Path(__file__).resolve().parents[2]


class DirectiveGAliasRegistryTest(unittest.TestCase):
    def test_every_paper_has_valid_explicit_alias_list(self) -> None:
        registry = load_registry(ROOT)
        self.assertEqual(tuple(registry), CANONICAL_IDS)
        for paper_id, entry in registry.items():
            aliases = entry["served_aliases"]
            self.assertIsInstance(aliases, list, paper_id)
            self.assertEqual(len(aliases), len(set(aliases)), paper_id)
            for alias in aliases:
                self.assertEqual(Path(alias).name, alias)
                self.assertTrue(alias.endswith(".pdf"), alias)

    def test_known_drift_prone_aliases_are_owned(self) -> None:
        registry = load_registry(ROOT)
        self.assertIn("p5-chirality.pdf", registry["P5"]["served_aliases"])
        self.assertIn("p4-chirality.pdf", registry["P4"]["served_aliases"])
        self.assertIn("paper2_fnl_forecast.pdf", registry["P2"]["served_aliases"])

    def test_directive_g_does_not_infer_aliases_by_hashing_all_pdfs(self) -> None:
        script = (ROOT / "tools" / "directive_g.sh").read_text(encoding="utf-8")
        self.assertIn('served_aliases', script)
        self.assertNotIn("find \"$root\" -maxdepth 1 -type f -name '*.pdf'", script)


if __name__ == "__main__":
    unittest.main()
