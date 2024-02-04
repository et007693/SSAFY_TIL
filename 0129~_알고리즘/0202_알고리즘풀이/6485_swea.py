# 6485_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AWczm7QaACgDFAWn&solveclubId=AY1S2R462h4DFAWX&problemBoxTitle=240202_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B41&problemBoxCnt=9&probBoxId=AY1andpK_vYDFAWX
'''
T = int(input())

for tc in range(T):
    n = int(input())
    stop = [0]*5001

    for _ in range(n):
        a, b = map(int, input().split())
        for s in range(a, b+1):
            stop[s] += 1

    p = int(input())
    c = [int(input()) for _ in range(p)]

    print(f'#{tc+1}', end = ' ')
    for s in c:
        print(stop[s], end = ' ')
    print()