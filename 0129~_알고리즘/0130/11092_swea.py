# swea_11092
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXYEGnBq6h0DFAST&probBoxId=AY1YYdUalYYDFAWX&type=USER&problemBoxTitle=240130_List1_2&problemBoxCnt=5

내장함수를 사용하지 않고 풀이
'''
T = int(input())

for tc in range(T):
    n = int(input())
    number = list(map(int, input().split()))
    max_num, min_num = 0, number[-1]

    for num in range(n):
        if number[num] >= max_num:
            max_num = number[num]
            max_idx = num
        if number[num] < min_num:
            min_num = number[num]
            min_idx = num

    print(f'#{tc + 1} {abs(max_idx - min_idx)}')