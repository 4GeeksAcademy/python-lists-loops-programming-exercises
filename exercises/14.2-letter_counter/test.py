import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Count all the letters")
def test_count(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "{'l': 6, 'o': 6, 'r': 14, 'e': 18, 'm': 7, 'i': 19, 'p': 4, 's': 14, 'u': 14, 'd': 4, 't': 16, 'a': 8, 'c': 11, 'n': 10, 'g': 3, 'b': 4, 'q': 1, 'v': 1}\n" in captured.out



@pytest.mark.it("Use the for...in loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use an if statement")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"if(\s)")
        assert bool(regex.search(content)) == True
