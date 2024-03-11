# 10926_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXVUixgKHFYDFAVE&probBoxId=AY3EiucKKtYDFAXh&type=USER&problemBoxTitle=240222_Start_1&problemBoxCnt=4
'''
T = int(input())

for tc in range(T):
    string = input()
    print(f'#{tc+1}', end = ' ')
    for i in range(0, len(string), 7):
        print(int(string[i:i+7],2), end = ' ')
    print()