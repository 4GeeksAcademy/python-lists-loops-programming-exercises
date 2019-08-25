import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_sample_list
import pytest

@pytest.mark.it("loop two by two")
def test_loop():
