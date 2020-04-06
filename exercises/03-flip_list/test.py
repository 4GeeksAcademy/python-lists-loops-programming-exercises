import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

# @pytest.mark.it('1. You should create a variable named new_list')
# def test_variable_exists(app):
#     try:
#         assert app.new_list
#     except AttributeError:
#         raise AttributeError("The variable 'new_list' should exist on app.py")

# FOR SOME REASON IS NOT WORKING THIS CODE ABOVE

@pytest.mark.it("Flip the entire list")
def test_flip(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "[60, 32, 5, 23, 87, 67, 45]" in captured.out



