# 10546_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXOt0B3qknwDFAXS&probBoxId=AY15MyoKdOYDFAWX&type=USER&problemBoxTitle=%EA%B8%B0%EC%B4%88+%EC%97%B0%EC%8A%B5+%EB%AC%B8%EC%A0%9C&problemBoxCnt=4
'''
T = int(input())

for tc in range(T):
    n = int(input())
    number = list(map(int, input().split()))
    cnt = 0

    for num in number:
        if num % 2 == 0:
            cnt += 1
    print(f'#{tc+1} {cnt}')