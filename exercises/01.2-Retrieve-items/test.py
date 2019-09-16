import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_list
import pytest


@pytest.mark.it('You have to print the 1st element of the list')
def test_output_one():
    print(my_list[0])
    captured = buffer.getvalue()
    assert  "4\n" in captured

@pytest.mark.it('You have to print the 4th element of the list')
def test_output_fourd():
    print(my_list[3])
    captured = buffer.getvalue()
    assert  "43\n" in captured

