import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

# @pytest.mark.it("Import the random package")
# def test_import_random():
#     with open(path, 'r') as content_file:
#         content = content_file.read()
#         regex = re.compile(r"import(\s)+random")
#         assert bool(regex.search(content)) == True

@pytest.mark.it("You need to build the matrix as the output")
def test_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert  "[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]\n" in captured.out

# @pytest.mark.it("Create the function matrixBuilder")
# def test_function_exists(app):
#     try:
#         app.matrixBuilder
#     except AttributeError:
#         raise AttributeError("The function 'matrixBuilder' should exist on app.py")