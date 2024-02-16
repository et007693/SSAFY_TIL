# 10722_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXRO_ZGqnokDFAXS&probBoxId=AY2YXC0qjRkDFAXh&type=USER&problemBoxTitle=240215_Queue_1&problemBoxCnt=3
'''
T = int(input())
 
for tc in range(T):
    n, m = map(int, input().split())
    number = list(map(int, input().split()))
 
    for _ in range(m):
        number.append(number.pop(0))
 
    print(f'#{tc+1} {number[0]}')