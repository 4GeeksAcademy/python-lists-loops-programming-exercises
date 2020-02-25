import io, sys, pytest

@pytest.mark.it('Your console have to print the 3rd item from the `list`')
def test_output_one(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "tuesday\n" in captured.out

@pytest.mark.it('Your code have to print the position of step 2')
def test_output_two(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "None\n" in captured.out

@pytest.mark.it('Set the position were thrusday is to None')
def test_position_two():
    from app import my_list
    assert my_list[4] is None