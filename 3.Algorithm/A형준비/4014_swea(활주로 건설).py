# 4014_swea(활주로 건설)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY2i7WQ6i8EDFAXh&contestProbId=AWIeW7FakkUDFAVH&probBoxId=AY3s4YIKB4kDFAUZ&type=PROBLEM&problemBoxTitle=A%ED%98%95_240302&problemBoxCnt=6
'''

dx = [1,0]
dy = [0,1]

def dfs(x, y, height, cnt, slope):
    global result, c, d
    print(x, y, ground[y][x], cnt, slope)

    if (d == 0 and x == n-1) or (d == 1 and y == n-1): # 끝이면 end
        if not slope: # 경사로 진행중이 아니라면
            result += 1
            print('end_point',x,y)
            return
        else:
            print('끝이지만 경사로에서 끝 end')
            return

    h = ground[y][x] # 현재 높이

    if abs(h - height) > 1: # 경사로 차이가 2 이상이면 종료
        print('2차이 end')
        return

    # if slope: # 경사로중일 때
    #     if cnt == c: # 경사로가 끝났다면
    #         slope = False # 경사로 끝 표시
    #         cnt = 0
    #     if h == height: # 이전과 높이가 같다면 계속 진행
    #         dfs(x+dx[d], y+dy[d], h, cnt+1, slope)
    #     elif cnt == 0:
    #         dfs(x+dx[d], y+dy[d], h, cnt+1, slope=True)
    #     else: # 경사로 중에 높이가 다르다면 종료
    #         print('경사로 중 차이 end')
    #         return

    if slope: # 경사로중일 때
        if h == height: # 이전과 높이가 같다면 계속 진행
            dfs(x+dx[d], y+dy[d], h, cnt, slope)
        else: # 경사로 중에 높이가 다르다면
            if c == cnt-1:
                dfs(x + dx[d], y + dy[d], h, cnt=1, slope=True)
            else:
                print('경사로 중 차이 end')
                return

    else: # 경사로가 아니라면
        # 높이가 이전과 다르다면
        if h != height:
            dfs(x+dx[d], y+dy[d], h, cnt + 1, slope=True)
        # 높이가 같다면
        else:
            dfs(x+dx[d], y+dy[d], h, cnt, slope)

T = int(input())

for tc in range(T):
    n, c = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        d = 0
        dfs(0, i, ground[i][0], 0, False)

    for i in range(n):
        d = 1
        dfs(i, 0, ground[0][i], 0, False)

    print(f'#{tc+1} {result}')
