value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(filter(lambda x: x%2==0, value_list))

cube = map(lambda x: pow(x, 3), value_list)
print(list(cube))