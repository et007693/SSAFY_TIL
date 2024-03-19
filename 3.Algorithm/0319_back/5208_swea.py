# 5208_swea(전기버스2)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXWJEOOaq1ADFAST&probBoxId=AY4mJz-K_tADFAUZ&type=USER&problemBoxTitle=240319_%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9_2&problemBoxCnt=4
'''
def charge(i, b, c):
    global cnt
    if c >= cnt or b <= 0:
        return
 
    if i == n-1:
        cnt = min(c, cnt)
        return
 
    charge(i+1, stop[i], c+1)
    charge(i+1, b-1, c)
 
 
T = int(input())
 
for tc in range(T):
    stop = list(map(int, input().split()))+[0]
    n = stop.pop(0)
    cnt = n
 
    charge(1, stop[0], 0)
 
    print(f'#{tc+1} {cnt}')