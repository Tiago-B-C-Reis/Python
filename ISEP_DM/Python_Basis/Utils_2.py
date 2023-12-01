import math


## Level I

# 1: ------------------------------------------------------------------------------------------------------------
def cylinder():
    """

    :return:
    """

    radius = input("Please insert the cylinder radius: ")
    height = input("Please input the cylinder height: ")

    volume = math.pi * (radius**2) * height
    print(volume)
    surface_area = 2 * math.pi * radius * height + (2 * math.pi * (radius**2))
    print(surface_area)

# 2: ------------------------------------------------------------------------------------------------------------




## Level II

# 1:
