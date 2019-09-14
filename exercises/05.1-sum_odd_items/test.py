import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest


@pytest.mark.it("Print the odd number")
def test_odd_numbers():
    captured = buffer.getvalue()
    assert "251\n" in captured

@pytest.mark.it("Looping the function")
def test_loop():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0