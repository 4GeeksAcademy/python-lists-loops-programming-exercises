import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest


@pytest.mark.it("Awesome!!!🤓You have the persons with parameter include")
def test_output():
    captured = buffer.getvalue()
    assert "['Liam', 'William', 'James', 'Benjamin', 'Samuel', 'Camila']\n" in captured

@pytest.mark.it("Using filter function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("filter") > 0