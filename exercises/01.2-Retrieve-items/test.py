import io, sys, pytest


@pytest.mark.it('You have to print the 1st element of the list')
def test_output_one(capsys, app):
    app()
    captured = capsys.readouterr()
    assert  "4\n" in captured.out

@pytest.mark.it('You have to print the 4th element of the list')
def test_output_fourd(capsys, app):
    app()
    captured = capsys.readouterr()
    assert  "43\n" in captured.out

