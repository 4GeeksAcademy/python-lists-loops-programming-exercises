import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest

@pytest.mark.it("Odd and even numbers order by values")
def test_odd_even():
    captured = buffer.getvalue()
    assert "[85, 59, 37, 25, 5, 81, 41, 55, 4, 80, 64, 66, 20, 64, 22, 76, 76, 96, 2, 68]\n" in captured

@pytest.mark.it("Looping the list")
def test_for():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0

@pytest.mark.it("Conditional if/else")
def test_if_else():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("if") > 0
    assert content.find("else") > 0