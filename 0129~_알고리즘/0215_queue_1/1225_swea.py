# 1225_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV14uWl6AF0CFAYD&probBoxId=AY2YXC0qjRkDFAXh&type=PROBLEM&problemBoxTitle=240215_Queue_1&problemBoxCnt=3
'''
for _ in range(10):
    tc = int(input())
    pwd = list(map(int, input().split()))
    point = 1
    cnt = 1
 
    while point > 0:
        point = pwd.pop(0)
        if point - cnt < 0:
            point = 0
        else:
            point -= cnt
        cnt = (cnt % 5) + 1
        pwd.append(point)
 
    print(f'#{tc}', *pwd)