
""" conta jovem - abertura com valor 0; não permite ter saldos negativos
    conta ordenado - tem um valor minimo de abertura; domiciliação de ordenado, permite saldos negativo"""


class operações_bancárias:
    
    #def __init__(self,quantia):
    #    self.saldo=quantia
    
    def deposito(self,quantia):
        self.saldo=self.saldo+quantia
        return  self.saldo
    
    def consulta(self):
        return self.saldo
    
    def levantamento(self,quantia):
        if self.saldo-quantia >= self.saldo_min:
            self.saldo=self.saldo-quantia
            return self.saldo
        else:
            print('Saldo Insuficiente')
    
class conta_ordenado(operações_bancárias):
        def __init__(self,saldo_inicial,ordenado):
            if saldo_inicial >=ordenado:
                self.saldo=saldo_inicial
                self.saldo_min = -ordenado
            else:
                print('O saldo deve ser maior ou igual ao seu ordenado')

class conta_jovem(operações_bancárias):
    def __init__(self,saldo_inicial):
        self.saldo=saldo_inicial
        self.saldo_min=0

if __name__=='__main__':
    
    tipo_conta=int(input('Escolha o seu tipo de conta: 1-Ordenado, 2-Jovem'))
    
    if tipo_conta==1:
        conta=conta_ordenado(int(input('Qual o saldo?')),int(input('Qual o ordenado?')))
        
    escolha=int(input('Escolha uma das opções: 1-Deposito, 2-Consultas, 3-Levantamentos'))
    
    if escolha ==1:
        print(conta.deposito(int(input('Deposito: '))))
    elif escolha==2:
        print(conta.consulta())
    elif escolha==3:
        print(conta.levantamento(int(input('Quanto pretende levantar? '))))
    else:
        print('Opção inválida')
        