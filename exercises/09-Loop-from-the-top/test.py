import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_sample_list
import pytest

@pytest.mark.it('Try looping from the end to the beginning')
def test_loop():
    for i in reversed(my_sample_list):
        print(i)


@pytest.mark.it("other way to flip list in python")
def test_print():
    print(my_sample_list[::-1])