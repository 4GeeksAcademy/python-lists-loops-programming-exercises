import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Print all data types of the list")
def test_multp(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "[<class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'int'>, <class 'int'>]\n" in captured.out

@pytest.mark.it("Use the map function to return the data type")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("map") > 0