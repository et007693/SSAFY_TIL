# 2806_swea(최소생산비용)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV7GKs06AU0DFAXB&probBoxId=AY4mJz-K_tADFAUZ&type=PROBLEM&problemBoxTitle=240319_%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9_2&problemBoxCnt=4
'''
def queen(y):
    global cnt
    if y == n:
        cnt += 1
        return
    else:
        for x in range(n):
            if check(y, x):
                board[y][x] = 1
                queen(y+1)
                board[y][x] = 0

def check(y, x):
    dy = [-1, -1, -1]
    dx = [0, -1, 1]

    for d in range(3):
        my, mx = y+dy[d], x+dx[d]

        while 0 <= mx < n  and 0 <= my < n:
            if board[my][mx]:
                return False
            my += dy[d]
            mx += dx[d]
    return True

T = int(input())

for tc in range(T):
    n = int(input())
    board = [[0]*n for _ in range(n)]
    cnt = 0
    queen(0)

    print(f'#{tc+1} {cnt}')