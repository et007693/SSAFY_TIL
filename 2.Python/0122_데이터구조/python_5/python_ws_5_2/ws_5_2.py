def remove_duplicates(origin_list):
    new_lst = list(set(origin_list))
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)