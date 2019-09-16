import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest


@pytest.mark.it("Good!!! 😎 Maybe your are smart!!!")
def test_output():
    captured = buffer.getvalue()
    assert "[23, 12, 35, 54, 21, 534, 23, 42]\n" in captured

@pytest.mark.it("Using filter function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("filter") > 0