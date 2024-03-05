# 2606_bj(바이러스)
'''
https://www.acmicpc.net/problem/2606
'''
# bfs - 시간초과
# def bfs(p):
#     q = [p]
#     while q:
#         p = q.pop(0)
#         node[p] = 1
#         for c in computer:
#             if c[0] == p:
#                 q.append(c[1])

# c = int(input())
# n = int(input())
# computer = [list(map(int, input().split())) for _ in range(n)]
# node = [0]*(c+1)

# bfs(1)
# print(sum(node)-1)

# dfs
def dfs(p):
    node[p] = 1
    for c in computer[p]:
        if node[c] != 1:
            dfs(c)

c = int(input())
n = int(input())

computer = [[] for _ in range(c+1)]
node = [0] * (c+1)

for _ in range(n):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

dfs(1)
print(sum(node)-1)