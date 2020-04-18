import io, sys, pytest, os, random, re

@pytest.mark.it("Import the random package")
def test_import_random():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import(\s)+random")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the for loop to loop 10 times")
def test_for_loop():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)+(\w)+(\s){1,3}in(\s){1,3}range")
        assert bool(regex.search(content)) == True


@pytest.mark.it("Use the randint function to add a radom number to the list each time you loop")
def test_for_randint():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"random\.randint\s*\(\s*\d+\s*,\s*\d+\s*\)")
        assert bool(regex.search(content)) == True


@pytest.mark.it("The list my_list should have 15 items in the end")
def test_for_size():
    from app import my_list
    assert len(my_list) == 15
