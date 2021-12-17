import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Add, change values and reversed list")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "Pepe\nBart\nCesco\nFernando\nLou\nMaria\nPedro\nLebron\nRuth\nSteven\nRuthPedro\n" in captured.out

@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)+[a-zA-Z\-_]+(\s)+in(\s)+range.*")
        regex2 = re.compile(r"for(\s)+[a-zA-Z\-_]+(\s)+in(\s)+reversed.*")
        assert bool(regex.search(content)) == True or bool(regex2.search(content)) == True