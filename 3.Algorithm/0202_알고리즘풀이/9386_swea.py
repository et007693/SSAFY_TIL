# 9386_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXALDUIq97oDFASI&probBoxId=AY1andpK_vYDFAWX&type=USER&problemBoxTitle=240202_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B41&problemBoxCnt=9
'''
T = int(input())

for tc in range(T):
    n = int(input())
    number = input()
    max_cnt = 0

    for c in range(n):
        cnt = 0
        if number[c] == '1':
            idx = c
            while True:
                if idx + 1 <= n and number[idx] != '0':
                    cnt += 1
                    idx += 1
                else:
                    break

            if cnt > max_cnt:
                max_cnt = cnt
    print(f'#{tc+1} {max_cnt}')