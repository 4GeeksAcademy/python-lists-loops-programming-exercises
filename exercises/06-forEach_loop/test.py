import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Print the numbers divisible by 14")
def test_even():
    captured = buffer.getvalue()
    assert "434\n56\n56\n56\n" in captured

@pytest.mark.it("Use for loop")
def test_for_loop():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    assert content.find("for") > 0

@pytest.mark.it("Use conditional statement if/elif")
def test_conditional():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    assert content.find("if") > 0