# 1260_DFS와 BFS
'''
https://www.acmicpc.net/problem/1260
DFS랑 BFS를 모두 연습할 수 있어서 좋았던 문제
아직 DFS에서 재귀 쓰는게 어려운데 문제 많이 풀어봐야 할 것 같다
'''
def dfs(start):
    point = start
    dot_dfs[start] = 1
    print(start, end = ' ')
    for i in node[start]:
        if not dot_dfs[i]:
            dfs(i)

def bfs(start):
    que = [start]
    dot_bfs[start] = 1
    while que:
        point = que.pop(0)
        print(point, end=' ')

        for n in node[point]:
            if dot_bfs[n] != 1:
                que.append(n)
                dot_bfs[n] = 1

n, m, v = map(int, input().split())
node = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for i in node:
    i.sort()

dot_dfs = [0] * (n+1)
dot_bfs = [0] * (n+1)

dfs(v)
print()
bfs(v)