import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest

@pytest.mark.it("Add, change values and reversed list")
def test_output():
    captured = buffer.getvalue()
    assert "Pepe\nBart\nCesco\nFernando\nLou\nMaria\nPedro\nLebron\nRuth\nSteven\nRuthPedro\n" in captured

@pytest.mark.it("Have to loop the entire list")
def test_use_foor():
    captured = buffer.getvalue()

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0