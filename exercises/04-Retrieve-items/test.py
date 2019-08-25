import io
import sys
sys.stdout = buffer = io.StringIO()

from app import list
import pytest


@pytest.mark.it('You have to print the 1st element of the list')
def test_output():
    assert list[0] == 4

@pytest.mark.it('You have to print the 4th element of the list')
def test_output_item():
    assert list[3] == 43
