# 1865_동철이의 일 분배
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV5LuHfqDz8DFAXc&probBoxId=AY4mJz-K_tADFAUZ&type=PROBLEM&problemBoxTitle=240319_%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9_2&problemBoxCnt=4
'''
def work(y, s):
    global result
    if result >= s:
        return
 
    if y == n:
        result = max(result, s)
        return
 
    for x in range(n):
        if not used[x]:
            used[x] = 1
            work(y+1, s*(percent[y][x]/100))
            used[x] = 0
 
T = int(input())
 
for tc in range(T):
    n = int(input())
    percent = [list(map(int, input().split())) for _ in range(n)]
    used = [0]*n
    result = 0
 
    work(0, 100)
    print(f'#{tc+1} {result:.6f}')