# 16268_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AYYlGU56XOkDFARc&probBoxId=AY1andpK_vYDFAWX&type=USER&problemBoxTitle=240202_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B41&problemBoxCnt=9
'''
T = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for tc in range(T):
    n, m = map(int, input().split())  # n = y, m = x
    ballon = []

    for _ in range(n):
        ballon.append(list(map(int, input().split())))

    max_cnt = 0
    for y in range(n):
        for x in range(m):
            cnt = ballon[y][x]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    cnt += ballon[ny][nx]
                if cnt > max_cnt:
                    max_cnt = cnt
    print(f'#{tc+1} {max_cnt}')
