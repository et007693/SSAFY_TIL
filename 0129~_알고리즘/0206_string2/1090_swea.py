# 1989_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV5PyTLqAf4DFAUq&probBoxId=AY15MYu6dNADFAWX&type=PROBLEM&problemBoxTitle=240206_String_2&problemBoxCnt=4
'''
T = int(input())

for tc in range(T):
    s = input()
    result = 0

    if s == s[::-1]:
        result = 1

    print(f'#{tc+1} {result}')