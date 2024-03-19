# 5209_swea(최소생산비용)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXIV0ii63u4DFAXR&probBoxId=AY4mJz-K_tADFAUZ&type=USER&problemBoxTitle=240319_%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9_2&problemBoxCnt=4
'''
def factory(y, s):
    global result
    if y == n:
        if s < result:
            result = s
        return
    if result < s + (n-y)*verify:
        return

    tmp = 0
    for x in range(n):
        if not used[x]:
            used[x] = 1
            factory(y+1, s+cost[y][x])
            used[x] = 0

T = int(input())

for tc in range(T):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    verify = min(min(*cost))
    used = [0]*n
    result = 99*n

    factory(0,0)
    print(f'#{tc+1} {result}')