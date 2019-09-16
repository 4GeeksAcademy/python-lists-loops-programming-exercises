import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_sample_list
import pytest
import app
import os

@pytest.mark.it("Loop two by two")
def test_output():
    captured = buffer.getvalue()
    assert "3423\n4\n654\n867543\n48\n55\n25\n" in captured


@pytest.mark.it("The for loop was used")
def test_use_for():
    captured = buffer.getvalue()

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0

