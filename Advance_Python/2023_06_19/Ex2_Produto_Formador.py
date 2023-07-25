class Produto():
    Aumento=0
    def __init__(self, Des, Quant, Pu):
        self.__Des = Des #Descrição
        self.__Quant = Quant #Quantidade
        self.__Pu=Pu #Preço Unitário
        
    @staticmethod
    def AumentoP(Perc):
        Produto.Aumento=Perc #Percentagem de aumento
        return
    
    def ValorProduto(self):
       return self.__Quant*self.__Pu*(1+Produto.Aumento/100)
    
    @staticmethod
    def Cabecalho():
        print(f"{'Designação':^15}{'Valor (€)':^10}")
        return
    
    def Impressao(self):
        print(f"{self.__Des:^15} {self.ValorProduto():^8.2f}")
        return

if  __name__=='__main__':
    Prod=(('LP1', 1, 10),('LP2', 2, 10),('LP3', 1.5, 15))
    Perc=5
    Produto.AumentoP(Perc)
    Produto.Cabecalho()
    for P in Prod:
        Pr=Produto(P[0],P[1],P[2])
        Pr.Impressao()