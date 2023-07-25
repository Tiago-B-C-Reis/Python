class OperaçõesBancarias:
    """
    Esta classe tem apenas a funcção de realizar operações bancarias para as outras 
    duas subclasses ''conta_ordenado' e 'conta_jovem'.
    Depositos, levantamentos e consultas.
    """   
    def deposito(self, quantia):
        self.saldo += quantia
        return self.saldo
    
    def consulta(self):
        return self.saldo
    
    def levantamento(self, quantia):
        if self.saldo - quantia >= self.saldo_min:
            self.saldo -= quantia
            return self.saldo
        else:
            return f"Não tem saldo suficiente para essa transição - Saldo atual: {self.saldo}"


class conta_ordenado(OperaçõesBancarias):
    """
    Conta Ordenado - Tem um valor minimo de abertura; domiciliação do ordenado, permite saldo negativo.
    Depositos, levantamentos e consultas.
    """
    def __init__(self, saldo_inicial, ordenado) -> None:
        if saldo_inicial >= ordenado:
            self.saldo = saldo_inicial
            self.saldo_min = -ordenado
        else:
            print("O saldo deve ser maior ou igual ao seu ordenado!")
    

class conta_jovem(OperaçõesBancarias):
    """
    Conta Jovem - Abertura com valor 0; não permite ter saldos negativos
    """
    def __init__(self, saldo_inicial) -> None:
        self.saldo = saldo_inicial
        self.saldo_min = 0



if __name__ == "__main__":
    tipo_conta = int(input("Escolha uma das seguintes contas:\n 1- Conta ordenado\n 2- Conta jovem\n"))
    
    if tipo_conta == 1:
        co1 = conta_ordenado(int(input("Introduza o deposito inicial: ")), int(input("Introduza o ordenado: ")))
        escolha = int(input("Escolha uma das seguintes opções:\n 1- Deposito\n 2- Consultas\n 3- Levantamentos\n"))
        if escolha == 1:
            print(co1.deposito(int(input("Introduza o valor do deposito: "))))
        elif escolha == 2:
            print(co1.consulta())
        elif escolha == 3:
            print(co1.levantamento(int(input("Introduza o valor a levantar: "))))
        else:
            print("Opção invalida!")
    elif tipo_conta == 2:
        cj1 = conta_jovem(int(input("Introduza o deposito inicial: ")))
        escolha = int(input("Escolha uma das seguintes opções:\n 1- Deposito\n 2- Consultas\n 3- Levantamentos\n"))
        if escolha == 1:
            print(cj1.deposito(int(input("Introduza o valor do deposito: "))))
        elif escolha == 2:
            print(cj1.consulta())
        elif escolha == 3:
            print(cj1.levantamento(int(input("Introduza o valor a levantar: "))))
        else:
            print("Opção invalida!")
    else:
        print("Opção invalida!")


