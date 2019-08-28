import io
import sys
sys.stdout = buffer = io.StringIO()


from app import my_stupid_list
import pytest
import random

@pytest.mark.it("assignt the value and print the last one")
def test_last_one():
    my_stupid_list = []
    for i in range(1, 100):
        my_stupid_list.append(random.randint(1,100))
        the_last_one = my_stupid_list[-1]
