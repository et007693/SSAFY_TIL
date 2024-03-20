
# 5248_swea(그룹 나누기)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXI1f2-qXWoDFAXR&solveclubId=AY1S2R462h4DFAWX&problemBoxTitle=240320_%EA%B7%B8%EB%9E%98%ED%94%84_1&problemBoxCnt=2&probBoxId=AY4mJ5Tq_tIDFAUZ
'''
def dfs(start):
    global cnt
    visited[start] = 1
    for s in people[start]:
        if not visited[s]:
            dfs(s)
            
T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    paper = list(map(int, input().split()))
    paper = [[paper[2*i], paper[2*i+1]] for i in range(m)]
    visited = [0]*(n+1)
    cnt = 0

    people = [[] for _ in range(n+1)]
    for n1, n2 in paper:
        people[n1].append(n2)
        people[n2].append(n1)

    for p in range(1, n+1):
        if not visited[p]:
            dfs(p)
            cnt += 1
    print(f'#{tc+1} {cnt}')