import io
import sys
import os
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import app

# @pytest.mark.it('Your code needs to print hello on the console')
# def test_for_file_output(capsys):
#     captured = buffer.getvalue()
#     assert captured == "hello\n" #add \n because the console jumps the line on every print

# @pytest.mark.it('Your function needs to print "Hello Inside Function" on the console')
# def test_for_function_output(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello Inside Function\n"

# @pytest.mark.it('Your function needs to return True')
# def test_for_function_return(capsys):
#     assert my_function() == True

@pytest.mark.it("Output 'Hello World'")
def test_output():
    captured = buffer.getvalue()
    assert "Hello World\n" in captured
    # convert everything in the buffer to lower case, captured to lower case


@pytest.mark.it("Use print function")
def test_print():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("print") > 0