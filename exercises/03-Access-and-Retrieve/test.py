import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_list
import pytest


@pytest.mark.it('Your console have to print the 3rd item from the `list`')
def test_output_good():
    print(my_list[2])
    captured = buffer.getvalue()
    assert captured == "tuesday\n""None\n"

@pytest.mark.it('This value should change to None')
def test_for_change_output():
    assert my_list[4] == "None"

@pytest.mark.it('Your code have to print the position of step 2')
def test_position_output():
    assert my_list[4] == "None"