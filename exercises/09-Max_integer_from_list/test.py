import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it("Max integer from the list")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "5435\n" in captured.out

@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use if statement")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"if(\s)")
        assert bool(regex.search(content)) == True