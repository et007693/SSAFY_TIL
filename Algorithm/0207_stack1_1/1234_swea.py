# 1234_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV14_DEKAJcCFAYD&probBoxId=AY15MYu6dNEDFAWX&type=PROBLEM&problemBoxTitle=240207_Stack1_1&problemBoxCnt=4
'''
for tc in range(10):
    l, password = input().split()
    stack = []
 
    for i in password:
        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    print(f'#{tc+1} ', *stack, sep='')