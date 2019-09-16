import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest

@pytest.mark.it("Congratulation!!!, that was a nice work")
def test_output():
    captured = buffer.getvalue()
    assert "['woko', 'wiki', 'woko', 'woko', 'wiki', 'wiki', 'wiki', 'woko', 'woko', 'wiki', 'woko', 'wiki', 'wiki', 'woko', 'woko', 'woko', 'woko', 'woko', 'woko', 'woko', 'woko', 'wiki', 'woko', 'woko', 'woko', 'woko', 'wiki']\n" in captured

@pytest.mark.it("Using map function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("map") > 0

def test_if():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("if") > 0

def test_else():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("else") > 0

