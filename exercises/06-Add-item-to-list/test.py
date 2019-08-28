import io
import sys
sys.stdout = buffer = io.StringIO()

from app import list
import pytest
import random


@pytest.mark.it("add ten random number to the list")
def test_random():
    for i in range(1, 11):
        list.append(random.randint(1, 10))
print(list)
