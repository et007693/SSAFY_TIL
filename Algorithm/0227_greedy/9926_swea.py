# 9926_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXHk2R_KFLADFARK&probBoxId=AY3oVKuqtf0DFAUZ&type=USER&problemBoxTitle=240227_%EC%99%84%EC%A0%84%EA%B2%80%EC%83%89%2F%EA%B7%B8%EB%A6%AC%EB%94%94_1&problemBoxCnt=3
'''
def dfs(start, score=0):
    global cnt
    x, y = start
 
    if x >= n or y >= n or score > cnt:
        return
 
    score += arr[y][x]
    if x == y == n - 1:
        if score <= cnt:
            cnt = score
        return
 
    dfs((x + 1, y), score)
    dfs((x, y + 1), score)
 
T = int(input())
 
for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = (n ** 2) * 13
 
    dfs([0, 0])
    print(f'#{tc + 1} {cnt}')