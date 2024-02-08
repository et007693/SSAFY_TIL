# 1219_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV14geLqABQCFAYD&probBoxId=AY15MYu6dNIDFAWX&type=PROBLEM&problemBoxTitle=240208_Stack1_2&problemBoxCnt=3
'''
def dfs(node, start, end):
    stack = [start]
    while stack:
        now = stack.pop()
        for n in node:
            if n[0] == now:
                if n[1] == end:
                    return 1
                else:
                    stack.append(n[1])
    return 0
 
for _ in range(10):
    tc, n = map(int,input().split())
    load = list(map(int, input().split()))
    load = [[load[l], load[l+1]] for l in range(0,n*2,2)]
 
    result = dfs(load, 0, 99)
 
    print(f'#{tc} {result}')

# def dfs(end):
#     for i in range(100):
#         stack = []
#         visited[i] = True
#         while end != :
#             for j in adj_lo[i]:
#                 if not visited[j]:
#                     stack.append(adj_lo[i])

#     return 0


# for _ in range(10):
#     tc, n = map(int,input().split())
#     load = list(map(int, input().split()))
#     load = [[load[l], load[l+1]] for l in range(0,n*2,2)]

#     adj_lo = [[] for _ in range(100)]
#     for l in load:
#         adj_lo[l[0]].append(l[1])
#     visited = [False] * 100
#     end = [0]*100

#     result = dfs(99)

#     print(f'#{tc} {result}')