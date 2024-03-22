# 7465_swea(창용 마을 무리의 개수)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AWngfZVa9XwDFAQU&probBoxId=AY4mKUKa_twDFAUZ&type=PROBLEM&problemBoxTitle=240322_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B44&problemBoxCnt=8
'''
def find(x):
    if parents[x] == x:
        return x
    return find(parents[x])

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x < y:
        for i in range(1, n+1):
            if parents[i] == y:
                parents[i] = x
    else:
        for i in range(1, n+1):
            if parents[i] == x:
                parents[i] = y

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    parents = [i for i in range(n+1)]

    for g1, g2 in graph:
        union(g1, g2)

    print(f'#{tc+1} {len(set(parents))-1}')