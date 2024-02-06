# 3143_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV5PyTLqAf4DFAUq&probBoxId=AY15MYu6dNADFAWX&type=PROBLEM&problemBoxTitle=240206_String_2&problemBoxCnt=4
'''
T = int(input())

for tc in range(T):
    s1, s2 = input().split()
    s1 = s1.replace(s2, " ")
    print(f'#{tc + 1} {len(s1)}')