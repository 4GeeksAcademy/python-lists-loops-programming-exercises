import io
import sys
sys.stdout = buffer = io.StringIO()


from app import my_stupid_list
import pytest
import random

@pytest.mark.it("assignt the value and print the last one")
def test_last_one():
