import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Result of multiply by 3")
def test_multp():
    captured = buffer.getvalue()
    assert "[69, 702, 1035, 13068702, 729, 129, 168, 6]\n" in captured

@pytest.mark.it("Use the map() function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("map") > 0



