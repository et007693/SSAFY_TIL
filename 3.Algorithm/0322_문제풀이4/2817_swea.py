# 2817_swea(부분수열의 합)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV7IzvG6EksDFAXB&probBoxId=AY4mKUKa_twDFAUZ&type=PROBLEM&problemBoxTitle=240322_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B44&problemBoxCnt=8
'''
def dfs(i, s):
    global cnt
    if i == n or s >= k:
        if s == k:
            cnt += 1
        return

    dfs(i+1, s+num[i])
    dfs(i+1, s)

T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    cnt = 0

    dfs(0, 0)

    print(f'#{tc+1} {cnt}')