import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("You should only print the tasks that are done")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert  "[{'label': 'Eat my lunch', 'done': True}, {'label': 'Replit the finishes', 'done': True}, {'label': 'Read a book', 'done': True}]\n" in captured.out

@pytest.mark.it("Use the filter function")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"filter")
        assert bool(regex.search(content)) == True
