# 9934_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXHqX2-6UdADFARK&probBoxId=AY3tCHGaCP4DFAUZ&type=USER&problemBoxTitle=240228_%EC%99%84%EC%A0%84%EA%B2%80%EC%83%89%2F%EA%B7%B8%EB%A6%AC%EB%94%94_2&problemBoxCnt=3
'''
T = int(input())
 
for tc in range(T):
    n, m = map(int, input().split())
    con = sorted(list(map(int, input().split())), reverse = True)
    truck = sorted(list(map(int, input().split())), reverse = True)
    result = 0
 
    for t in truck:
        for c in range(n):
            if t >= con[c] and con[c] != 0:
                result += con[c]
                con[c] = 0
                break
 
    print(f'#{tc+1} {result}')