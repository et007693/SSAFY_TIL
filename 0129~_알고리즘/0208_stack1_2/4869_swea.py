# 4869_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXQrSFQKpusDFAXS&probBoxId=AY15MYu6dNIDFAWX&type=USER&problemBoxTitle=240208_Stack1_2&problemBoxCnt=2
dp
'''
T = int(input())

for tc in range(T):
    n = int(input())
    cnt = [0] * (n//10)

    cnt[0] = 1
    cnt[1] = 3

    for i in range(2, n//10):
        cnt[i] = cnt[i-1] + 2*cnt[i-2]

    print(f'#{tc+1} {cnt[-1]}')
