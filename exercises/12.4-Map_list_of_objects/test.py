import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Each element needs to have this output: !!😎")
def test_multp(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "['Hello, my name is Joe and I am 33 years old', 'Hello, my name is Bob and I am 44 years old', 'Hello, my name is Erika and I am 30 years old', 'Hello, my name is Dylan and I am 20 years old', 'Hello, my name is Steve and I am 16 years old']\n" in captured.out

@pytest.mark.it("Use the map function ")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("map") > 0



