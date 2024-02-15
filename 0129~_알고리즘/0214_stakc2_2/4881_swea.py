# 4881_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXRI9fXK62cDFAQT&probBoxId=AY2YXC0qjRgDFAXh&type=USER&problemBoxTitle=240214_Stack2_2&problemBoxCnt=4
'''
def dfs(i, k, s):
    global min_v
    if i == k:
        if min_v > s:
            min_v = s
    elif s > min_v:
        return
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            dfs(i + 1, k, s + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]
 
T = int(input())
 
for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [i for i in range(n)]
    min_v = 100
    dfs(0, n, 0)
    print(f'#{tc+1} {min_v}')