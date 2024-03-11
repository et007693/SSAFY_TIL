# 9937_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXHqawrKUigDFARK&probBoxId=AY3tCHGaCP4DFAUZ&type=USER&problemBoxTitle=240228_%EC%99%84%EC%A0%84%EA%B2%80%EC%83%89%2F%EA%B7%B8%EB%A6%AC%EB%94%94_2&problemBoxCnt=3
'''
def check(n):
    turn = player[n]
    for j in range(10):
        if turn[j] == 3:
            return True
    for k in range(8):
        if turn[k] and turn[k+1] and turn[k+2]:
            return True

T = int(input())

for tc in range(T):
    card = list(map(int, input().split()))
    player = [[0]*10 for _ in range(2)]
    result = 0

    for c in range(0,12,2):
        player[0][card[c]] += 1
        player[1][card[c+1]] += 1

        if c >= 4:
            if check(0):
                result = 1
                break
            elif check(1):
                result = 2
                break

    print(f'#{tc + 1} {result}')