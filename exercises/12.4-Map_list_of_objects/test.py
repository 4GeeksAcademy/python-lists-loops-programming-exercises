import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Good job!!😎")
def test_output():
    captured = buffer.getvalue()
    assert "['Hello my name is Joe and I am 32 years old', 'Hello my name is Bob and I am 44 years old', 'Hello my name is Erika and I am 30 years old', 'Hello my name is Dylan and I am 19 years old', 'Hello my name is Steve and I am 16 years old']\n" in captured



@pytest.mark.it("Using map function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("map") > 0