# 1952_swea(수영장)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV5PpFQaAQMDFAUq&solveclubId=AY1S2R462h4DFAWX&problemBoxTitle=240322_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B44&problemBoxCnt=8&probBoxId=AY4mKUKa_twDFAUZ
너무 dfs, 백트래킹만 사용해서 풀려고 하지 말자!
'''
# 방법 1(dfs) - 내 방식
def dfs(i, s):
    # print(i, s)
    global result
    if i >= 12 or s >= result:
        result = min(s, result)
        return

    if s >= month[i]:
        return

    month[i] = min(s, month[i])

    dfs(i+12, s+y)
    dfs(i+3, s+tm)
    dfs(i+1, s+m)
    dfs(i+1, s+d*(cost[i]))

T = int(input())

for tc in range(T):
    d, m, tm, y = map(int, input().split())
    cost = list(map(int, input().split()))
    result = 3000*12
    month = [result]*12

    dfs(0, 0)
    print(f'#{tc+1} {result}')

# 방법 2(visited)
T=int(input())

for tc in range(T):
    a,b,c,d = map(int,input().split())
    arr = [0]+list(map(int,input().split()))
    plan =[0]*13
 
    for i in range(1,13):
        plan[i] = plan[i-1] + min(a*arr[i],b)
        if i>=3:
            plan[i]=min(plan[i-3]+c,plan[i])
        if i==12:
            plan[i]=min(plan[i],d)
    print(f'#{tc+1} {plan[12]}')