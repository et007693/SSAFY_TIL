# 9922_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXHN_JW6YWEDFAXR&probBoxId=AY3EiucKKtYDFAXh&type=USER&problemBoxTitle=240222_Start_1&problemBoxCnt=4
'''
T = int(input())

for tc in range(T):
    num = float(input())
    cnt = 1
    result = ''

    while num:
        if cnt > 12:
            result = 'overflow'
            break
        result += str(num // 2 ** -cnt)[0]
        num %= 2 ** -cnt
        cnt += 1

    print(f'#{tc + 1} {result}')