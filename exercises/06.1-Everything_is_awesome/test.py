import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Output the new_list with the new items")
def test_output():
    captured = buffer.getvalue()
    assert "[1, 'Yahoo', 'Yahoo', 'Yahoo', 1, 'Yahoo', 'Yahoo', 'Yahoo', 1, 1]\n" in captured


@pytest.mark.it("Using the conditional statement")
def test_conditional():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    assert content.find("if") > 0
    assert content.find("else") > 0