import io
import sys
import app
import pytest

from app import the_last_one

sys.stdout = buffer = io.StringIO()

@pytest.mark.it("create and assign the value to the variable the_last_one")
def test_create_assign():
    assert app.the_last_one is not None


@pytest.mark.it("print in the console the_last_one")
def test_output():
    captured = buffer.getvalue()
    assert str(app.the_last_one) in captured
