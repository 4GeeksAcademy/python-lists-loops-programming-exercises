import io
import sys
sys.stdout = buffer = io.StringIO()



import pytest
import app


@pytest.mark.it("Max integer from the list")
def test_output():
    captured == buffer.getvalue()
    assert "5435\n" in captured