import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest


@pytest.mark.it("Print the minimum value from the list")
def test_min():
    captured = buffer.getvalue()
    assert "27278.8125\n" in captured

@pytest.mark.it("Use the for loop and len function")
def test_if_loo():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0
    assert content.find("len") > 0