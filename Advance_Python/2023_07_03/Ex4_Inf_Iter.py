# Processo de iteração infinita

from itertools import count

# Criar um iterador infinito
iterador_infinito = count(1)

for i in range(5):
    print(next(iterador_infinito))