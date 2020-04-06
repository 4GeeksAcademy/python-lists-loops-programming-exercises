import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Cool!!! 🤩 You have names only with 'R' ")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "['Romario', 'Roosevelt']\n" in captured.out

@pytest.mark.it("Using filter function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("filter") > 0

# @pytest.mark.it("Create the variable resulting_names")
# def test_variable_exists(app):
#     try:
#         app.resulting_names
#     except AttributeError:
#         raise AttributeError("The variable 'resulting_names' should exist on app.py")