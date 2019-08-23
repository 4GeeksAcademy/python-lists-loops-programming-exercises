import io
import sys
sys.stdout = buffer = io.StringIO()

from app import arr
import pytest

@pytest.mark.it('You have to print the 1st element of the array')
def test_output():
    assert arr[0] == 4

@pytest.mark.it('You have to print the 4th element of the array')
def test_output_item():
    assert arr[3] == 43
