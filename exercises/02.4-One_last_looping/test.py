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
        regex = re.compile(r"for(\s*)+\S+(\s*)+in(\s*)+range.*")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to put Steven in the second place in the array.")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"my_sample_list\[\s*1\s*\]\s*\=\s*[\'\"]\s*Steven\s*[\'\"]")
        assert bool(regex.search(content)) == True 

@pytest.mark.it("You have to put Steven in the second place in the array.")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"my_sample_list\[\s*1\s*\]\s*\=\s*[\'\"]\s*Steven\s*[\'\"]")
        assert bool(regex.search(content)) == True 

@pytest.mark.it("Check the third point again")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"my_sample_list\[\s*0\s*\]\s*\=\s*my_sample_list\[\s*2\s*\]\s*\+\s*my_sample_list\[\s*4\s*\]")
        assert bool(regex.search(content)) == True 