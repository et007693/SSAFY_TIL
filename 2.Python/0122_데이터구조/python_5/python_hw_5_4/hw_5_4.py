# 아래 함수를 수정하시오.
def find_min_max(origin_list):
    max_num = 0
    min_num = origin_list[0]
    for i in origin_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
            
    return min_num, max_num

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
