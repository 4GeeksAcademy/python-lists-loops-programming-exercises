import io
import os
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest

@pytest.mark.it("You have a good list numbers with exclamation sign!!! 😃")
def test_output():
    captured = buffer.getvalue()
    assert "20 !\n19\n18\n17\n16\n15 !\n14\n13\n12\n11\n10 !\n9\n8\n7\n6\n5 !\n4\n3\n2\n1\nLIFTOFF\n" in captured


@pytest.mark.it("Declare the variable and asign the value of 20")
def test_variable():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    assert content.find("20") > 0

@pytest.mark.it("While loop")
def test_while():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    assert content.find("while") > 0


@pytest.mark.it("Conditional statement was declared")
def test_if():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    assert content.find("if") > 0

def test_else():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    assert content.find("else") > 0

@pytest.mark.it("Print the 'LIFTOFF'  to the end")
def test_liftoff():
    f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
    content = f.read()
    assert content.find("LIFTOFF") > 0