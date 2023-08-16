import io, sys, os, pytest, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it("Use the for loop")
def test_for_loop():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"for(\s)+[a-zA-Z\-_]+(\s)+in(\s)+range.*")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You should not be hardcoding the answer")
def test_hard_code():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\"\s*1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9\\n10\\n11\\n12\\n13\\n14\\n15\\n16\\n17\\n\s*\"")
        assert bool(regex.search(content)) == False

@pytest.mark.it("Use the function print once inside your loop")
def test_use_print():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print(\s)*\(")
        assert bool(regex.search(content)) == True


@pytest.mark.it("Print on the console from 1 to 17 (do not print 0)")
def test_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n" in captured.out