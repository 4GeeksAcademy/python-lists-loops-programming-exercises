import io, sys, pytest, re, os

path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('You have to print the 1st element of the list')
def test_output_one(capsys, app):
    app()
    captured = capsys.readouterr()
    assert  "4\n" in captured.out

@pytest.mark.it('You have to print the 4th element of the list')
def test_output_fourd(capsys, app):
    app()
    captured = capsys.readouterr()
    assert  "43\n" in captured.out

@pytest.mark.it('You should not be hard coding any values')
def test_output_one(capsys, app):
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\(\s*(\"[0-9]*|\'[0-9]*|[0-9]+)\s*")
        assert bool(regex.search(content)) == False

