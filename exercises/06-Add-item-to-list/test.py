import io
import sys
sys.stdout = buffer = io.StringIO()

from app import list
import pytest

@pytest.mark.it("add ten random numbers")
def test_random():
    captured = buffer.getvalue()
    assert captured == print(list)
