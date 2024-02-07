# 4873_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXQrcIh6qJADFAXS&solveclubId=AY1S2R462h4DFAWX&problemBoxTitle=240207_Stack1_1&problemBoxCnt=4&probBoxId=AY15MYu6dNEDFAWX
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