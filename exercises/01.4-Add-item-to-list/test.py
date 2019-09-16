import io
import sys
sys.stdout = buffer = io.StringIO()

import pytest
import app
import os
import random
from app import my_list

@pytest.mark.it("Add ten random numbers to the list")
def test_add_numb():
    assert app.my_list.append(random.randint(1, 100)) is not None

@pytest.mark.it("Output of the list with 15 items numbers")
def test_output():
    captured = buffer.getvalue()
    assert str(app.my_list) in captured

@pytest.mark.it("Import random function")
def test_import_random():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("import random") > 0
