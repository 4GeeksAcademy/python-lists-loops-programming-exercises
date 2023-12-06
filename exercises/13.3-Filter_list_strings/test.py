import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("You should only output the names that contain the string 'am'")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "['Liam', 'William', 'James', 'Benjamin', 'Amelia', 'Samuel', 'Camila']\n" in captured.out

@pytest.mark.it("Use the filter function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("filter") > 0
