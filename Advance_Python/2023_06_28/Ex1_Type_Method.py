""" 
class LinguagemTipo(object):
    def __init__(self, lprog) -> None:
        self.lprog = lprog

    def getLtiop(self):
        return self.lprog
    
class PyTipo(LinguagemTipo):
    def Instruções(self):
        return {"print", "input"}

def main():
    InsTipo = PyTipo(lprog= "Python")
    print(InsTipo.getLtiop())
    print(InsTipo.Instruções())

main()
"""

# Meta Class:

def init(self, lprog) -> None:
    self.lprog = lprog

def getItiop(self):
    return self.lprog

def instruções(self):
    return {"print", "input"}


LinguagemTipo = type("LinguagemTipo", (object, ), {"__init__": init, "getItiop": getItiop, })

PyTipo = type("PyTipo", (LinguagemTipo, ), {"instruções": instruções, })


P = PyTipo(lprog = "Python")
print(P.getItiop())
print(P.instruções())


