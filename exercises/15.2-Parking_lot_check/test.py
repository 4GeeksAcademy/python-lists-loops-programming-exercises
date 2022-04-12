import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Create the function get_parking_lot")
def test_variable_exists(app):
    try:
        app.get_parking_lot
    except AttributeError:
        raise AttributeError("The function get_parking_lot should exist on app.py")

@pytest.mark.it('The function get_parking_lot should return an object with correct values')
def test_variable_exists(app):
    value1 = [[1,1,1], [0,0,0], [1,1,2]]
    result1 = {'total_slots': 6, 'available_slots': 1, 'occupied_slots': 5}
    try:
        assert app.get_parking_lot(value1) == result1
    except AttributeError:
        raise AttributeError("The function get_parking_lot should exist on app.py")