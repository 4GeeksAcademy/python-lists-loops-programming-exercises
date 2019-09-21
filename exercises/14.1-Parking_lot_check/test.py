import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Print the object")
def test_output():
    captured  = buffer.getvalue()
    assert "{'total': 9, 'occupied': 5, 'available': 1}\n" in captured

@pytest.mark.it("Create a get_parking_lot function")
def test_function():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("get_parking_lot") > 0

@pytest.mark.it("Make a for loop")
def test_for():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("for") > 0



@pytest.mark.it("Using conditional statements")
def test_conditional():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find('if') > 0
    assert content.find('elif') > 0

@pytest.mark.it("Push the value into the new variables")
def test_append():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find('append') > 0



