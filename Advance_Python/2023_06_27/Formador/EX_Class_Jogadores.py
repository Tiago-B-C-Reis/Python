"""Uma determinada equipa tem vários jogadores.
Cada jogador é instanciado a partir da classe Jogador
Os atributos de cada jogador são:
    - nome
    - altura
    - peso
Pretende-se completar os métodos da classe Equipa e elaborar
um programa para adicionar jogadores à equipa e imprimir a lista
dos jogadores

Serão solicitados os jogadores até o utilizador pretender sair da inserção de jogadores

IMC (kg/m^2) = peso (kg) / altura^2 (m)

"""

class jogador():
    def __init__(self,nome,altura,peso):
        self.nome=nome
        self.altura=altura
        self.peso=peso
        
    def imprimir(self):
        return self.nome + "----" +str(self.altura)+ "cm ----"+str(self.peso)+"kg"
    
class equipa():
    jogadores=[]
    def __init__(self,n):
        self.nome=n
        
    def adicionar(self):
        nome=input("Nome do Jogador ou SAIR: ")
        while nome.lower()!="sair":
            a=int(input("Altura em cm: "))
            p=int(input("Peso em kg: "))
            J=jogador(nome,a,p)
            self.jogadores.append(J)
            nome=input("Nome do Jogador ou SAIR: ")
            
    def listar(self):
        for J in self.jogadores:
            print(J.imprimir())

if __name__=='__main__':
    E=equipa(("Qual o nome da equipa: "))
    E.adicionar()
    E.listar()
