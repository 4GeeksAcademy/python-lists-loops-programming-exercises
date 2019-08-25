import io
import sys
sys.stdout =  buffer = io.StringIO()

from app import my_list
import pytest

@pytest.mark.it("You have to print the all item from the list")
def test_loop():
    for i in my_list:
        print(i)
