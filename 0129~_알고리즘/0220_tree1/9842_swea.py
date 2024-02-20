# 9842_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXGBLnRKVf8DFARK&probBoxId=AY2YXC0qjRsDFAXh&type=USER&problemBoxTitle=240220_Tree_1&problemBoxCnt=3
'''
def node_count(start):
    cnt = 1
    que = [start]
    while que:
        point = que.pop(0)
        for n in node:
            if n[0] == point:
                que.append(n[1])
                cnt += 1
    return cnt

T = int(input())

for tc in range(T):
    e, n = map(int, input().split())
    node_list = list(map(int, input().split()))
    node = [node_list[i:i+2] for i in range(0, e*2, 2)]

    result = node_count(n)
    print(f'#{tc+1} {result}')