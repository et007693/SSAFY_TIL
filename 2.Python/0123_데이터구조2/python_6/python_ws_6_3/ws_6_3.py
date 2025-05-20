def intersection_sets(*args):
    intersection_set = args[0]
    for i in args:
        intersection_set &= i

    return intersection_set

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)
