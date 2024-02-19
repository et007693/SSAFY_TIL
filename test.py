
# a = [1,5,4,9,6,7]
# n = 6

# 버블정렬
# for i in range(n-1):
#     for j in range(i, n):
#         if a[i] > a[j]:
#             a[i],a[j] = a[j],a[i]
        
# print(a)

# 버블정렬2
# for i in (5, 0, -1):
#     for j in range(i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]

# print(a)



# a = [1,1,1,3,4,5,5,4]

# 선택정렬
# cnt = [0]*(len(a)+1)
# result = [0] * len(a)

# for i in a:
#     cnt[i] += 1

# for i in range(1, len(cnt)):
#     cnt[i] += cnt[i-1]

# for i in range(len(a)-1, 0, -1):
#     cnt[a[i]] -= 1
#     result[cnt[a[i]]] = a[i]

# print(result)

# 부분집합
# a = [1,3,5,7,9]
# arr = []
# cnt = 0

# for i in range(1<<len(a)):
#     tmp = []
#     for j in range(len(a)):
#         if i & (1<<j):
#             tmp.append(a[j])
#     arr.append(tmp)

# for i in arr:
#     if sum(i) == 0:
#         cnt += 1
# print(cnt)

# a = [i for i in range(1, 401)]

# 이진선택(재귀)
# def binary(a, start, end, key):
#     if start > end:
#         return False
#     else:
#         mid = (start + end)//2
#         if key == a[mid]:
#             return True
#         elif key < a[mid]:
#             binary(a, start, mid-1, key)
#         elif key > a[mid]:
#             binary(a, mid+1, end, key)
        
# print(binary(a, 1, 400, 150))

a = [1,5,4,9,6,7]

# 선택정렬
for i in range(len(a)-1):
    min_idx = i
    for j in range(i+1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    a[min_idx], a[i] = a[i], a[min_idx]
    
print(a)
