# 1979_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV5PuPq6AaQDFAUq&probBoxId=AY1andpK_vYDFAWX&type=PROBLEM&problemBoxTitle=240202_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B41&problemBoxCnt=9
'''
T = int(input())

for tc in range(T):
    n, k = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        row = array[i]
        col = [col[i] for col in array]

        cnt = 0
        for r in row:
            if r == 1:
                cnt += 1
            elif r == 0:
                if cnt == 3:
                    result += 1
                cnt = 0
            print(f'{cnt},{result})


        cnt = 0
        for c in col:
            if c == 1:
                cnt += 1
            elif c == 0:
                if cnt == 3:
                    result += 1
                cnt = 0


    print(f'#{tc+1} {result}')