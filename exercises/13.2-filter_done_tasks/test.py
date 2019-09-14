import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest


@pytest.mark.it("Good job!!! 😃 the True tasks are passed")
def test_output():
    captured = buffer.getvalue()
    assert  "[{'label': 'Eat my lunch', 'done': True}, {'label': 'Replit the finishes', 'done': True}, {'label': 'Read a book', 'done': True}]\n" in captured

@pytest.mark.it("Using filter function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("filter") > 0