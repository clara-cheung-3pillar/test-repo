#!/usr/bin/env python3
"""Tests for main.py"""

# test comment

# new comment

import io
import sys

from main import main


def test_main_prints_hello(capsys):
    """main() should print the expected greeting to stdout."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from test-repo!\n"


def test_main_prints_to_stdout():
    """main() should write only to stdout, not stderr."""
    captured_stdout = io.StringIO()
    sys.stdout = captured_stdout
    try:
        main()
    finally:
        sys.stdout = sys.__stdout__
    assert captured_stdout.getvalue() == "Hello from test-repo!\n"
