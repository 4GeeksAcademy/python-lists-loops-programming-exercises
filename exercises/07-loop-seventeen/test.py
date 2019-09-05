import io
import sys
sys.stdout = buffer = io.StringIO()

@pytest.mark.it('Count 1 to 17')
def test_output_one():
    
