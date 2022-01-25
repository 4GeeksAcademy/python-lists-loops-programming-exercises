import io, sys, os, pytest, re, app
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("The variable 'new_list' should exist")
def test_variable_exists():
    assert app.new_list != None

@pytest.mark.it("The variable 'new_list' value should contain data-types of 'dict' and 'list'")
def test_variable_value():
    assert app.new_list == [[2, 1], {'name': 'juan'}]


@pytest.mark.it("You have to use a for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to use an if statement")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"if(\s)")
        assert bool(regex.search(content)) == True

# @pytest.mark.it("You have to print the value of the variable 'hello' in the console")
# def test_all_data_type(capsys, app):
#     app()
#     captured = capsys.readouterr()
#     assert "[[2, 1], {'name': 'juan'}]\n" in captured.out

@pytest.mark.it("Print the value of the variable 'new_list'")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\(new_list\)")
        assert bool(regex.search(content)) == True