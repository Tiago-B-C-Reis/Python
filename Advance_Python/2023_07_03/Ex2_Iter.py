# class ImprimeNumero:
#     """
#     """
#     def __init__(self, max: int) -> None:
#         self.max = max
        
#     # metodo iter() dentro de uma classe
#     def __iter__(self):
#         self.num = 0
#         return self


#     # método nex() dentro da classe
#     def __next__(self):
#         if (self.num >= self.max):
#             raise StopAsyncIteration
#         self.num += 1
#         return self.num
    


# if __name__ == "__main__":
#     imprimir_numeros = ImprimeNumero(50)
#     imprimir_numeros = iter(imprimir_numeros)
#     for i in range(50):
#         print(next(imprimir_numeros))


# -------------------------------------------------------

class ImprimeNumero:
    """
    """
    def __init__(self, min: int) -> None:
        self.min = min
        
    # metodo iter() dentro de uma classe
    def __iter__(self):
        self.num = 100
        return self


    # método nex() dentro da classe
    def __next__(self):
        if (self.min >= self.num):
            raise StopAsyncIteration
        self.num -= 1
        return self.num + 1
    


if __name__ == "__main__":
    imprimir_numeros = ImprimeNumero(0)
    imprimir_numeros = iter(imprimir_numeros)
    for i in range(50):
        print(next(imprimir_numeros))

    