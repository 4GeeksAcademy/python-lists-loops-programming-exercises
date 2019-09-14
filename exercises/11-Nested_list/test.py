import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest


@pytest.mark.it("Print the longitudes")
def test_dict():
    captured = buffer.getvalue()
    assert "-112.633853\n-63.987\n-81.901693\n-71.653268\n" in captured

@pytest.mark.it("Loop the all values using for loop")
def test_if_loo():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0


