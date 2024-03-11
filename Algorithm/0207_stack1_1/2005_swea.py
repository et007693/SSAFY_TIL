# 2005_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV5P0-h6Ak4DFAUq&probBoxId=AY15MYu6dNEDFAWX&type=PROBLEM&problemBoxTitle=240207_Stack1_1&problemBoxCnt=4
재귀, DP
'''
def pascal(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1,1]
    else:
        before = pascal(n-1)
        tmp = [1]*(n+1)
        for i in range(n-1):
            tmp[i+1] = before[i] + before[i+1]
        return tmp

T = int(input())

for tc in range(T):
    n = int(input())
    print(f'#{tc+1}')
    for i in range(n):
        print(*pascal(i))