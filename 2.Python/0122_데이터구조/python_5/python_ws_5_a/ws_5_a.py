N = 9
data_1 = '123456789'
arr_1 = []
for num in data_1:
    arr_1.append(num)
print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
arr_2 = data_2.split()
for i in arr_2:
    if int(i) % 2 == 1:
        print(i)