import os
from time import sleep
import math

class Menu:
    """
    Areas:
    1. Square/Rectangle
    2. Triangle
    3. Circumference
    4. Trapeze
    5. End
    """

    def __init__(self, optlist) -> None:
        self.options = optlist
    options = []

    def clearscream(self):
        os.system("cls")
        return
    
    def attach(self):
        self.clearscream()
        print("Areas of geometric figures.")
        num = 1
        for i in self.options:
            print(f'{num}.{i}')
            num += 1
    
    def readvalidate(self):
        while True:
            self.attach()
            op = int(input("Insert 1, 2, 3, 4 or 5: "))
            if op<1 or op>5:
                print("Invalid option!")
                sleep(2)
                continue
            else:
                break
        return op



class Executeop:
        """
        """
        def __init__(self, opt, optlist):
            opt -= 1
            if opt == 0:
                print(f"Procedure for {optlist[opt]}")
                side1 = float(input("Insert the dimension of the side 1: "))
                side2 = float(input("Insert the dimension of the side 2: "))
                print(f"The area of the square/rectange = {side1 * side2}")
                sleep(5)
            if opt == 1:
                print(f"Procedure for {optlist[opt]}")
                base = float(input("Insert the dimension of the triangle base: "))
                heigh = float(input("Insert the dimension of the triangle heigh: "))
                print(f"The area of the triangle = {(base/heigh) / 2}")
                sleep(5)
            if opt == 2:
                print(f"Procedure for {optlist[opt]}")
                r = float(input("Insert the circumference radius: "))
                print(f"The area of the circumference = {math.pi * math.pow(r, 2)}")
                sleep(5)
            if opt == 3:
                print(f"Procedure for {optlist[opt]}")
                a = float(input("Insert the trapeze long base: "))
                b = float(input("Insert the trapeze short base: "))
                h = float(input("Insert the trapeze altitude: "))
                print(f"The area of the trapeze = {((a+b)/2) * h}")
                sleep(5)
            if opt == 4:
                print(f"Procedure for {optlist[opt]}")     
                sleep(5)
            return




if __name__ == "__main__":
    listt = ["Square/Rectangle", "Triangle", "Circumference", "Trapeze", "End"]
    while True:
        opt = Menu(listt).readvalidate()
        if opt == len(listt):
            break
        else:
            Exop = Executeop(opt, listt)