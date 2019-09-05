import io
import sys
sys.stdout = buffer = io.StringIO()

import pytest
import app
import random

@pytest.mark.it("Add ten random numbers to the list")
def test_add_numb():
    assert app.my_list.append(random.randint(1, 10))