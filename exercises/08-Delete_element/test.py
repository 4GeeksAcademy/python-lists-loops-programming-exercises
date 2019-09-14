import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Delete person")
def test_even():
    captured = buffer.getvalue()
    assert "['juan', 'ana', 'michelle', 'stefany', 'lucy', 'barak']\n['ana', 'michelle', 'daniella', 'stefany', 'lucy', 'barak']\n['juan', 'ana', 'michelle', 'daniella', 'stefany', 'lucy', 'barak']\n" in captured

@pytest.mark.it("Use for loop and if statement")
def test_for_loop():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    assert content.find("for") > 0

def test_if():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    assert content.find("if") > 0