# 1222_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV14mbSaAEwCFAYD&probBoxId=AY2YXC0qjRcDFAXh&type=PROBLEM&problemBoxTitle=240213_Stack2_1&problemBoxCnt=3
'''
for tc in range(10):
    n = int(input())
    formula = input()
    forth = []
    stack = []
    operator = ''

    for f in formula:
        if operator:
            if f.isdigit():
                forth.append(f)
                forth.append('+')
                operator = False
        elif f == '+':
            operator = True
        else:
            forth.append(f)

    for f in forth:
        if f.isdigit():
            stack.append(int(f))
        elif f == '+' and len(stack) >= 2:
            stack.append(int(stack.pop() + int(stack.pop())))

    print(f'#{tc+1} {stack.pop()}')