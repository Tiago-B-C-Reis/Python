class Person:
    """
    """
    def __init__(self, N: str, P: int) -> None:
        self.__Name = N
        self.__Phone = P
    
    def read_name(self):
        return self.__Name
    
    def read_phone(self):
        return self.__Phone
    
    def person_print(self):
        return f"{self.read_name()} -- {self.read_phone()} --"