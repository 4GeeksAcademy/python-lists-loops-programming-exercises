import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Awesome!!!🤓You have the persons with parameter include")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "['Liam', 'William', 'James', 'Benjamin', 'Amelia', 'Samuel', 'Camila']\n" in captured.out

@pytest.mark.it("Using filter function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("filter") > 0
