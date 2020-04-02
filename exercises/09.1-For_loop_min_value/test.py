import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Print the minimum value from the list")
def test_min():
    captured = buffer.getvalue()
    assert "23\n" in captured

@pytest.mark.it("Use the for loop and if statemnent")
def test_if_loo():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0
    assert content.find("if") > 0