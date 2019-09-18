import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it("Print the types of items from list")
def test_type_items():
    captured = buffer.getvalue()
    assert "<class 'int'>\n<class 'bool'>\n<class 'str'>\n<class 'list'>\n<class 'str'>\n<class 'float'>\n<class 'dict'>\n" in captured


@pytest.mark.it("Use for loop")
def test_use_for_loop():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for")>0


@pytest.mark.it("Use type() function")
def test_use_type():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("type")>0