import io
import sys
sys.stdout = buffer = io.StringIO()


import os
import pytest
import app

@pytest.mark.it("Output from 1 to 17")
def test_output():
    captured = buffer.getvalue()
    assert "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n" in captured



@pytest.mark.it("Make sure that there is a 'for loop' in your code")
def test_for_loop():
    captured = buffer.getvalue()

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for ") > 0
