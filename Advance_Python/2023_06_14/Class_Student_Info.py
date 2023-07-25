import math

class StudentInfo:
    """
    The main purpose of this class is to learn the purpose of use of the 'getters e setters'
    """
    def __init__(self, N, T1, T2) -> None:
        self.name = N
        self.test1 = T1
        self.test2 = T2
    
    def getname(self):
        return self.name
    def setname(self, N):
        self.name = N

    def gettest1(self):
        return self.test1
    def settest1(self, T1):
        self.test1 = T1

    def gettest2(self):
        return self.test2
    def settest2(self, T2):
        self.test2 = T2

    def finalgrade(self):
        return math.floor((self.test1 + self.test2) / 2)
    
    def data_input(self):
        self.setname(input("What is the name? "))
        self.settest1(int(input("What is the 1º grade? ")))
        self.settest2(int(input("What is the 2º grade? ")))
    
    def presentation(self):
        print(f"{'Name':^15}{'Test_1':^10}{'Test_2':^10}{'Final_Grade':^15}")
        print(f"{self.getname():^15}{self.gettest1():^10}{self.gettest2():^10}{self.finalgrade():^15}")

    def finalClassification(self):
        if self.finalgrade() < 10:
            return "Reprovado"
        else:
            return "Aprovado"



# 
if __name__ == "__main__":

    student = StudentInfo("", 0, 0)
    student.data_input()
    student.presentation()
    student.finalClassification()


    # student.setname(input("What is the name? "))
    # student.settest1(int(input("What is the 1º grade? ")))
    # student.settest2(int(input("What is the 2º grade? ")))

    # print(f"The {student.getname()} has had {student.gettest1()} has first grade and {student.gettest2()} has secound grade.")
    # print(f"The {student.getname()} final grade is {student.finalgrade(student.gettest1(), student.gettest2())}")

    # print(f"{'Name':^15}{'Test_1':^10}{'Test_2':^10}{'Final_Grade':^15}")
    # print(f"{student.getname():^15}{student.gettest1():^10}{student.gettest2():^10}{student.finalgrade(student.gettest1(), student.gettest2()):^15}")
