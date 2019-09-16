import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_sample_list
import pytest
import app
import os

@pytest.mark.it("loop from the last")
def test_output():
    captured = buffer.getvalue()
    assert "12\n25\n23\n55\n56432\n48\n23\n867543\n8\n654\n47889\n4\n5\n3423\n" in captured

@pytest.mark.it("Be sure that use the for loop")
def test_use_for():
    captures = buffer.getvalue()

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for ") > 0
