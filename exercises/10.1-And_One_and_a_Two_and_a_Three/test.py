import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Print the items in the console")
def test_dict(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "fullname: Jane Doe\nphone: 321-321-4321\nemail: test@test.com\n" in captured.out

@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True


