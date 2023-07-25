class ProdPrice:
    """
    A class representing product prices with inflation calculation.

    Attributes:
    - LP (float): The unit price of the product.
    - LP_Stock (float): The number of units in stock for the product.
    - price_inflation (float): The inflation rate to apply for price adjustment.

    Methods:
    - change_prices(): Update the price of the product based on the inflation rate.
    - show_prices(): Display the price and stock value of the product.
    """
    
    def __init__(self, price_inflation: float, LP, LP_Stock) -> None:
        """
        Initialize the ProdPrice object with the given price inflation rate, unit price, and stock.

        Parameters:
        - price_inflation (float): The inflation rate to apply for price adjustment.
        - LP (float): The unit price of the product.
        - LP_Stock (float): The number of units in stock for the product.
        """
        self.LP = LP
        self.LP_Stock = LP_Stock
        self.price_inflation = price_inflation

    # Getters:
    def getLP1(self):
        return self.LP
    def getLP_Stock(self):
        return self.LP_Stock
    def getpriceInflation(self):
        return self.price_inflation

    # Setters:
    def setLP(self, P):
        self.LP = P
    def setLP_Stock(self, S):
        self.LP_Stock = S
    def setpriceInflation(self, I):
        self.price_inflation = I

    def change_prices(self):
        """
        Update the prices of products based on the inflation rate.
        """
        self.LP = self.LP * (1 + (self.price_inflation / 100))

        
    def show_prices(self, P: str):
        """
        Display the price and stock value of the product.

        Parameters:
        - P (str): The product number for display purposes.
        """
        stock_value = self.LP * self.LP_Stock
        print("{} | Price: {:.2f}, Stock: {}, Stock_Value: {:.2f}".format(P, self.LP, self.LP_Stock, stock_value))


  
if __name__ == "__main__":
    # Price increase input from the user:
    price_increase = float(input("What is the inflation rate to apply? "))
    # 
    Prod = (("LP1", 10, 1), ("LP2", 10, 2), ("LP3", 15, 1.5))
    for P in Prod:
        Pr = ProdPrice(price_increase, P[1], P[2])
        Pr.change_prices()
        Pr.show_prices(P[0])
