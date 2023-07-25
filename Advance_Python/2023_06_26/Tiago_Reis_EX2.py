class ProdPrice:
    
    Inflation = 0
    def __init__(self, Des: float, PStock: float, UnitP: float) -> None:
        self.Des = Des # Product Description
        self.PStock = PStock # Existing Stock
        self.UnitP = UnitP # Unit Price

    @staticmethod
    def PIncrease(price_increase: float):
        ProdPrice.Inflation = price_increase # Infation Rate on the product.
        return
    
    def ProductValue(self):
       return self.PStock * self.UnitP * (1 + (ProdPrice.Inflation / 100))
    
    @staticmethod
    def Header():
        print(f"{'Designation':^15}{'Value (€)':^10}")
        return
    
    def Printing(self):
        print(f'{self.Des:^15} {self.ProductValue():^8.2f}')
        return

  
if __name__ == '__main__':
    Prod = (('LP1', 1, 10),('LP2', 2, 10),('LP3', 1.5, 15))
    price_increase = 5
    ProdPrice.PIncrease(price_increase)
    ProdPrice.Header()
    for P in Prod:
        Pr=ProdPrice(P[0],P[1],P[2])
        Pr.Printing()