"""
PR-1 Autograder — Git Identity + Commit Hygiene

Checks: git-setup.md present and non-empty, README.md has required sections,
at least 2 commits on the PR branch relative to main.

Test file lives at tests/test_pr_01_git_setup.py in the student repo.
REPO_ROOT is one level above tests/.
"""
import subprocess
import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def test_git_setup_md_exists():
    """docs/git-setup.md must be present in the repository."""
    target = REPO_ROOT / "docs" / "git-setup.md"
    assert target.exists(), (
        "docs/git-setup.md not found. "
        "Fill in the template and commit it to your branch."
    )


def test_git_setup_md_not_empty():
    """docs/git-setup.md must contain content (file size > 0 bytes)."""
    target = REPO_ROOT / "docs" / "git-setup.md"
    if not target.exists():
        pytest.skip("docs/git-setup.md not found — skipping size check")
    assert target.stat().st_size > 0, (
        "docs/git-setup.md is empty. Fill in your configured identity values."
    )


def test_readme_has_about_section():
    """README.md must contain a ## About section header."""
    readme = REPO_ROOT / "README.md"
    assert readme.exists(), "README.md not found in repository root."
    content = readme.read_text(encoding="utf-8")
    assert "## About" in content, (
        "README.md is missing the '## About' section. "
        "Add a brief paragraph describing who you are and what this repo is for."
    )


def test_readme_has_setup_section():
    """README.md must contain a ## Setup section header."""
    readme = REPO_ROOT / "README.md"
    assert readme.exists(), "README.md not found in repository root."
    content = readme.read_text(encoding="utf-8")
    assert "## Setup" in content, (
        "README.md is missing the '## Setup' section. "
        "Add the commands needed to clone this repo and navigate to it."
    )


def test_at_least_two_commits():
    """The PR branch must have at least 2 commits relative to main."""
    result = subprocess.run(
        ["git", "log", "--oneline", "origin/main..HEAD"],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )
    if result.returncode != 0:
        pytest.skip(
            f"git log failed (returncode {result.returncode}): {result.stderr.strip()}"
        )
    commits = [line for line in result.stdout.strip().splitlines() if line.strip()]
    assert len(commits) >= 2, (
        f"Expected at least 2 commits on this branch, found {len(commits)}. "
        "Make sure you have committed docs/git-setup.md and your README.md update "
        "as separate commits with meaningful messages."
    )
