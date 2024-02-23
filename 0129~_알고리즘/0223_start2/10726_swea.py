# 10726_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXRSXf_a9qsDFAXS&probBoxId=AY3EiucKKtcDFAXh&type=PROBLEM&problemBoxTitle=240223_Start_2&problemBoxCnt=2
'''
T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    if m & (1 << n)-1 == (1 << n)-1:
        print(f"#{tc+1} ON")
    else:
        print(f"#{tc+1} OFF")