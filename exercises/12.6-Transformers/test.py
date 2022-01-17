import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("You should create a function named data_transformer")
def test_function_exists(app):
    try:
        app.data_transformer
    except AttributeError:
        raise AttributeError("The function 'data_transformer' should exist on app.py")

@pytest.mark.it('The function named data_transformer should return the correct value')
def test_function_value1(app):
    try:
        incoming_ajax_data = [
	        { "name": 'Mario', "last_name": 'Montes' },
	        { "name": 'Joe', "last_name": 'Biden' },
	        { "name": 'Bill', "last_name": 'Clon' },
	        { "name": 'Hilary', "last_name": 'Mccafee' },
	        { "name": 'Bobby', "last_name": 'Mc birth' }
        ]

        assert app.data_transformer(incoming_ajax_data) == ['Mario Montes', 'Joe Biden', 'Bill Clon', 'Hilary Mccafee', 'Bobby Mc birth']
    except AttributeError:
        raise AttributeError("The variable 'transformed_data' should have the correct value")

@pytest.mark.it('The function named data_transformer should return the correct value (Testing with a different list)')
def test_function_value2(app):
    try:
        incoming_ajax_data = [
	        { "name": 'Donald', "last_name": 'Trump' },
	        { "name": 'Cristiano', "last_name": 'Ronaldo' },
	        { "name": 'Lebron', "last_name": 'James' },
	        { "name": 'Steve', "last_name": 'Jobs' }
        ]

        assert app.data_transformer(incoming_ajax_data) == ['Donald Trump', 'Cristiano Ronaldo', 'Lebron James', 'Steve Jobs']
    except AttributeError:
        raise AttributeError("The variable 'transformed_data' should have the correct value")

@pytest.mark.it("You should use the map method")
def test_map_usage():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert re.search("map\s*\(", content)
