import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it("Print the types of items from list")
def test_find(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "<class 'int'>\n<class 'bool'>\n<class 'str'>\n<class 'list'>\n<class 'str'>\n<class 'float'>\n<class 'dict'>\n" in captured.out

@pytest.mark.it("Use the for in loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the type() function")
def test_type():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"type")
        assert bool(regex.search(content)) == True