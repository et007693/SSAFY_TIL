# 10543_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AY1S2R462h4DFAWX&probBoxId=AY15MyoKdOYDFAWX
'''
T = int(input())

for tc in range(T):
    n = int(input())
    number = list(map(int, input().split()))
    min_idx = 0

    for i in range(n):
        if number[i] < number[min_idx]:
            min_idx = i

    print(f'#{tc+1} {min_idx+1}')