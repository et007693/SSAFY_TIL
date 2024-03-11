def dfs(s):
    global level
    q = [s]
    visited = [[0]*m for _ in range(n)]
    while q:
        x, y = q.pop()

        for d in [1,0],[-1,0],[0,1],[0,-1]:
            for l in range(1, level+1):
                mx = x + d[0]
                my = y + l * d[1]

                if 0 <= mx < m and 0 <= my < n:
                    if rock[my][mx] != 0 and visited[my][mx] != 1:
                        q.append([mx, my])
                        visited[my][mx] = 1
                    if rock[my][mx] == 3:
                        return
    else:
        level += 1
        dfs(start)

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    rock = []
    level = 1

    for y in range(n):
        rock.append(list(map(int, input().split())))
        for x in range(m):
            if rock[y][x] == 2:
                start = [x, y]
            elif rock[y][x] == 3:
                end = [x,y]

    dfs(start)

    print(f'#{tc+1} {level}')