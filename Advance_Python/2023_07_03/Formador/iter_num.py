
"""class Imprime_numero:
    def __init__(self, max):
        self.max=max

    # método iter() dentro de uma classe
    def __iter__(self):
        self.num = 0
        return self

    # método next() dentro da classe
    def __next__(self):
        if (self.num>=self.max):
            raise StopIteration
        self.num=self.num+1
        return self.num

Imprimir_Numeros=Imprime_numero(100)

Imprime_iter=iter(Imprimir_Numeros)

for i in range (20):
    print(next(Imprime_iter))"""
    
    
    
class Imprime_numero:
    def __init__(self, min):
        self.min=min

    # método iter() dentro de uma classe
    def __iter__(self):
        self.num = 100
        return self

    # método next() dentro da classe
    def __next__(self):
        if (self.minself.num):
            raise StopIteration
        self.num=self.num-1
        return self.num+1

Imprimir_Numeros=Imprime_numero(0)

Imprime_iter=iter(Imprimir_Numeros)

for i in range (200):
    print(next(Imprime_iter))
