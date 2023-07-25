import os
from time import sleep

class Menu:
    """
    The purpose is to create a program that can allow the creation of a menu with buttons.
    1. Create
    2. Insert
    3. Edit
    4. Remove
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
        print("Registration of data.")
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
            if opt == 1:
                print(f"Procedure for {optlist[opt]}")
            if opt == 2:
                print(f"Procedure for {optlist[opt]}")
            if opt == 3:
                print(f"Procedure for {optlist[opt]}")
            if opt == 4:
                print(f"Procedure for {optlist[opt]}")            
            sleep(2)
            return




if __name__ == "__main__":
    listt = ["Create", "Insert", "Edit", "Remove", "End"]
    while True:
        opt = Menu(listt).readvalidate()
        if opt == len(listt):
            break
        else:
            Exop = Executeop(opt, listt)

