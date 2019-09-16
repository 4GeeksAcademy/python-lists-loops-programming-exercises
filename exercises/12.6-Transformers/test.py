import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest


@pytest.mark.it("Nice work!!! the transformed_data variable is passed")
def test_output():
    captured = buffer.getvalue()
    assert "['Mario Montes', 'Joe Biden', 'Bill Clon', 'Hilary Mccafee', 'Bobby Mc birth']\n" in captured

@pytest.mark.it("Using map function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("map") > 0