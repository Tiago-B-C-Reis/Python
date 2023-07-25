# Processo iterativo com sentinela iter()

class triplo:
    def __init__(self) -> None:
        self.inicio = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.inicio *= 3
        return self.inicio
    
    __call__ = __next__




if __name__ == "__main__":
    proc_iter = iter(triplo(), 54)
    for i in proc_iter:
        print(i)