# 1945_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV5Pl0Q6ANQDFAUq&solveclubId=AY1S2R462h4DFAWX&problemBoxTitle=240202_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B41&problemBoxCnt=9&probBoxId=AY1andpK_vYDFAWX
'''

T = int(input())

for tc in range(T):
    n = int(input())
    prime = [2,3,5,7,11]
    prime_cnt = [0]*5

    for p in range(5):
        while n % prime[p] == 0:
            n //= prime[p]
            prime_cnt[p] += 1
    print(f'#{tc+1}', *prime_cnt)
