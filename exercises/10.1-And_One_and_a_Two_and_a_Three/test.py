import io
import os
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest


@pytest.mark.it("Print the items in the console")
def test_dict():
    captured = buffer.getvalue()
    assert "fullname : Jane Doe\nphone : 321-321-4321\nemail : test@test.com\n" in captured

@pytest.mark.it("Loop the all  values")
def test_if_loo():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0


