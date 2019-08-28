import io
import sys
sys.stdout =  buffer = io.StringIO()

from app import my_list
import pytest

@pytest.mark.it("You have to print the all items from the list")
def test_loop():
    for num in my_list:
        print(num)

@pytest.mark.it("other way to print the all values of my list")
def test_output():
    for x in range(len(my_list)):
        print(my_list[x])
