# 4873_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXQrcIh6qJADFAXS&probBoxId=AY15MYu6dNEDFAWX&type=USER&problemBoxTitle=240207_Stack1_1&problemBoxCnt=2
'''
T = int(input())

for tc in range(T):
    s1 = input()
    s2 = []

    for s in s1:
        if s2:
            if s == s2[-1]:
                s2.pop()
            else:
                s2.append(s)
        else:
            s2.append(s)

    print(f'#{tc+1} {len(s2)}')
