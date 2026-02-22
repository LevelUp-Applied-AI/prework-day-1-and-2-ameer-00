"""
PR-0 Autograder — Laptop Verification Evidence Pack

Checks: required files present and non-empty.
No Python execution or script output is tested for PR-0.
"""
import pytest
from pathlib import Path

# Test file lives at tests/test_pr_00_laptop_verify.py in the student repo.
# REPO_ROOT is one level above tests/.
REPO_ROOT = Path(__file__).parent.parent

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}


def test_device_check_md_exists():
    """docs/device-check.md must be present in the repository."""
    target = REPO_ROOT / "docs" / "device-check.md"
    assert target.exists(), (
        "docs/device-check.md not found. "
        "Fill in the template and upload it to docs/ in your repository."
    )


def test_device_check_md_not_empty():
    """docs/device-check.md must contain content (file size > 0 bytes)."""
    target = REPO_ROOT / "docs" / "device-check.md"
    if not target.exists():
        pytest.skip("docs/device-check.md not found — skipping size check")
    assert target.stat().st_size > 0, (
        "docs/device-check.md is empty. Fill in your system specifications."
    )


def test_screenshots_present():
    """At least one screenshot (PNG or JPG) must be present in the repository."""
    images = [
        f for f in REPO_ROOT.rglob("*")
        if f.suffix.lower() in IMAGE_EXTENSIONS
    ]
    assert len(images) >= 1, (
        "No screenshot files found in the repository. "
        "Upload at least one screenshot (.png or .jpg) as evidence of your device specs."
    )
