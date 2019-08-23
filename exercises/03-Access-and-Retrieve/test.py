import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_Array
import pytest


@pytest.mark.it('Your console have to print the 3rd item from array')
def test_output_good():
    print(my_Array[2])
    captured = buffer.getvalue()
    assert captured == "tuesday\n"

@pytest.mark.it('This value should change to null')
def test_for_change_output():
    assert my_Array[4] is None
