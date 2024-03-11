# 4875_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXRHzoUq3XYDFAQT&probBoxId=AY2YXC0qjRcDFAXh&type=USER&problemBoxTitle=240213_Stack2_1&problemBoxCnt=2
'''
T = int(input())
 
def dfs(point):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = [point]
 
    while stack:
        x, y = stack.pop()
        maze[y][x] = 1
        for i in range(4):
            mx = x+dx[i]
            my = y+dy[i]
            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue
            if int(maze[my][mx]) == 0:
                stack.append((mx,my))
            elif int(maze[my][mx]) == 3:
                return 1
    return 0
 
for tc in range(T):
    n = int(input())
    maze = [[1]*n for _ in range(n)]
    start = ''
 
    for i in range(n):
        tmp = input()
        for j in range(n):
            if int(tmp[j]) != 1:
                maze[i][j] = int(tmp[j])
                if int(tmp[j]) == 2:
                    start = (j, i)
 
    result = dfs(start)
    print(f'#{tc+1} {result}')