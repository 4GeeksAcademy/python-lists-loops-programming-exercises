import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("The output should be as expected")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "20!\n19\n18\n17\n16\n15!\n14\n13\n12\n11\n10!\n9\n8\n7\n6\n5!\n4\n3\n2\n1\nLIFTOFF\n" in captured.out


@pytest.mark.it("Use the while loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        # regex = re.compile(r"while(\s)+[a-zA-Z\-_]+(\s)") only checks for one character before the space.
        regex = re.compile(r"while(\s)\S*")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use an if statement")
def test_if():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"if(\s)")
        assert bool(regex.search(content)) == True

