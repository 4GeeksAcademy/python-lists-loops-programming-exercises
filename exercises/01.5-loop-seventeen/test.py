import io
import sys
sys.stdout = buffer = io.StringIO()
import app



import pytest

@pytest.mark.it("loop from 1 to 17")
def test_add_number():
    captured = buffer.getvalue()
    assert "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n" in captured

