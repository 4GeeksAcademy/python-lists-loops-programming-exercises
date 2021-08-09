import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("You should add `love` programatically to the dictionary")
def test_love():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    value = False
    if(content.find("spanish_translations['love'] = 'amor'") > 0 or content.find('spanish_translations["love"] = "amor"') > 0):
        value = True
    assert value == True

@pytest.mark.it("You should add `code` programatically to the dictionary")
def test_code():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    value = False
    if(content.find("spanish_translations['code'] = 'codigo'") > 0 or content.find('spanish_translations["code"] = "codigo"') > 0):
        value = True
    assert value == True

@pytest.mark.it("You should add `smart` programatically to the dictionary")
def test_smart():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    value = False
    if(content.find("spanish_translations['smart'] = 'inteligente'") > 0 or content.find('spanish_translations["smart"] = "inteligente"') > 0):
        value = True
    assert value == True

@pytest.mark.it("You should print in the console the dictionary with proper translations")
def test_multp(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "All {'dog': 'perro', 'house': 'casa', 'cat': 'gato', 'love': 'amor', 'code': 'codigo', 'smart': 'inteligente'}" in captured.out