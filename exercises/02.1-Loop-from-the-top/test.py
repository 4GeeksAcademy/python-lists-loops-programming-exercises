import io, sys, pytest, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("loop from the last")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "12\n25\n23\n55\n56432\n48\n23\n867543\n8\n654\n47889\n4\n5\n3423\n" in captured.out

@pytest.mark.it("Be sure that you use the for loop in the exercises")
def test_use_forLoop():

    f = open(path)
    content = f.read()
    assert content.find("for") > 0
