import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Import the random package")
def test_import_random():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"^[^#]*\bimport(\s)+random\b", re.MULTILINE)
        assert bool(regex.search(content)) == True

@pytest.mark.it("Create the variable the_last_one")
def test_variable_exists(app):
    try:
        app.the_last_one
    except AttributeError:
        raise AttributeError("The variable 'the_last_one' should exist on app.py")

@pytest.mark.it("Assign the last number to the variable")
def test_assing(app):
    assert app.the_last_one == app.my_stupid_list[-1]

@pytest.mark.it("Use the function print")
def test_use_print():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print(\s)*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Print the last element")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert  str(app.my_stupid_list[-1])+"\n" in captured.out