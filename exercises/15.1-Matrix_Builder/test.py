import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

# @pytest.mark.it("Import the random package")
# def test_import_random():
#     with open(path, 'r') as content_file:
#         content = content_file.read()
#         regex = re.compile(r"import(\s)+random")
#         assert bool(regex.search(content)) == True

exp_fn_name = "matrixBuilder"

@pytest.mark.it("You need to print the matrix as output")
def test_output(capsys):
    import app
    out, err = capsys.readouterr()
    assert (
        len(out) > 0 and
        out.startswith("[[") and
        (out.endswith("]]") or out.endswith("]]\n"))
    )

@pytest.mark.it("Create the function matrixBuilder")
def test_function_exists(app):
    if not hasattr(app, exp_fn_name):
        pytest.fail(f"The function {exp_fn_name} should exist on app.py")

@pytest.mark.it("Matrix should only have one's")
def test_oneness(app):
    if hasattr(app, exp_fn_name):
        fn = getattr(app, exp_fn_name)    
        matrix = fn(4)
        for row in matrix:
            for element in row:
                assert element == 1

@pytest.mark.it("Your matrix should be simmetrical")
def test_symmetry(app):
    import random
    side = random.randint(2,10) 
    if hasattr(app, exp_fn_name):
        fn = getattr(app, exp_fn_name) 
        student_matrix = fn(side)
        assert len(student_matrix) == side
        for row in student_matrix:
            assert len(row) == side
