# 5249_swea(최소 신장 트리)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXI6cxVKimUDFAXR&probBoxId=AY4mJ-0q_tQDFAUZ&type=USER&problemBoxTitle=240321_%EA%B7%B8%EB%9E%98%ED%94%84_2&problemBoxCnt=3
prim
dijkstra
kruskal
'''
# 방법 1(kruskal)
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
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x : x[2])
    parents = [i for i in range(V+1)]
    cnt = 0
    total = 0
    for u, v, w in edge:
        if find(u) != find(v):
            cnt += 1
            union(u, v)
            total += w
            if cnt == V:
                break
                
    print(f'#{tc+1} {total}')

# 방법 2
