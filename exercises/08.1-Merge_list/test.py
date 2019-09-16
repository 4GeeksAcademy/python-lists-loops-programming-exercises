import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Mergin lists")
def test_merge():
    captured = buffer.getvalue()
    assert "['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell', 'Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']\n" in captured

@pytest.mark.it("Use looping and return the new list")
def test_loop():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0
    assert content.find("return") > 0