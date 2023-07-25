class product:
    """
    """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
    
    def descount(self, percentage: float) -> float:
        """
        """
        self.price *= (1-(percentage/100))
    
    @property # calls the getter, aka: input filters. On this case, transform my below methods in to a static ones.
    def price(self):
        """
        Getter.
        """
        return self._price
    @price.setter
    def price(self, value):
        """
        Setter.
        """
        if isinstance(value, str):
            value = float(value.replace("€", ""))
        self._price = value

    @property
    def name(self):
        """
        Getter.
        """
        return self._name
    @name.setter
    def name(self, value):
        """
        Setter.
        """
        # self._name = value.upper()
        # self._name = value.title()
        self._name = value.replace("e", "€")




if __name__ == "__main__":
    prod1 = product("RiCe", 1.20)
    prod1.descount(10)
    print(prod1.name, prod1.price)

    prod2 = product("detEeGent", "€20.50")
    prod2.descount(10)
    print(prod2.name, prod2.price)