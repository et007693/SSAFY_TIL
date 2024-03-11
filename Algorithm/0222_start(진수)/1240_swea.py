# 1240_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV15FZuqAL4CFAYD&probBoxId=AY3EiucKKtYDFAXh&type=PROBLEM&problemBoxTitle=240222_Start_1&problemBoxCnt=4
'''
T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    code = [input() for _ in range(n)]
    num = ['0001101',
           '0011001',
           '0010011',
           '0111101',
           '0100011',
           '0110001',
           '0101111',
           '0111011',
           '0110111',
           '0001011'
           ]
    pwd = []
    v_n = 0
    result = 0

    for y in range(n):
        for x in range(m-6):
            if code[y][x:x+7] in num and code[y][x+56:].find('1') == -1:
                start = (x,y)
                break

    for i in range(start[0], start[0]+56, 7):
        pwd.append(code[start[1]][i:i+7])

    for p in range(8):
        value = num.index(pwd[p])
        if p % 2 == 0:
            v_n += value * 3
        else:
            v_n += value
        result += value

    if v_n % 10 == 0:
        print(f'#{tc+1} {result}')
    else:
        print(f'#{tc+1} 0')