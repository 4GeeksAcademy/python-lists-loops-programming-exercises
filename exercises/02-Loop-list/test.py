import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Print all items from the list")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "232\n32\n1\n4\n55\n4\n3\n32\n3\n24\n5\n5\n5\n34\n2\n35\n5365743\n52\n34\n3\n55\n" in captured.out

@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)")
        assert bool(regex.search(content)) == True
