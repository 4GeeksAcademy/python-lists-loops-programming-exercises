import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Mergin lists")
def test_merge(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell', 'Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']\n" in captured.out

@pytest.mark.it("Remember to return something in your function")
def test_return():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)+[a-zA-Z\-_]")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True