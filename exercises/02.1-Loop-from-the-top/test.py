import io
import sys
sys.stdout = buffer = io.StringIO()

from app import my_sample_list
import pytest
import app

@pytest.mark.it("loop from the last")
def test_output():
    captured = buffer.getvalue()
    assert "12\n25\n23\n55\n56432\n48\n23\n867543\n8\n654\n47889\n4\n5\n3423\n" in captured
