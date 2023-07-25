
# Manipulação de strings:
print("Nesta string será colocada outra %s" %'string')
print("%s string será colocada outra %s" % ('Nesta', 'string'))

num = 15.6
print('Numeros como o %s pode ser convertido a string' % num)

num_1 = 14.7
num_2 = -27.4745624
print('Parte inteira do num_1 = %d e o valor num2 = %f' % (num_1, num_2))
print('Parte inteira do num_1 = %d e o valor num2 = %.2f' % (num_1, num_2))
print('Parte inteira do num_1 = %+d e o valor num2 = %+.2f' % (num_1, num_2))
print('Parte inteira do num_1 = %+i e o valor num2 = %+.2f' % (num_1, num_2))


print("num + num_1 = {}".format(num + num_1))
print("num_1 = {} and num_2 = {}".format(num_1, num_2))

print('{1} string {0} colocado {2}.'.format('Nesta', 'será', 'texto'))

a = 10
b = 20
c = 30
print('Primeiro: {0}; Segundo: {1}; Terceiro: {2}'.format(a, b, c))
print('Primeiro: {a}; Segundo: {b}; Terceiro: {c}'.format(a=12, b=45, c=82))

print('{0:16} | {1:5}'.format('Nome', 'Idade'))
print('{0:15} | {1:5}'.format('Pedro', 30))
print('{0:14} | {1:5}'.format('Carlos', '35'))
print('{1:16} | {0:5}'.format('Francisco', '40'))
print('{0:16} | {1:.0f}'.format('Tony', 28.5))





