import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_list
import pytest

@pytest.mark.it('Your console have to print the 3rd item from the `list`')
def test_output_one():
    print(my_list[2])
    captured = buffer.getvalue()
    assert "tuesday\n" in captured

@pytest.mark.it('Your code have to print the position of step 2')
def test_output_two():
    print(my_list[2])
    captured = buffer.getvalue()
    assert "None\n" in captured

@pytest.mark.it('Set index[4] to None')
def test_position_two():
    assert my_list[4] is None