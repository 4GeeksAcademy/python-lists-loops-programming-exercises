import io
import sys
sys.stdout = buffer = io.StringIO()



import pytest
from app import my_list

@pytest.mark.it("Add ten random numbers")
def test_add_number():
    
