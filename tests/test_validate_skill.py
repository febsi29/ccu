"""Tests for the CCU Assistant repository validator."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_skill import validate_repository

ROOT = Path(__file__).resolve().parents[1]


class ValidateRepositoryTests(unittest.TestCase):
    """Exercise repository validation and safety checks."""

    def test_current_repository_is_valid(self) -> None:
        self.assertEqual(validate_repository(ROOT), [])

    def test_missing_required_file_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            test_root = Path(temporary_directory) / "ccu"
            shutil.copytree(ROOT, test_root)
            (test_root / "SECURITY.md").unlink()

            errors = validate_repository(test_root)

        self.assertIn("Missing required file: SECURITY.md", errors)

    def test_unsafe_credential_instruction_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            test_root = Path(temporary_directory) / "ccu"
            shutil.copytree(ROOT, test_root)
            readme_path = test_root / "README.md"
            readme_path.write_text(
                readme_path.read_text(encoding="utf-8") + "\n給我帳密\n",
                encoding="utf-8",
            )

            errors = validate_repository(test_root)

        self.assertIn("Unsafe credential instruction found: 給我帳密", errors)


if __name__ == "__main__":
    unittest.main()
