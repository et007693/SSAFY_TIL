data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
for s in data_1:
    if s.isupper() or s == ' ':
        print(s, end = '')
print()

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
need_to_find = ['내','힘','들','다']
arr = []
for s in need_to_find:
    arr.append(data_2.find(s))
print(arr)
print(sorted(arr))

for n in sorted(arr):
    print(data_2[n], end = '')