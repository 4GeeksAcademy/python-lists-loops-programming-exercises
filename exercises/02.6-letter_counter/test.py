import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Count letter")
def test_count():
    captured = buffer.getvalue()
    assert "{'L': 1, 'o': 6, 'r': 14, 'e': 18, 'm': 7, ' ': 24, 'i': 18, 'p': 4, 's': 14, 'u': 14, 'd': 4, 'l': 5, 't': 16, 'a': 8, 'c': 9, 'n': 10, 'g': 3, 'C': 2, 'b': 4, 'q': 1, 'v': 1, 'I': 1}\n" in captured



@pytest.mark.it("Use for loop and if statement")
def test_loop():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("for") > 0

def test_if():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("if") > 0