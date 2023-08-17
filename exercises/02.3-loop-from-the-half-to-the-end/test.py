import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it("Loop from the half to the end")
def test_half_to_end(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "23\n48\n56432\n55\n23\n25\n12\n" in captured.out

@pytest.mark.it("You should not be hardcoding the answer")
def test_hard_code():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\"\s*23\\n48\\n56432\\n55\\n23\\n25\\n12\\n\s*\"")
        assert bool(regex.search(content)) == False

@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)+[a-zA-Z\-_]+(\s)+in(\s)+range.*")
        assert bool(regex.search(content)) == True

@pytest.mark.it("The original my_list should not have any values hardcoded into it")
def test_no_hardcoding():
    with open(path, 'r') as content_file:
        content = content_file.read()
        # Counting the occurrences of this exact string ensures it hasn't been modified.
        occurrences = content.count('my_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]')
        assert occurrences == 1