# Gerador Python de iterativo

def minha_funcao(A):
    # Inicializamos o contador
    valor = 0
    # ciclo enquanto o contador for menor que o A
    while valor < A:
        # Criar o valor conrrente do contador
        yield valor
        # Incremento do contador
        valor += 1



for valor in minha_funcao(10):
    print(valor)