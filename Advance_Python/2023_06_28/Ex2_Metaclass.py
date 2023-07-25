# Metaclasses são classes que herdam de forma direta a partir do "type"
# 1. O primeiro argumento é a metaclasse
# 2. O segundo argumento contem o nome da class
# 3. O terceiro argumento é o superclase em forma de tuplo
# 4. O quarto argumento são os atributos da classe em forma de dicionario.


class MetaClass(type):
    """ 
    Uma amostra classica da metaclasse sem funcionalidades atribuidas.
    """
    def __new__(cls, clsnome, superclasse, atributodict):
        print("clsnome", clsnome)
        print("superclasse", superclasse)
        print("atributodict", atributodict)
        return super(MetaClass, cls).__new__(cls, clsnome, superclasse, atributodict)
    

c = MetaClass("c", (object, ), {})
print("class type:", type(c))

class S(object):
    pass
print(type(S))