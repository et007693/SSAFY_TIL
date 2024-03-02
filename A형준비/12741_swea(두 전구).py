# 12741_swea(두 전구)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXuUo_Tqs9kDFARa&probBoxId=AY3tCHGaCQADFAUZ&type=PROBLEM&problemBoxTitle=IM+%EB%8C%80%EB%B9%84&problemBoxCnt=10
test case 수가 많아 시간 초과 발생
print가 시간이 오래걸림 - 한번에 출력
'''
T = int(input())
result = ''

for tc in range(T):
    a, b, c, d = map(int, input().split())
    value = 0

    start = max(a, c)
    end = min(b, d)

    if end > start:
        value = end - start
    result += f'#{tc + 1} {value}\n'
print(result)