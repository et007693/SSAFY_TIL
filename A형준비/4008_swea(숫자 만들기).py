# 4008_swea(숫자 만들기)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY2i7WQ6i8EDFAXh&contestProbId=AWIeRZV6kBUDFAVH&probBoxId=AY3s4YIKB4kDFAUZ&type=PROBLEM&problemBoxTitle=A%ED%98%95_240302&problemBoxCnt=6
dfs 응용 문제
dfs 응용 방법 이해를 조금 더 해야 될 것 같다
'''
def dfs(i, a, b, c, d, cal):
    global t_max, t_min
    if i == n:
        if cal > t_max:
            t_max = cal
        if cal < t_min:
            t_min = cal
        return

    if a:
        dfs(i+1, a-1, b, c, d, cal+num[i])
    if b:
        dfs(i+1, a, b-1, c, d, cal-num[i])
    if c:
        dfs(i+1, a, b, c-1, d, cal*num[i])
    if d:
        dfs(i+1, a, b, c, d-1, int(cal/num[i]))

T = int(input())

for tc in range(T):
    n = int(input())
    a, b, c, d = map(int, input().split())
    num = list(map(int, input().split()))
    t_max = -100000000
    t_min = 100000000

    dfs(1, a, b, c, d, num[0])

    print(f'#{tc+1} {t_max-t_min}')