# 13742_swea(정사각형 판정)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AX8BAN1qTwoDFARO&probBoxId=AY3tCHGaCQADFAUZ&type=PROBLEM&problemBoxTitle=IM+%EB%8C%80%EB%B9%84&problemBoxCnt=10
'''
T = int(input())

for tc in range(T):
    n = int(input())
    square = [list(input()) for _ in range(n)]
    start = []
    result = 'yes'

    for y in range(n):
        for x in range(n):
            cnt = 0
            if square[y][x] == '#':
                for i in range(n):
                    dx = x + i
                    dy = y + i
                    if 0 <= dx < n and 0 <= dy < n:
                        if square[dy][dx] == '#':
                            cnt += 1
                        elif square[dy][dx] == '.':
                            break
                start.append([x, y, cnt])

    x, y, cnt = start[0]
    for i in range(x, x+cnt):
        for j in range(y, y+cnt):
            if square[j][i] == '#':
                square[j][i] = '.'
            elif square[j][i] == '.':
                result = 'no'

    for i in square:
        if '#' in i:
            result = 'no'
            break

    print(f'#{tc+1} {result}')