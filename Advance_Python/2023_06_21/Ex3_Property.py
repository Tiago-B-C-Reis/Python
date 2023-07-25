class Property:
    """
    """
    def __init__(self, ownername, TN) -> None:
        self.__Owner = ownername
        self.__TaxNumber = TN

    @property
    def Owner(self):
        """
        Getter
        """
        return self.__Owner
    @Owner.setter
    def Owner(self, N):
        """
        Setter
        """
        self.__Owner = N
    
    @property
    def TaxNumber(self):
        """
        Getter
        """
        return self.__TaxNumber
    @TaxNumber.setter
    def TaxNumber(self, TN):
        """
        Setter
        """
        self.__TaxNumber = TN



class House(Property):
    """
    Property, TN, Location, Category of energetic efficiency.
    """
    def __init__(self, ownername, TN, L, C) -> None:
        super().__init__(ownername, TN)
        self.__Location = L
        self.__Categ = C
    
    @property
    def Location(self):
        """
        Getter
        """
        return self.__Location
    @Location.setter
    def Location(self, L):
        """
        Setter
        """
        self.__Location = L

    @property
    def Categ(self):
        """
        Getter
        """
        return self.__Categ
    @Categ.setter
    def Categ(self, C):
        """
        Setter
        """
        self.__Categ = C



class Flat(Property):
    """
    Property, TN, Typology, Area
    """
    def __init__(self, ownername, TN, T, A) -> None:
        super().__init__(ownername, TN)
        self.__Typology = T
        self.__Area = A
    
    @property
    def Typology(self):
        """
        Getter
        """
        return self.__Typology
    @Typology.setter
    def Typology(self, T):
        """
        Setter
        """
        self.__Typology = T

    @property
    def Area(self):
        """
        Getter
        """
        return self.__Area
    @Area.setter
    def Area(self, A):
        """
        Setter
        """
        self.__Area = A



if __name__ == "__main__":
    H = House("Artur Silva", 325848551, "Porto", "A+")
    F = Flat("Luis Reis", 129420145, "T4", 150)
    print(H.Owner, H.TaxNumber, H.Location, H.Categ)
    print(F.Owner, F.TaxNumber, F.Typology, F.Area)
