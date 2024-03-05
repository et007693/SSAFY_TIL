# 2805_bj(나무 자르기)
'''
https://www.acmicpc.net/problem/2805
'''
n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    h = (start + end) // 2
    cnt = 0

    for t in tree:
        if t > h:
            cnt += t-h

    if cnt >= m:
        start = h + 1
    else:
        end = h - 1

print(end)