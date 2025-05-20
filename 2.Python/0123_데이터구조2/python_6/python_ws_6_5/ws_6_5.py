def difference_sets(*args):
    return args[0] - args[1]

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
