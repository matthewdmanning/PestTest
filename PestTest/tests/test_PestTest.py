"""
Unit and regression test for the PestTest package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import PestTest


def test_PestTest_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "PestTest" in sys.modules
