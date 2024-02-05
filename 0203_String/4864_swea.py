# 4864_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXQhKu6KwW0DFAXS&probBoxId=AY13LDfqMhMDFAWX&type=USER&problemBoxTitle=240205_String_1&problemBoxCnt=2
'''
T = int(input())

for tc in range(T):
    s1 = input()
    s2 = input()
    cnt = 0

    for s in s2.split(s1):
        cnt += 1

    if cnt >= 2:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')