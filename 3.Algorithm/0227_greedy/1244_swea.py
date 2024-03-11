# 1244_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV15Khn6AN0CFAYD&probBoxId=AY3oVKuqtf0DFAUZ&type=PROBLEM&problemBoxTitle=240227_%EC%99%84%EC%A0%84%EA%B2%80%EC%83%89%2F%EA%B7%B8%EB%A6%AC%EB%94%94_1&problemBoxCnt=3
''.join(list)
백트래킹 조건
'''
def dfs(n):
    global result
    if n == int(t):
        result = max(result, int(''.join(s)))
        return

    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            s[i], s[j] = s[j], s[i]

            # 백트래킹 조건
            tmp = ''.join(s)
            if (n, tmp) not in valid:
                dfs(n+1)
                valid.append((n, tmp))

            s[i], s[j] = s[j], s[i]

T = int(input())

for test_case in range(1, T + 1):
    num, t = input().split()
    result = 0
    s, valid = [], []
    for i in num:
        s.append(i)

    dfs(0)
    print(f'#{test_case} {result}')