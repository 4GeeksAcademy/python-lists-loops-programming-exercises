import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest

@pytest.mark.it("Create a function lyrics_generator")
def test_function():
    f = open(os.path.dirname(os.path.abspath(__file__)) +'/app.py')
    content = f.read()
    assert content.find("lyrics_generator")


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

@pytest.mark.it("Store the value in the variable that you have to return")
def test_append():
    f = open(os.path.dirname(os.path.abspath(__file__)) +'/app.py')
    content = f.read()
    assert content.find("append")

@pytest.mark.it("Print the strings like song")
def test_output():
    captured = buffer.getvalue()
    assert "['boom', 'boom', 'Drop the base', 'Drop the base', 'boom', 'boom', 'boom']\n['boom', 'boom', 'Drop the base', 'Drop the base', 'Drop the base', '!!!Break the base', 'boom', 'boom', 'boom']\n['boom', 'boom', 'boom']\n['Drop the base', 'boom', 'Drop the base']\n['Drop the base', 'Drop the base', 'Drop the base', '!!!Break the base']\n" in captured




