import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest

@pytest.mark.it("Flip entire list")
def test_flip():
    captured = buffer.getvalue()

    assert "[60, 32, 5, 23, 87, 67, 45]" in captured


#test this
@pytest.mark.it("Create new variable")
def test_new_list():
    captured = buffer.getvalue()

    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("new_list") > 0


@pytest.mark.it("Use for loop for flip list")
def test_loop():
    captured = buffer.getvalue()

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0