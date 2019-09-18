import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app.py
import pytest

@pytest.mark.it("")
def test_():
    captured = buffer.getvalue()
    assert "\n" in captured

@pytest.mark.it("")
def test_():
    f = open(os.path.dirname(os.path.abspath(__file__)) +'/app.py')
    content = f.read()
    assert content.fint()


@pytest.mark.it("")
def test_():
    f = open(os.path.dirname(os.path.abspath(__file__)) +'/app.py')
    content = f.read()
    assert content.find()