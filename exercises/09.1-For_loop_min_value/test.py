import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function minInteger must exist')
def test_function_existence(capsys, app):
    assert app.minInteger

@pytest.mark.it("The function should return the minimum number from a list")
def test_output(capsys, app):
    result = app.minInteger([43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34])
    assert result == 1
    
@pytest.mark.it("The function should print the minimum number from my_list")
def test_printed_output(capsys, app):
    def minInteger_wrapper(my_list):
        result = app.minInteger(my_list)
        print(result)
        return result

    original_minInteger = app.minInteger
    app.minInteger = minInteger_wrapper

    exec(open(app.__file__).read())
    captured = capsys.readouterr()

    app.minInteger = original_minInteger

    assert int(captured.out.strip()) == min(app.my_list)

@pytest.mark.it("The function should work with other lists")
def test_output_2(capsys, app):
    result = app.minInteger([43,23,6,8733,43,1,4,6,3,67,8,99999,3,7,5435,63])
    assert result == 1

@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use if statement")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"if(\s)")
        assert bool(regex.search(content)) == True