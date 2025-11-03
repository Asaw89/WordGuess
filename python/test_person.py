from person import Person
from person_interface import PersonInterface


class TestPerson:
    """
    Test class for Person implementation.
    
    @author git-leon
    @version 1.0.0
    @date 5/17/21 11:02 AM
    """
    
    @pytest.mark.parametrize("first_name", ["Leon", "Dolio", "Kris", "Desa"])
    def test_set_first_name(self, first_name):
        # given
        expected = first_name
        person = Person()
        person_interface = person  # Python doesn't need explicit casting
        person_interface.set_first_name(expected)
        
        # when
        actual = person_interface.get_first_name()
        
        # then
        assert expected == actual
    
    @pytest.mark.parametrize("last_name", ["Hunter", "Durant", "Younger", "Burton"])
    def test_set_last_name(self, last_name):
        # given
        expected = last_name
        person = Person()
        person_interface = person
        person_interface.set_last_name(expected)
        
        # when
        actual = person_interface.get_last_name()
        
        # then
        assert expected == actual
    
    @pytest.mark.parametrize("age", [28, 40, 50, 45])
    def test_set_age(self, age):
        # given
        expected = age
        person = Person()
        person_interface = person
        person_interface.set_age(expected)
        
        # when
        actual = person_interface.get_age()  # Fixed: was get_last_name() in Java test
        
        # then
        assert expected == actual