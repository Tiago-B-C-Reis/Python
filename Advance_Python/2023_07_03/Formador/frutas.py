""" O metodo iter() permite utilizar dados armazenados num dicionário e selecionar dado a dado pr posição"""

frutas=['melancia','morangos','maracuja','melão','pessego','ameixas','ananas','banana','meloa']

frutas_iter=iter(frutas)

print(next(frutas_iter)) #Posição 0 do dicionário
print(next(frutas_iter)) #Posição 1 do dicionário
print(next(frutas_iter)) #Posição 2 do dicionário
print(next(frutas_iter)) #Posição 3 do dicionário
print(next(frutas_iter)) #Posição 4 do dicionário
print(next(frutas_iter)) #Posição 5 do dicionário
print(next(frutas_iter)) #Posição 6 do dicionário
print(next(frutas_iter)) #Posição 7 do dicionário
print(next(frutas_iter)) #Posição 8 do dicionário

