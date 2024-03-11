# 1979_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV5PuPq6AaQDFAUq&probBoxId=AY1andpK_vYDFAWX&type=PROBLEM&problemBoxTitle=240202_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B41&problemBoxCnt=9
'''
T = int(input())

def word(array, k):
    result = 0
    cnt = 0
    for w in range(len(array)):
        if array[w] == 1:
            cnt += 1
            if w == len(array)-1 and cnt == k:
                result += 1
        elif array[w] == 0:
            if cnt == k:
                result += 1
            cnt = 0
    return result


for tc in range(T):
    n, k = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        row = array[i]
        col = [col[i] for col in array]

        result += word(row, k)
        result += word(col, k)

    print(f'#{tc+1} {result}')