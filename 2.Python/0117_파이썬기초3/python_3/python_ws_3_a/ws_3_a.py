def my_multi(number_1, number_2):
    return number_1 * number_2
result_1 = my_multi(2,3)
print(result_1)

def is_negative(number):
    return True if number <= 0 else False
result_2 = is_negative(3)
print(result_2)

def default_arg_func(default = '기본 값'):
    return default

result_3 = default_arg_func()
result_4 = default_arg_func('다른 값')

print(result_3)
print(result_4)