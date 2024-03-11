# 4866_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXQrUKEap0gDFAXS&probBoxId=AY15MYu6dNEDFAWX&type=USER&problemBoxTitle=240207_Stack1_1&problemBoxCnt=2
'''
T = int(input())

for tc in range(T):
    s1 = input()
    s2 = []
    arr = ['(', ')', '{', '}']
    result = 0

    for s in s1:
        if s in arr:
            if s2:
                if s == ')' and s2[-1] == '(':
                    s2.pop()
                elif s == '}' and s2[-1] == '{':
                    s2.pop()
                else:
                    s2.append(s)
            else:
                s2.append(s)
    if s2:
        result = 0
    else:
        result = 1

    print(f'#{tc+1} {result}')