# 15663_N과 M(9)
'''
https://www.acmicpc.net/problem/15663
백트래킹
'''
def dfs(s):
    if len(s) == m:
        print(*s)
        return

    used = 0
    for i in range(n):
        if not visited[i] and used != arr[i]:
            used = arr[i]
            visited[i] = 1
            dfs(s+[arr[i]])
            visited[i] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * n
path = []
arr.sort()

dfs([])