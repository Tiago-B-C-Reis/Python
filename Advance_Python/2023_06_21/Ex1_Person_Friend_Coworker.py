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
    

class Friend(Person):
    """
    """
    def __init__(self, N: str, P: int, L: str, Y: int) -> None:
        super().__init__(N, P)
        self.__Location = L
        self.__Year = Y
    
    def readLocation(self):
        return self.__Location
    
    def readYear(self):
        return self.__Year
    
    def printF(self):
        print(super().person_print(), self.readLocation(), " -- ", self.readYear())


class Coworker(Person):
    """
    """
    def __init__(self, N: str, P: int, Pr: str, Wp: str) -> None:
        super().__init__(N, P)
        self.__Profession = Pr
        self.__WorkPlace = Wp
    
    def readProfession(self):
        return self.__Profession
    
    def readWorkPlace(self):
        return self.__WorkPlace
    


if __name__ == "__main__":
    F = Friend("Tiago", 92305273, "Porto", 2023)
    C = Coworker("Joana", 912041285, "Dual", "Formadora")
    print(F.read_name(), F.readLocation())
    print(C.read_name(), C.readWorkPlace())
