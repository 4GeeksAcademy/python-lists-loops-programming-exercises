import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_list
import pytest


@pytest.mark.it('You have to print the 1st element of the list')
def test_output():
    print(my_list[0])
    assert my_list[0] == 4

@pytest.mark.it('You have to print the 4th element of the list')
def test_output_item():
    print(my_list[3])
    assert my_list[3] == 43
