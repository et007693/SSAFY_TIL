# 1954_swea
'''

'''
T = int(input())
for tc in range(T):
    c = int(input())
    arr = [[0]*c for i in range(c)]

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direction = 0

    arr[0] = ([i for i in range(1, c+1)])
    value = c+1 
    c -= 1

    x = c
    y = 0

    while c > 0:
        for i in range(2):
            for j in range(c):
                x = x + dx[direction]
                y = y + dy[direction]
                arr[y][x] = value
                value += 1
            direction = (direction + 1) % 4
        c -= 1

    print(f'#{tc+1}')
    for i in arr:
        print(*i)