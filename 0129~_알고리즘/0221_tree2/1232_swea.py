# 1232_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AY1S2R462h4DFAWX&probBoxId=AY3EiY6KKq4DFAXh
'''
def cal(start=1):
    start = int(start)
    if start <= n:
        s = node[start][0]
        if s in '-+/*':
            if s == '+':
                node[start] = int(cal(node[start][1]) + cal(node[start][2]))
            elif s == '-':
                node[start] = int(cal(node[start][1]) - cal(node[start][2]))
            elif s == '/':
                node[start] = int(cal(node[start][1]) / cal(node[start][2]))
            else:
                node[start] = int(cal(node[start][1]) * cal(node[start][2]))
            return node[start]
        else:
            return int(s)
    else:
        return
 
for tc in range(10):
    n = int(input())
    node = [0]*(n+1)
 
    for i in range(n):
        tmp = list(input().split())
        node[int(tmp[0])] = tmp[1:]
 
    result = cal()
 
    print(f'#{tc+1} {result}')