# 4865_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXQhQbZ6z8wDFAXS&probBoxId=AY13LDfqMhMDFAWX&type=USER&problemBoxTitle=240205_String_1&problemBoxCnt=2
'''
T = int(input())

for tc in range(T):
    s1 = set(input())
    s2 = input()
    max_cnt = 0

    for i in s1:
        cnt = 0
        for j in s2:
            if i == j:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{tc+1} {max_cnt}')