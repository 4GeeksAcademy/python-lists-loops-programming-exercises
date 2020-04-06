import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it("Nice work!!! the transformed_data variable is passed")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "['Mario Montes', 'Joe Biden', 'Bill Clon', 'Hilary Mccafee', 'Bobby Mc birth']\n" in captured.out

@pytest.mark.it("Using map function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("map") > 0

@pytest.mark.it("Create the function my_var")
def test_function_exists(app):
    try:
        app.my_var
    except AttributeError:
        raise AttributeError("The function 'my_var' should exist on app.py")

@pytest.mark.it("Create the variable transformedData")
def test_variable_exists(app):
    try:
        app.transformedData
    except AttributeError:
        raise AttributeError("The variable 'transformedData' should exist on app.py")