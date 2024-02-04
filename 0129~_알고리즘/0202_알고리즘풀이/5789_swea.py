# 5789_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AWYygN36Qn8DFAVm&probBoxId=AY1andpK_vYDFAWX&type=PROBLEM&problemBoxTitle=240202_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B41&problemBoxCnt=9
'''
T = int(input())

for tc in range(T):
    n, q = map(int, input().split())
    box = [0]*(n+1)

    for i in range(q):
        l, r = map(int, input().split())
        for c in range(l, r+1):
            box[c] = i+1

    print('#{}'.format(tc+1), *box[1:n+1])