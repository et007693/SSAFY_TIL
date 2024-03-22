# 5251_swea(최소 이동 거리)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXI7ZKKKnugDFAXR&solveclubId=AY1S2R462h4DFAWX&problemBoxTitle=240321_%EA%B7%B8%EB%9E%98%ED%94%84_2&problemBoxCnt=3&probBoxId=AY4mJ-0q_tQDFAUZ
최소 이동 거리 - Dijkstra
그래프 이론 공부하기
'''
from heapq import heappush, heappop
def dijkstra(start):
    pq = []
    heappush(pq, (start, 0))
    distance[start] = 0

    while pq:
        now, dist = heappop(pq)
        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            n_dist = dist + cost
            if n_dist < distance[next_node]:
                distance[next_node] = n_dist
                heappush(pq, (next_node, n_dist))

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    inf = int(1e9)
    distance = [inf] * (n+1)
    dijkstra(0)

    print(f'#{tc+1} {distance[-1]}')