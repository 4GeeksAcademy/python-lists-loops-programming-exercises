import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it("The variable `hello` should exist")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"hello")
        assert bool(regex.search(content)) == True


@pytest.mark.it("You have to use a for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to use an if statement")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"if(\s)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to print the value of the variable 'hello' in the console")
def test_all_data_type(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "[[2, 1], {'name': 'juan'}]\n" in captured.out