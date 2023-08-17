import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Loop from the last to the beginning")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "12\n25\n23\n55\n56432\n48\n23\n867543\n8\n654\n47889\n4\n5\n3423\n" in captured.out
    
@pytest.mark.it("You should not be hardcoding the answer")
def test_hard_code():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\"\s*12\\n25\\n23\\n55\\n56432\\n48\\n23\\n867543\\n8\\n654\\n47889\\n4\\n5\\n3423\\n\s*\"")
        assert bool(regex.search(content)) == False


@pytest.mark.it("Use the while loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"while(\s)+[a-zA-Z\-_]+(\s)")
        assert bool(regex.search(content)) == True
