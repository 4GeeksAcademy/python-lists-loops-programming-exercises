import io, sys, pytest, os, random, re

path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it("Import the random package")
def test_import_random():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"^[^#]*\bimport(\s)+random\b", re.MULTILINE)
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the randint function to add a random number between 1 and 100 to the list")
def test_for_randint():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"random\.randint\s*\(\s*1\s*,\s*100\s*\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("The list my_list should have 10 items in the end")
def test_for_size():
    from app import my_list
    assert len(my_list) == 10

@pytest.mark.it("The original my_list should not have any values hardcoded into it")
def test_no_hardcoding():
    with open(path, 'r') as content_file:
        content = content_file.read()
        # Assuming the original list is provided as 'my_list = [4,5,734,43,45]'
        # Counting the occurrences of this exact string ensures it hasn't been modified.
        occurrences = content.count('my_list = [4,5,734,43,45]')
        assert occurrences == 1