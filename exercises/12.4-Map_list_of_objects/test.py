import io, sys, pytest, os, re, datetime
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Each element needs to have this output: !!😎")
def test_multp(capsys, app):
    import app
    people = [
        { "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
        { "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
        { "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
        { "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
        { "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
    ]
    def calculateAge(birthDate):
        today = datetime.date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age
    name_list = list(map(lambda person: "Hello, my name is " + person["name"] + " and I am " + str(calculateAge(person["birthDate"])) + " years old"  , people))
    captured = capsys.readouterr()
    assert str(name_list) in captured.out

@pytest.mark.it("Use the map function ")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("map") > 0



