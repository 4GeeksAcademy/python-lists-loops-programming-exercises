import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Print the updated state ")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "{'total_slots': 6, 'available_slots': 1, 'occupied_slots': 5}\n" in captured.out


@pytest.mark.it("Create the function get_parking_lot")
def test_variable_exists(app):
    try:
        app.get_parking_lot
    except AttributeError:
        raise AttributeError("The function get_parking_lot should exist on app.py")







