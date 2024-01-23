# 아래 함수를 수정하시오.
def union_sets(*args):
    union_set = set()
    for i in args:
        union_set |= i 

    return union_set

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)