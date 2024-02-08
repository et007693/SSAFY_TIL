# 10564_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AY1S2R462h4DFAWX&probBoxId=AY15MyoKdOYDFAWX
'''
T = int(input())
 
for tc in range(T):
    n = int(input())
    number = list(map(int, input().split()))
 
    ma = mi = number[0] + number[1]
 
    for n in range(n - 1):
        tmp = number[n] + number[n + 1]
        if tmp > ma:
            ma = tmp
        if tmp < mi:
            mi = tmp
 
    print(f'#{tc + 1} {ma} {mi}')