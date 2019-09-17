import io
import sys
import app
import pytest

import os
# from app import the_last_one
import app


sys.stdout = buffer = io.StringIO()

# @pytest.mark.it("create and assign the value to the variable the_last_one")
# def test_create_assign():
#     assert app.the_last_one is not None


# @pytest.mark.it("print in the console the_last_one")
# def test_output():
#     captured = buffer.getvalue()
#     assert str(app.the_last_one) in captured

@pytest.mark.it("Import random function")
def test_import_random():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("import random") > 0

@pytest.mark.it("Create the variable the_last_one")
def test_create():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("the_last_one") > 0

@pytest.mark.it("Assign the last number to the variable")
def test_assing():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("the_last_one = my_stupid_list[-1]") > 0

@pytest.mark.it("Print the last element")
def test_output():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("print(the_last_one)") > 0