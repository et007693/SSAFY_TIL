def restructure_word(word, arr):
    for i in word:
        if i.isdecimal():
            for _ in range(int(i)):
                arr.pop(-1)
        else:
            arr.remove(i)

    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
for s in original_word:
    arr.extend(s)
print(arr)

result = restructure_word(word, arr)
print(result)

print(''.join(result))
