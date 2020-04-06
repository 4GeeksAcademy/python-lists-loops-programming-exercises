import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Convert Celsius to Fahrenheit and print to console")
def test_dict(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "[28.4, 93.2, 132.8, 14.0]\n" in captured.out

@pytest.mark.it("Use map function")
def test_if_loo():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("map") > 0