
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

# a = [1,5,4,9,6,7]

# # 선택정렬
# for i in range(len(a)-1):
#     min_idx = i
#     for j in range(i+1, len(a)):
#         if a[j] < a[min_idx]:
#             min_idx = j
#     a[min_idx], a[i] = a[i], a[min_idx]
    
# print(a)

# c, r = map(int, input().split())
# k = int(input())
# arr = [[0]*c for _ in range(r)]

# cnt = 0
# line = 1
# dir = 0
# x = 0
# y = r

# while cnt < k:
#     if cnt <= r:
#         y -= 1
#         cnt += 1
#         print(x, y)

#     for _ in range(2):
#         for _ in range(c-line):
#             if dir == 0:
#                 x += 1
#             elif dir == 2:
#                 x -= 1
#             print(x, y)

#             cnt += 1
#         for _ in range(r-line):
#             if dir == 1:
#                 y += 1
#             elif dir == 3:
#                 y -= 1
#             cnt += 1
#             print(x, y)

#         dir = (dir + 1) % 4
#     line += 1
#     print(x, y)


# print(x,y)

# 토끼 경주
# def priority():
#     jump_cnt = [r[2] for r in rabbit]
#     x = [r[3][0] for r in rabbit]
#     y = [r[3][1] for r in rabbit]
#     p_1 = jump_cnt.count(min(jump_cnt))
#     p_3 = x.count(min(x))
#     p_4 = y.count(min(y))
#     if p_1 >= 2:
#         rabbit = sorted(rabbit, key=lambda x=x[2])[:p_1]  # 점프횟수가 같은 토끼
#         x_y = [sum(r[3]) for r in rabbit]  # x_y의 합을 구하고
#         p_2 = x_y.count(min(x_y))  # 합이 작은 토끼 수
#         if p_2 >= 2:
# 
#         else:
#             return rabbit
# 
#     else:
#         return jump_cnt.index(min(jump_cnt))
# 
# 
# Q = int(input())
# 
# q1 = list(map(int, input().split()))
# n = q1[0]  # 맵 가로 크기
# m = q1[1]  # 맵 세로 크기
# p = q1[2]  # 토끼 수
# rabbit = [[] * p]  # 토끼 정보(id, distance, jump_cnt, 현재 위치(x,y), score)
# arr = [[0] * n for _ in ramge(m)]  # 맵(토끼 위치 표시)
# 
# for _ in range(1, p + 1):  # 토끼 수만큼 정보 추가
#     rabbit.append([q1[2 * i + 1], q1[2 * i + 2]])
# 
# for c in range(Q - 1):  # 경기 진행
#     c, i, n = map(int, input().split())
#     if c == 200:
# 
# 
#     elif c == 300:
#         rabbit[i] = n
#     elif c == 400:
#         print(max(score))
# my_list = [1, 2, 3, 4, 5]

# # 딕셔너리를 사용하여 값의 합 저장
# results = {}
# for value in my_list:
#     key = f"cnt_{value}"  # 변수명 생성
#     if key in results:
#         results[key] += value
#     else:
#         results[key] = value

# print("Results:", results)

# 나무 타이쿤
# 나무 타이쿤
n, m = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(n)]
tree = list(reversed(tree))
result = 0

dx = [0, 1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

def plus(x, y):
    # 성장 +1
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < n:
            tree[my][mx] += 1
            tree_bool[my][mx] = 1

def nutrition_cnt(x, y):
    plus(x,y)
    print(tree)
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < n:
            # 대각선 나무만큼 성장
            for x2, y2 in [[-1,1],[-1,-1],[1,1],[1,-1]]:
                mx2 = mx + x2
                my2 = my + y2
                if 0 <= mx2 < n and 0 <= my2 < n and tree[my2][mx2] >= 1:
                    tree_cnt[my2][mx2] += 1

def cut():
    new = []
    # 높이 2 이상 cut
    for y in range(n):
        for x in range(n):
            if tree_bool[y][x] != 1 and tree[y][x] >= 2:
                tree[y][x] -= 2
                nutrition_cnt(x,y)

def nutrition_sum():
    for i in range(n):
        for j in range(n):
            tree[i][j] = tree[i][j] + tree_cnt[i][j]

for _ in range(m):
    tree_bool = [[0] * n for _ in range(n)]
    tree_cnt = [[0] * n for _ in range(n)]

    x, y = 0, 0
    d, p = map(int, input().split())

    x = (x + (p * dx[d])) % n
    y = (y + (p * dy[d])) % n

    # 키우고 -> 대각선 -> 합
    nutrition_cnt(x, y)
    nutrition_sum()
    print(tree)
    tree_cnt = [[0] * n for _ in range(n)]

    # 자르고 영양제
    cut()
    # print(tree)
    nutrition_sum()
    # print(tree)
    tree_cnt = [[0] * n for _ in range(n)]

for t in tree:
    result += sum(t)

print(result)