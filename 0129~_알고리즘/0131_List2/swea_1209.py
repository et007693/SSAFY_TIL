# swea_1209
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV13_BWKACUCFAYh&probBoxId=AY1andpK_vQDFAWX&type=PROBLEM&problemBoxTitle=240131_List2_1&problemBoxCnt=4

'''
for _ in range(10):
    arr = []
    result = 0
    n = int(input())
    for _ in range(100):
        arr.append(list(map(int,input().split())))

    max_sum = []
    for c in range(100):
        max_sum.append(sum([i[c] for i in arr]))
        max_sum.append(sum(arr[c]))

    max_sum.append(sum([arr[i][i] for i in range(10)]))
    max_sum.append(sum([arr[9-i][0+i] for i in range(10)]))

    for m in max_sum:
        if m > result:
            result = m

    print(f'#{n} {result}')