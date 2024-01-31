# swea_2001
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV5PzOCKAigDFAUq&probBoxId=AY1andpK_vQDFAWX&type=PROBLEM&problemBoxTitle=240131_List2_1&problemBoxCnt=3

처음엔 델타값을 활용해서 진행하려고 했으나 파리채의 크기가 커질수록 비는 값이 생겼음
-> 이중 for문을 사용하여 범위 개념으로 진행

중간에 좌표가 자꾸 벗어나서 많이 헤멨음 -> 범위 정해주는 과정에서 문제가 있었는데 항상 어려운것 같다 
'''
T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    fly = []
    fly_cnt = 0

    for _ in range(n):
        fly.append(list(map(int, input().split())))

    for y in range(n - (m - 1)):
        for x in range(n - (m - 1)):
            cnt = 0
            for i in range(m):
                for j in range(m):
                    dx = x + j
                    dy = y + i
                    cnt += fly[dy][dx]

            if cnt > fly_cnt:
                fly_cnt = cnt

    print(f'#{tc + 1} {fly_cnt}')
