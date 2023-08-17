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