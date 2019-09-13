import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest


@pytest.mark.it("Loop from the half to the end")
def test_half_to_end():
    captured = buffer.getvalue()
    assert "23\n48\n56432\n55\n23\n25\n12\n" in captured

@pytest.mark.it("The for loop was used")
def test_use_for():
    captured = buffer.getvalue()

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0