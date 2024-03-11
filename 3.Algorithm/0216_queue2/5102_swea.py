# 5105_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXRPDuNKn4kDFAXS&probBoxId=AY2YXC0qjRoDFAXh&type=USER&problemBoxTitle=240216_Queue_2&problemBoxCnt=2
'''
T = int(input())

def bfs(start):
    queue = [start]
    visited[start] = True
    while queue:
        now = queue.pop(0)
        for n in node:
            if n[0] == now and not visited[n[1]]:
                queue.append(n[1])
                distance[n[1]] = distance[now] + 1
                visited[n[1]] = True
            if n[1] == now and not visited[n[0]]:
                queue.append(n[0])
                distance[n[0]] = distance[now] + 1
                visited[n[0]] = True
    return 0

for tc in range(T):
    v, e = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())
    distance = [0]*(v+1)
    visited = [0]*(v+1)

    bfs(s, g)
    print(f'#{tc+1} {distance[g]}')