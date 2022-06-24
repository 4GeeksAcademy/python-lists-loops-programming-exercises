import io, sys, os
import pytest

@pytest.mark.it("Output 'Hello World' case sensitive")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "Hello World\n" == captured.out
    # convert everything in the buffer to lower case, captured to lower case

@pytest.mark.it("Use print function")
def test_print():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("print") >= 0
