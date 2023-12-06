import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Print all the names as in the output")
def test_multp(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "['My name is: Alice', 'My name is: Bob', 'My name is: Marry', 'My name is: Joe', 'My name is: Hilary', 'My name is: Stevia', 'My name is: Dylan']\n" in captured.out

@pytest.mark.it("Use the map function")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("map") > 0
