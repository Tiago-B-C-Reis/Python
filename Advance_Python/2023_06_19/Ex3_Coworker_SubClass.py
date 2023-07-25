from Ex3_Person_Class import*


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
    
    # def printF(self):
    #     return f"{super().person_print()} {self.readLocation} -- {self.readYear}"