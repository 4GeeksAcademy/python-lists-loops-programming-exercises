import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Print the list of color in the console")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "<ul><li>Red</li><li>Orange</li><li>Pink</li><li>Violet</li></ul>\n" in captured

@pytest.mark.it("Create the function generate_li")
def test_variable_exists(app):
    try:
        app.generate_li
    except AttributeError:
        raise AttributeError("The function 'generate_li' should exist on app.py")
@pytest.mark.it("Create the function filter_colors")
def test_function_exists(app):
    try:
        app.filter_colors
    except AttributeError:
        raise AttributeError("The function 'filter_colors' should exist on app.py")


@pytest.mark.it("Use the filter function")
def test_filter():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("filter")


@pytest.mark.it("Use map function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("map")