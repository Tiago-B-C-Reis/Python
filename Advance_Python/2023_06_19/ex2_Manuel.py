class Produto():
  def __init__(self, Name, Qt, Price):
        self.__name = Name
        self.__qt = Qt
        self.__price = Price


  def ReadPr(self):
    return f"{self.__price:>2.2f}"

  def aumento(self, Value):
    self.__price *= (1+Value/100)
    return self.__price

  def showProd(self):
    return float(self.ReadPr())*self.__qt

  def showRecipe(self):
    return self.showProd() * self.__qt

if __name__ == "__main__":
    product = Produto('Lp1', 1, 10)
    product.aumento(5)
    print(product.showProd())

    product2 = Produto('Lp2', 2, 10)
    product2.aumento(2)
    print(product2.showProd())

    product3 = Produto('Lp3', 1.5, 15)
    product3.aumento(5)
    print(product3.showProd())

    product3.showRecipe()