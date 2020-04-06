import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Congratulation!!!, that was a nice work")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "['woko', 'wiki', 'woko', 'woko', 'wiki', 'wiki', 'wiki', 'woko', 'woko', 'wiki', 'woko', 'wiki', 'wiki', 'woko', 'woko', 'woko', 'woko', 'woko', 'woko', 'woko', 'woko', 'wiki', 'woko', 'woko', 'woko', 'woko', 'wiki']\n" in captured.out

@pytest.mark.it("Use a map function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("map") > 0

@pytest.mark.it("Use if statement")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"if(\s)")
        assert bool(regex.search(content)) == True


