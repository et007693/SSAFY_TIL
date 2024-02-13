# 4874_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXRHBq7K1xIDFAQT&probBoxId=AY2YXC0qjRcDFAXh&type=USER&problemBoxTitle=240213_Stack2_1&problemBoxCnt=2
'''
T = int(input())
 
for tc in range(T):
    forth = input().split()
    stack = []
    result = ''
 
    for f in forth:
        if f.isdigit():
            stack.append(int(f))
        elif f == '.' and len(stack) == 1:
            result = stack.pop()
        elif f in '+-*/' and len(stack) >= 2:
            a = int(stack.pop())
            b = int(stack.pop())
            if f == '+':
                stack.append(b+a)
            elif f == '-':
                stack.append(b-a)
            elif f == '*':
                stack.append(b*a)
            else:
                stack.append(int(b/a))
        else:
            result = 'error'
            break
 
    print(f'#{tc+1} {result}')