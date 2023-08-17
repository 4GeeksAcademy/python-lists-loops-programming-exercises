import io, sys, pytest, os, re, app
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The variable "names" should exist.')
def test_variable_exists():
    try:
        app.names
    except AttributeError:
        raise AttributeError('The variable "names" should exist on app.py')

@pytest.mark.it('You have to set the second element of the array to "Steven".')
def test_change_second():
    try:
        assert app.names[1] == "Steven"
    except AttributeError:
        raise AttributeError('The second element of the list "names" should should be "Steven"')

@pytest.mark.it('You have to change the first element of the array to the third + the fifth element.')
def test_change_first():
    try:
        assert app.names[0] == "RuthPedro"
    except AttributeError:
        raise AttributeError('The first element of the list "names" should should be "RuthPedro"')

@pytest.mark.it("You have to use a for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s*)+\S+(\s*)+in(\s*)+range.*")
        assert bool(regex.search(content)) == True

@pytest.mark.it('You should print the list "names" reversed.')
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "Pepe\nBart\nCesco\nFernando\nLou\nMaria\nPedro\nLebron\nRuth\nSteven\nRuthPedro\n" in captured.out

@pytest.mark.it("The original names list should not have any values hardcoded into it")
def test_no_hardcoding():
    with open(path, 'r') as content_file:
        content = content_file.read()
        # Counting the occurrences of this exact string ensures it hasn't been modified.
        occurrences = content.count("names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']")
        assert occurrences == 1