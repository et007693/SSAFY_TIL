# 4871_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXQrYZ-qqBoDFAXS&probBoxId=AY15MYu6dNIDFAWX&type=USER&problemBoxTitle=240208_Stack1_2&problemBoxCnt=2
DFS
'''
T = int(input())
 
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
 
for tc in range(T):
    v, e = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int,input().split())
 
    result = dfs(node, s, g)
 
    print(f'#{tc+1} {result}')