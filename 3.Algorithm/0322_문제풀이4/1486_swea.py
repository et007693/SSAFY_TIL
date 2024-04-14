# 1486_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV2b7Yf6ABcBBASw&probBoxId=AY4mKUKa_twDFAUZ&type=PROBLEM&problemBoxTitle=240322_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B44&problemBoxCnt=8
'''
def dfs(i, s):
    global result
    if i == n:
        if s >= b:
            result = min(result, s)
        return

    dfs(i+1, s+height[i])
    dfs(i+1, s)

T = int(input())

for tc in range(T):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    result = sum(height)
    dfs(0, 0)

    print(f'#{tc+1} {result-b}')