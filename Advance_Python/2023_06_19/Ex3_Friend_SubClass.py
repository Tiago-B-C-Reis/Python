from Ex3_Person_Class import*


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