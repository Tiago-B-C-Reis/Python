class Conta:
    """
    Depositos, levantamentos e consultas
    """
    def __init__(self, quantia) -> None:
        self.saldo = quantia
    
    def deposito(self, quantia):
        self.saldo += quantia
        return self.saldo
    
    def consulta(self):
        return self.saldo
    
    def levantamento(self, quantia):
        if self.saldo - quantia >= 0:
            self.saldo -= quantia
            return self.saldo
        else:
            return f"Não tem saldo suficiente para essa transição - Saldo atual: {self.saldo}"



def cria_conta(saldo):
    return Conta(saldo)

def consulta(c):
    return c.consulta()

def deposito(c, q):
    return c.deposito(q)

def levantamento(c, q):
    return c.levantamento(q)