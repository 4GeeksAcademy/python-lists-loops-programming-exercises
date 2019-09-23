import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest


@pytest.mark.it("Print the list of color in the console")
def test_output():
    captured = buffer.getvalue()
    assert "\n" in captured


@pytest.mark.it("Use the filter function")
def test_filter():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("filter")


@pytest.mark.it("Use map function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("map")