import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("The dictionary must have a new key `love`")
def test_count(capsys):
    import app

    if 'love' not in app:
        raise 'The dictionary must have a new key `love`'