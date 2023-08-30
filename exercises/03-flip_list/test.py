import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

# @pytest.mark.it('1. You should create a variable named new_list')
# def test_variable_exists(app):
#     try:
#         assert app.new_list
#     except AttributeError:
#         raise AttributeError("The variable 'new_list' should exist on app.py")

# FOR SOME REASON IS NOT WORKING THIS CODE ABOVE

@pytest.mark.it("Flip the entire list")
def test_flip(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "[60, 32, 5, 23, 87, 67, 45]" in captured.out


@pytest.mark.it("The original arr list should not have any values hardcoded into it")
def test_no_hardcoding_on_list():
    with open(path, 'r') as content_file:
        content = content_file.read()
        # Counting the occurrences of this exact string ensures it hasn't been modified.
        occurrences = content.count("arr = [45, 67, 87, 23, 5,  32, 60]")
        assert occurrences == 1

@pytest.mark.it("Do not hard code the solution")
def test_for_hard_output():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\[ *\s*60\s*,\s*32\s*,\s*5\s*,\s*23\s*,\s*87\s*,\s*67\s*,\s*45\s* *\]")
        assert bool(regex.search(content)) == False
