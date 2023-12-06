import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it("Create the function lyrics_generator")
def test_variable_exists(app):
    try:
        app.lyrics_generator
    except AttributeError:
        raise AttributeError("The function lyrics_generator should exist on app.py")


@pytest.mark.it("Print the expected strings")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert 'Boom Boom Drop the bass Drop the bass Boom Boom Boom \nBoom Boom Drop the bass Drop the bass Drop the bass !!!Break the bass!!! Boom Boom Boom \nBoom Boom Boom \nDrop the bass Boom Drop the bass \nDrop the bass Drop the bass Drop the bass !!!Break the bass!!! \n' in captured.out
