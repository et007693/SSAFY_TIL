# 9935_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXHqYYIqUecDFARK&solveclubId=AY1S2R462h4DFAWX&problemBoxTitle=240228_%EC%99%84%EC%A0%84%EA%B2%80%EC%83%89%2F%EA%B7%B8%EB%A6%AC%EB%94%94_2&problemBoxCnt=3&probBoxId=AY3tCHGaCP4DFAUZ
'''
T = int(input())
 
for tc in range(T):
    n = int(input())
    truck = [list(map(int, input().split())) for _ in range(n)]
    cargo = [0]*25
    result = 0
 
    truck.sort(key=lambda x: x[1])
 
    for t in range(n):
        s, e = truck[t][0], truck[t][1]
        if cargo[s] != 1:
            result += 1
            for c in range(e):
                cargo[c] = 1
 
    print(f'#{tc+1} {result}')