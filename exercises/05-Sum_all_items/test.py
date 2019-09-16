import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Print the sum in the console")
def test_sum():
    captured = buffer.getvalue()
    assert "925960\n" in captured


@pytest.mark.it("Use for loop")
def test_use_loop():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0