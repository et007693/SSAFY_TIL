def get_value_from_dict(dict, k):
    return dict.get(k)

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice