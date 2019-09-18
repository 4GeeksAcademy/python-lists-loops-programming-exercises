import io
import os
import sys
sys.stdout = buffer.getvalue()


import app.py
import pytest

@pytest.mark.it("")

@pytest.mark.it("")
def test_():
    f = open(os.path.dirname(os.path.abspath(__file__)) +'/app.py')
    content = f.read()
    assert conten.fint()


@pytest.mark.it("")
def test_():
    f = open(os.path.dirname(os.path.abspath(__file__)) +'/app.py')
    content = f.read()
    assert content.find()