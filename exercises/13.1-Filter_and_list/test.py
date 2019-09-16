import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest


@pytest.mark.it("Cool!!! 🤩 You have names only with 'R' ")
def test_output():
    captured = buffer.getvalue()
    assert "['Romario', 'Roosevelt']\n" in captured

@pytest.mark.it("Using filter function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("filter") > 0