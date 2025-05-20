def add_item_to_dict(dictionary, k, v):
    new_dict = dictionary.copy()
    add_dict = {k:v}
    new_dict.update(add_dict)

    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
