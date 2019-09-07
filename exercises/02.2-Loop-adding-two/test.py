import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_sample_list
import pytest
import app

@pytest.mark.it("Loop two by two")
def test_output():
    captured = buffer.getvalue()
    assert "3423\n4\n654\n867543\n48\n55\n25\n" in captured

