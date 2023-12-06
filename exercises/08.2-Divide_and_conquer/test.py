import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Concatenate both lists. Remember the odd list comes first")
def test_odd_even(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "[85, 59, 37, 25, 5, 81, 41, 55, 4, 80, 64, 66, 20, 64, 22, 76, 76, 96, 2, 68]\n" in captured.out

@pytest.mark.it("Use the for loop")
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

@pytest.mark.it('You should create a function named sort_odd_even')
def test_variable_exists(app):
    try:
        app.sort_odd_even
    except AttributeError:
        raise AttributeError("The function 'sort_odd_even' should exist on app.py")
