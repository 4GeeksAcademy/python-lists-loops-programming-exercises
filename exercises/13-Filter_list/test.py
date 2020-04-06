import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Good!!! 😎 Maybe your are smart!!!")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "[23, 12, 35, 54, 21, 534, 23, 42]\n" in captured.out

@pytest.mark.it("Use the filter function")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"filter")
        assert bool(regex.search(content)) == True