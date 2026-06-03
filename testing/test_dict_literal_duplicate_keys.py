"""Tests for AST duplicate-key detection in dict literals."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.utils.dict_literal_duplicate_keys import (
    DuplicateKeyFinding,
    find_duplicate_keys_in_file,
    validate_dict_literal_files,
)


class TestFindDuplicateKeysInFile(unittest.TestCase):
    def _findings(self, source: str, stem: str = "sample") -> list[DuplicateKeyFinding]:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / f"{stem}.py"
            path.write_text(source, encoding="utf-8")
            return find_duplicate_keys_in_file(path)

    def test_no_duplicates(self) -> None:
        source = '''
DATA = {
    "UnitA": {
        "ECM": -0.25,
        "CommandPoints": 100,
    },
}
'''
        self.assertEqual(self._findings(source), [])

    def test_nested_duplicate(self) -> None:
        source = '''
DATA = {
    "F16E_CBU_US": {
        "ECM": -0.25,
        "Divisions": {"default": {"cards": 1}},
        "ECM": -0.35,
    },
}
'''
        findings = self._findings(source)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].key_repr, "'ECM'")
        self.assertIn("F16E_CBU_US", findings[0].path)
        self.assertIn("ECM", findings[0].path)

    def test_top_level_duplicate_unit_name(self) -> None:
        source = '''
DATA = {
    "UnitA": {"ECM": 1},
    "UnitA": {"ECM": 2},
}
'''
        findings = self._findings(source)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].key_repr, "'UnitA'")

    def test_tuple_key_duplicate(self) -> None:
        source = '''
NEW_UNITS = {
    ("Donor", 0): {"NewName": "A"},
    ("Donor", 0): {"NewName": "B"},
}
'''
        findings = self._findings(source)
        self.assertEqual(len(findings), 1)
        self.assertIn("Donor", findings[0].key_repr)

    def test_dict_unpack_no_false_positive(self) -> None:
        source = '''
_BASE = {"ECM": -0.1}
DATA = {
    "UnitA": {
        **_BASE,
        "ECM": -0.25,
    },
}
'''
        self.assertEqual(self._findings(source), [])

    def test_duplicate_keys_in_salves_ignored(self) -> None:
        source = '''
DATA = {
    "TankHunters": {
        "WeaponDescriptor": {
            "Salves": {
                "FM_G3": 11,
                "RocketInf_PzF_3T": 4,
                "RocketInf_PzF_3T": 4,
            },
        },
    },
}
'''
        self.assertEqual(self._findings(source), [])

    def test_duplicate_outside_salves_still_reported(self) -> None:
        source = '''
DATA = {
    "UnitA": {
        "WeaponDescriptor": {
            "Salves": {"FM_G3": 1, "FM_G3": 2},
            "turrets": {0: {"Tag": "a"}, 0: {"Tag": "b"}},
        },
    },
}
'''
        findings = self._findings(source)
        self.assertEqual(len(findings), 1)
        self.assertIn("turrets", findings[0].path)

    def test_non_literal_key_skipped_for_duplicate_check(self) -> None:
        source = '''
KEY = "dynamic"
DATA = {
    KEY: {"a": 1},
    "UnitA": {"b": 1, "b": 2},
}
'''
        findings = self._findings(source)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].key_repr, "'b'")


class TestValidateDictLiteralFiles(unittest.TestCase):
    def test_validate_logs_errors_and_returns_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "foo_unit_edits.py"
            path.write_text(
                'DATA = {"U": {"k": 1, "k": 2}}\n',
                encoding="utf-8",
            )
            with patch(
                "src.utils.dict_literal_duplicate_keys.logger",
            ) as mock_logger:
                count = validate_dict_literal_files([path], label="test")
            self.assertEqual(count, 1)
            mock_logger.error.assert_called()
            self.assertTrue(
                any(
                    "duplicate key" in str(call).lower()
                    for call in mock_logger.error.call_args_list
                ),
            )


if __name__ == "__main__":
    unittest.main()
