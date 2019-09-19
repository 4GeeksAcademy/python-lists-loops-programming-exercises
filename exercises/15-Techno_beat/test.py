import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app.py
import pytest




@pytest.mark.it("Create a function lyrics_generator")
def test_function():
    f = open(os.path.dirname(os.path.abspath(__file__)) +'/app.py')
    content = f.read()
    assert content.fint("lyrics_generator")


@pytest.mark.it("Use for loop")
def test_for():
    f = open(os.path.dirname(os.path.abspath(__file__)) +'/app.py')
    content = f.read()
    assert content.find("for")

@pytest.mark.it("Use conditionals if/elif/else")
def test_conditinal():
    f = open(os.path.dirname(os.path.abspath(__file__)) +'/app.py')
    content = f.read()
    assert content.find("for")

@pytest.mark.it("Add the value to the new list")
def test_append():
    f = open(os.path.dirname(os.path.abspath(__file__)) +'/app.py')
    content = f.read()
    assert content.find("append")

@pytest.mark.it("Print the strings like song")
def test_output():
    captured = buffer.getvalue()
    assert "\n" in captured




