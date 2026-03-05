"""
pytest configuration: set required environment variables before check_pr is
imported so the module-level constants don't raise KeyError.
"""

import os
import sys

# Add the pr-processing directory to the path so `import check_pr` works.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# Provide dummy values for all required env vars. Individual tests that care
# about specific values can override them with monkeypatch.
os.environ.setdefault("GITHUB_TOKEN", "test-token")
os.environ.setdefault("REPO", "test-org/test-repo")
os.environ.setdefault("PR_NUMBER", "42")
os.environ.setdefault("PR_BODY", "")
