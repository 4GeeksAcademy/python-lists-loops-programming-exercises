import io
import sys
sys.stdout = buffer = io.StringIO()


from app import my_stupid_list
import pytest
import random



@pytest.mark.it("assign a value of my_stupid_list to the_last_one variable")
def test_assignment():




@pytest.mark.it("print the the_last_one variable in the console")
def test_output():
