# 5099_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXRPF5xKoBQDFAXS&probBoxId=AY2YXC0qjRkDFAXh&type=USER&problemBoxTitle=240215_Queue_1&problemBoxCnt=3
'''
T = int(input())
 
for tc in range(T):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    oven = pizza[:n]
    idx = [i for i in range(1, n+1)]
    point = n
 
    while len(oven) > 1:
        if oven[0] > 0:
            oven.append(oven.pop(0)//2)
            idx.append(idx.pop(0))
        else:
            oven.pop(0)
            idx.pop(0)
            if point < len(pizza):
                oven.insert(0, pizza[point])
                idx.insert(0, point+1)
                point += 1
 
    print(f'#{tc+1} {idx.pop()}')