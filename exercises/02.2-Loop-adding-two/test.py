import io, sys, pytest, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Loop two by two")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "3423\n4\n654\n867543\n48\n55\n25\n" in captured.out


@pytest.mark.it("Be sure that you use the for loop in the exercises")
def test_use_forLoop():

    f = open(path)
    content = f.read()
    assert content.find("for") > 0

