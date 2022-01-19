import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("You should add `love` programatically to the dictionary")
def test_love():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    regex = re.compile(r"spanish_translations\[\s*[\'\"]\s*love\s*[\'\"]\s*\]\s*\=\s*[\'\"]\s*amor\s*[\'\"]")
    assert bool(regex.search(content)) == True

@pytest.mark.it("You should add `code` programatically to the dictionary")
def test_code():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    regex = re.compile(r"spanish_translations\[\s*[\'\"]\s*code\s*[\'\"]\s*\]\s*\=\s*[\'\"]\s*codigo\s*[\'\"]")
    assert bool(regex.search(content)) == True

@pytest.mark.it("You should add `smart` programatically to the dictionary")
def test_smart():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    regex = re.compile(r"spanish_translations\[\s*[\'\"]\s*smart\s*[\'\"]\s*\]\s*\=\s*[\'\"]\s*inteligente\s*[\'\"]")
    assert bool(regex.search(content)) == True

@pytest.mark.it("You should print in the console the dictionary with proper translations")
def test_multp(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "{'dog': 'perro', 'house': 'casa', 'cat': 'gato', 'love': 'amor', 'code': 'codigo', 'smart': 'inteligente'}" in captured.out