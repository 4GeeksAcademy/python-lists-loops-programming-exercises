import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Cool !!! 😎 You have the all data-type object")
def test_all_data_type():
    captured = buffer.getvalue()
    assert "[[2, 1], {'name': 'juan'}]\n" in captured

@pytest.mark.it("You used to append the return  values to the hello variable, that's very good")
def test_append():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("append") > 0

@pytest.mark.it("The if/elif statement was used")
def test_if():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("if") > 0

def test_elif():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("elif") > 0