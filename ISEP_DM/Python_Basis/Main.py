import os
os.chdir("/Users/tiagoreis/PycharmProjects/Python/ISEP_DM/Python_Basis/")
from Utils_1 import solve_quadratic
import Utils_1
import Utils_2


if __name__ == "__main__":
    exmple1 = solve_quadratic(1, 0, -1)
    exmple2 = solve_quadratic(2, 3, 1)
    exmple3 = solve_quadratic(2, 1, -1)
    print(exmple1, exmple2, exmple3)

    number_list = [1, 2, 3, 9.0, 1, 19, 1238, 30, 18, 98, 1, 2.4]
    a = Utils_1.list_biggest(number_list)
    print(a)

    number_list1 = (1, 2, 3, 9.0, 1, 19, 1238, 30, "abc", 18, 98, 1, 2.4)
    b = Utils_1.lower_cut_list(number_list1)
    print(b)
