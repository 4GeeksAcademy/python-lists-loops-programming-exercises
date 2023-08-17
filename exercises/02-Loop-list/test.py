import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Print the all items from the list")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "232\n32\n1\n4\n55\n4\n3\n32\n3\n24\n5\n5\n5\n34\n2\n35\n5365743\n52\n34\n3\n55\n" in captured.out

@pytest.mark.it("You should not be hardcoding the answer")
def test_hard_code():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\"\s*232\\n32\\n1\\n4\\n55\\n4\\n3\\n32\\n3\\n24\\n5\\n5\\n5\\n34\\n2\\n35\\n5365743\\n52\\n34\\n3\\n55\\n\s*\"")
        assert bool(regex.search(content)) == False


@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("The original my_list should not have any values hardcoded into it")
def test_no_hardcoding():
    with open(path, 'r') as content_file:
        content = content_file.read()
        # Counting the occurrences of this exact string ensures it hasn't been modified.
        occurrences = content.count('my_list = [232,32,1,4,55,4,3,32,3,24,5,5,5,34,2,35,5365743,52,34,3,55]')
        assert occurrences == 1