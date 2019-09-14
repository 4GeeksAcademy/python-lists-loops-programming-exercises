import io
import os
import sys
sys.stdout = buffer = io.StringIO()



import pytest
import app


@pytest.mark.it("Max integer from the list")
def test_output():
    captured = buffer.getvalue()
    assert "5435\n" in captured

@pytest.mark.it("Use for loop and if statement")
def test_loo_if():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0
    assert content.find("if") > 0