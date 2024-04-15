# 1520_bj(내리막 길)
'''
https://www.acmicpc.net/problem/1520
dp
visited를 -1로 설정

'''
def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for dx, dy in [1, 0], [-1, 0], [0, 1], [0, -1]:
        mx = x + dx
        my = y + dy
        if 0 <= mx < n and 0 <= my < m and hill[y][x] > hill[my][mx]:
            dp[y][x] += dfs(mx, my)

    return dp[y][x]

m, n = map(int, input().split())
hill = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]

print(dfs(0, 0))