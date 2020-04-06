import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Loop two by two")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "3423\n4\n654\n867543\n48\n55\n25\n" in captured.out


@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)+[a-zA-Z\-_]+(\s)+in(\s)+range.*")
        assert bool(regex.search(content)) == True

