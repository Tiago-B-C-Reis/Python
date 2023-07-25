texto = "Programação em Python"
# print("Python" in texto)

texto1 = "Hoje é vespera de Santo António!"

print(texto1)
a = input("Intruduza a palavra que pretende: ")
if a in texto1:
    print("Palavra presente.")
else:
    print("Palavra ausente.")

c = int(input("c= "))
d = int(input("d= "))

y = lambda a,b : a+b
x = lambda k, j : k*j
print(y(10, 2))

# Decision structure:
if c>d:
    print(y(c, d))
elif c<d:
    print(x(c,d))
else:
    print(y(c, d))
    print(x(c,d))


min = lambda a,b :a if(a<b) else b
print(min(10, 20))

# This lambda function should replace the 'decision structure' above, but using the 'x' and 'y' lambdas functions:
result = (lambda c, d: print(y(c, d)) if c > d else print(x(c, d)) if c < d else (print(y(c, d)), print(x(c, d))))(c, d)

# This lambda does not need the 'x' and 'y' lambda functions above:
result_1 = lambda c,d: (c+d if (c>d) else c*d if (c<d) else (c+d, c*d))
print(result_1(c,d))
# This is another way to do it:
result_2 = (lambda c,d: (print(c+d) if (c>d) else print(c*d) if (c<d) else (print(c+d), print(c*d))))(c,d)
