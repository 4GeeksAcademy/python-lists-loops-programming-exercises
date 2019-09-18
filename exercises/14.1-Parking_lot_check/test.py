import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Print the object")
def test_output():
    captured  = buffer.getvalue()
    assert "\n" in captured

@pytest.mark.it("Have make a for loop")
def test_for():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("for") > 0



@pytest.mark.it("Using conditional statements")
def test_conditional():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find('if')>0
    assert content.find('elif')


