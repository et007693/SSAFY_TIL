def even_elements(origin_list):
    new_list = []
    for num in origin_list:
        if num %2 == 0:
            new_list.extend([origin_list.pop(origin_list.index(num))])
            
    return new_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
