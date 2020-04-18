import io, sys, pytest, os, random, re

@pytest.mark.it("Import the random package")
def test_import_random():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import(\s)+random")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the for loop")
def test_for_loop():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)+(\w)+in(\s)+range")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Add the ten random numbers to the list")
def test_add():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("my_list.append(random.randint(1,100))") > 0
