# 5250_swea(최소 비용)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXx8RCrKU-wDFARs&solveclubId=AY1S2R462h4DFAWX&problemBoxTitle=240321_%EA%B7%B8%EB%9E%98%ED%94%84_2&problemBoxCnt=3&probBoxId=AY4mJ-0q_tQDFAUZ
'''
from collections import deque
T = int(input())
for tc in range(T):
    n = int(input())
    h = [list(map(int, input().split())) for _ in range(n)]

    visited = [[int(1e9)] * n for _ in range(n)]
    visited[0][0] = 0

    q = deque()
    q.append([0,0])
    while q:
        i, j = q.popleft()
        for di, dj in [0, 1], [0, -1], [1, 0], [-1, 0]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                diff = h[ni][nj] - h[i][j] if h[ni][nj] >= h[i][j] else 0
                if visited[ni][nj] > visited[i][j] + diff + 1:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + diff + 1

    print(f'#{tc+1} {visited[n - 1][n - 1]}')
