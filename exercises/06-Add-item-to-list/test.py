import io
import sys
sys.stdout = buffer = io.StringIO()

from app import list
import pytest

@pytest.mark.it("add ten random numbers to the list")
def test_add_random():
assert == list

@pytest.mark.it("print in the console the list with random numbers")
def test_output_list():
    captured = buffer.getvalue
    assert captured == print(list)
