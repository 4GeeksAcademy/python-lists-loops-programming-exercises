import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Result of multiply by 3")
def test_multp(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "[69, 702, 1035, 13068702, 729, 129, 168, 6]\n" in captured.out

@pytest.mark.it("Use the map() function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("map") > 0

@pytest.mark.it("Create the function increment_by_one")
def test_variable_exists(app):
    try:
        app.increment_by_one
    except AttributeError:
        raise AttributeError("The function 'increment_by_one' should exist on app.py")
        
@pytest.mark.it("Create the variable new_list")
def test_variable_new_list(app):
    try:
        app.new_list
    except AttributeError:
        raise AttributeError("The variable 'new_list' should exist on app.py")

