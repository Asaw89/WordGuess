from person_interface import PersonInterface


class Person(PersonInterface):
    """Implementation of PersonInterface."""
    
    def __init__(self):
        self._first_name = input("Enter First name  """) #added this and kept everything the same
        self._last_name = input ("Enter Last Name  """)
        self._age = input("Enter Age """)
    
    def get_first_name(self) -> str:
        return self._first_name
    
    def set_first_name(self, first_name: str) -> None:
        self._first_name = first_name
    
    def get_last_name(self) -> str: 
        return self._last_name
    
    def set_last_name(self, last_name: str) -> None:
        self._last_name = last_name
    
    def get_age(self) -> int:
        return self._age
    
    def set_age(self, age: int) -> None:
        self._age = age
    
    def __str__(self) -> str:
        return f"Person(first_name={self._first_name}, last_name={self._last_name}, age={self._age})"
    
   