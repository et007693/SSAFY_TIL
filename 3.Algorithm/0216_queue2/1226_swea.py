# 1226_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV14vXUqAGMCFAYD&probBoxId=AY2YXC0qjRoDFAXh&type=PROBLEM&problemBoxTitle=240216_Queue_2&problemBoxCnt=3
'''
def bfs(start):
    queue = [start]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        x, y = queue.pop(0)
        maze[y][x] = 1
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < 16 and 0 <= my < 16:
                if maze[my][mx] == 0:
                    queue.append([mx, my])
                elif maze[my][mx] == 3:
                    return 1
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    start = ''

    for y in range(15):
        for x in range(15):
            if int(maze[y][x]) == 2:
                start = (x, y)

    result = bfs(start)
    print(f'#{tc} {result}')