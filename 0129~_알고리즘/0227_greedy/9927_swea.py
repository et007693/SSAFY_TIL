# 9927_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXHk-aUaFd8DFARK&probBoxId=AY3oVKuqtf0DFAUZ&type=USER&problemBoxTitle=240227_%EC%99%84%EC%A0%84%EA%B2%80%EC%83%89%2F%EA%B7%B8%EB%A6%AC%EB%94%94_1&problemBoxCnt=3
'''
def back(i, s):
    global result

    if result <= s:
        return

    if i == n:
        s += battery[idx[i - 1]][idx[i]]
        if s < result:
            result = s
        return

    for j in range(i, n):
        idx[i], idx[j] = idx[j], idx[i]
        back(i+1, s + battery[idx[i - 1]][idx[i]])
        idx[i], idx[j] = idx[j], idx[i]

T = int(input())

for tc in range(T):
    n = int(input())
    battery = [list(map(int, input().split())) for _ in range(n)]
    idx = [i for i in range(n)] + [0]
    result = 1000000

    back(1, 0)

    print(f'#{tc+1} {result}')