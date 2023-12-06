import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("You should add `love` programmatically to the dictionary")
def test_love():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    regex = re.compile(r"spanish_translations\[\s*[\'\"]love[\'\"]\s*\]\s*\=\s*[\'\"]amor[\'\"]")
    assert bool(regex.search(content)) == True

@pytest.mark.it("You should add `code` programmatically to the dictionary")
def test_code():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    regex = re.compile(r"spanish_translations\[\s*[\'\"]code[\'\"]\s*\]\s*\=\s*[\'\"]codigo[\'\"]")
    assert bool(regex.search(content)) == True

@pytest.mark.it("You should add `smart` programmatically to the dictionary")
def test_smart():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    regex = re.compile(r"spanish_translations\[\s*[\'\"]smart[\'\"]\s*\]\s*\=\s*[\'\"]inteligente[\'\"]")
    assert bool(regex.search(content)) == True

@pytest.mark.it("You should print in the console the dictionary with the proper translations")
def test_multp(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "{'dog': 'perro', 'house': 'casa', 'cat': 'gato', 'love': 'amor', 'code': 'codigo', 'smart': 'inteligente'}" in captured.out
