import io, sys, pytest, os, re

path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('Your console have to print the 3rd item from the `list`')
def test_output_one(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "tuesday\n" in captured.out


@pytest.mark.it('You should not be hard coding any values')
def test_output_one(capsys, app):
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\(\s*(\"|\')\s*[a-zA-Z]*\s*")
        assert bool(regex.search(content)) == False


@pytest.mark.it('Your code have to print the position of step 2')
def test_output_two(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "None\n" in captured.out

@pytest.mark.it('Set the position were thrusday is to None')
def test_position_two():
    from app import my_list
    assert my_list[4] is None