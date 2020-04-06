import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Concatenate both lists. Remember the Odd list come first")
def test_odd_even(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "[[85, 59, 37, 25, 5, 81, 41, 55], [4, 80, 64, 66, 20, 64, 22, 76, 76, 96, 2, 68]]\n" in captured.out

@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use if statement")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"if(\s)")
        assert bool(regex.search(content)) == True

@pytest.mark.it('1. You should create a function named merge_two_list')
def test_variable_exists(app):
    try:
        app.merge_two_list
    except AttributeError:
        raise AttributeError("The function 'merge_two_list' should exist on app.py")