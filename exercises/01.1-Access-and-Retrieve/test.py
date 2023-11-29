import io, sys, pytest

@pytest.mark.it('Your console has to print the 3rd item from my_list')
def test_output_one(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "tuesday\n" in captured.out

@pytest.mark.it('Your code has to print the fourth position from my_list')
def test_output_two(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "None\n" in captured.out

@pytest.mark.it('Set the value of thursday to None')
def test_position_two():
    from app import my_list
    assert my_list[4] is None
