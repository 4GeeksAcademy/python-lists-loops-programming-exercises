import io
import sys
sys.stdout = buffer = io.StringIO()

from app import list
import pytest
import random


@pytest.mark.it("add ten random number to the list")
def test_random():

