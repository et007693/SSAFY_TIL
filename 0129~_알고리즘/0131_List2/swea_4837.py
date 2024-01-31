# swea_4837
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXO-1Zh6aPEDFAXS&probBoxId=AY1andpK_vQDFAWX&type=USER&problemBoxTitle=240131_List2_1&problemBoxCnt=3

'''
T = int(input())
A = [i for i in range(1, 13)]

for tc in range(T):
    n, k = map(int, input().split())
    cnt = 0
    subsets = []

    for i in range(1<<len(A)):
        subsets.append([A[j] for j in range(len(A)) if (i & (1 << j))> 0])

    subsets = [i for i in subsets if len(i) == n]

    for sub in subsets:
        if sum(sub) == k:
            cnt +=1

    print(f'#{tc+1} {cnt}')