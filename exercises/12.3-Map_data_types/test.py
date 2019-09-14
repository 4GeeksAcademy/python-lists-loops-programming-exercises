import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest

@pytest.mark.it("Output all data types of the list")
def test_type():
    captured = buffer.getvalue()
    assert "[<class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'int'>, <class 'int'>]\n" in captured


@pytest.mark.it("Use the map function to return the data type")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("map") > 0