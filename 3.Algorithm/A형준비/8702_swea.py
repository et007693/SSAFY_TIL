# 8702_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AW2ZiPcaPQ8DFAWg&probBoxId=AY15MyoKdOYDFAWX&type=USER&problemBoxTitle=%EA%B8%B0%EC%B4%88+%EC%97%B0%EC%8A%B5+%EB%AC%B8%EC%A0%9C&problemBoxCnt=4
'''
T = int(input())

for tc in range(T):
    n = int(input())
    carrot = list(map(int, input().split()))
    carrot_min = sum(carrot)
    a = b = 0

    for i in range(n):
        if abs(sum(carrot[:i]) - sum(carrot[i:])) < carrot_min:
            carrot_min = abs(sum(carrot[:i]) - sum(carrot[i:]))
            a, b = len(carrot[:i]), carrot_min

    print(f'#{tc+1} {a} {b}')