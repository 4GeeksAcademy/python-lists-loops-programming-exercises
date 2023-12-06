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
    assert 'Boom Boom Drop the base Drop the base Boom Boom Boom \nBoom Boom Drop the base Drop the base Drop the base !!!Break the base!!! Boom Boom Boom \nBoom Boom Boom \nDrop the base Boom Drop the base \nDrop the base Drop the base Drop the base !!!Break the base!!! \n' in captured.out




