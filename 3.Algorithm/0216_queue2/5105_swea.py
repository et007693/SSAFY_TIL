# 5105_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXRPDuNKn4kDFAXS&probBoxId=AY2YXC0qjRoDFAXh&type=USER&problemBoxTitle=240216_Queue_2&problemBoxCnt=3
'''
T = int(input())

def bfs(start):
    queue = [start]
    distance = [[0] * n for _ in range(n)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        x, y = queue.pop(0)
        maze[y][x] = 1
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < n:
                distance[my][mx] = distance[y][x] + 1
                if maze[my][mx] == 0:
                    queue.append([mx, my])
                elif maze[my][mx] == 3:
                    return distance[my][mx]-1
    return 0

for tc in range(T):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    start = ''

    for y in range(n):
        for x in range(n):
            if int(maze[y][x]) == 2:
                start = (x, y)

    result = bfs(start)
    print(f'#{tc+1} {result}')