import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Create the function get_parking_lot")
def test_variable_exists(app):
    try:
        app.get_parking_lot
    except AttributeError:
        raise AttributeError("The function get_parking_lot should exist on app.py")

@pytest.mark.it('The function get_parking_lot should return an object with correct values')
def test_correct_output(app):
    value1 = [[1,1,1], [0,0,0], [1,1,2]]
    result1 = {'total_slots': 6, 'available_slots': 1, 'occupied_slots': 5}
    try:
        assert app.get_parking_lot(value1) == result1
    except AttributeError:
        raise AttributeError("The function get_parking_lot should exist on app.py")

@pytest.mark.it('The function get_parking_lot should return an object with correct values')
def test_different_values(app):
    value1 = [[1,2,1,0], [0,1,0,2], [1,0,1,1]]
    result1 = {'total_slots': 8, 'available_slots': 2, 'occupied_slots': 6}
    try:
        assert app.get_parking_lot(value1) == result1
    except AttributeError:
        raise AttributeError("The function get_parking_lot should exist on app.py")