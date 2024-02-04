# 4831_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXO0kefqydEDFAXS&probBoxId=AY1YYdUalYYDFAWX&type=USER&problemBoxTitle=240130_List1_2&problemBoxCnt=5
'''
T = int(input())

for tc in range(T):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))
    cnt = 0
    distance = 0

    for d in range(1, n):
        distance += 1

        if distance > k:
            cnt = 0
            break
        else:
            if d in charge:
                if d == charge[-1]:
                    if distance + n - d <= k:
                        continue
                    else:
                        cnt += 1
                idx = charge.index(d)
                if idx < m - 1:
                    if (distance + (charge[idx + 1] - charge[idx])) <= k:
                        continue
                    else:
                        distance = 0
                        cnt += 1

    if cnt:
        print(f'#{tc + 1} {cnt}')
    else:
        print(f'#{tc + 1} {0}')