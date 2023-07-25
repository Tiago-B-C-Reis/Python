# O metodo iter() permite utilizar dados armazenados num dicionario/lista e selecionar dado a dado por posição


frutas = ["melancia", "Morango", "Maracuja", "Melão", "Pessego", "Ameixa", "Ananás", "Banana", "Meloa"]

frutas_iter = iter(frutas)

print(next(frutas_iter)) # Posição 0 da lista...
print(next(frutas_iter))
print(next(frutas_iter))
print(next(frutas_iter))
print(next(frutas_iter)) # até à posição 4.
