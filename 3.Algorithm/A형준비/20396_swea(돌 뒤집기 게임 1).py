# 20396_swea(돌 뒤집기 게임 1)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AY3ozjTawckDFAUZ&probBoxId=AY3tCHGaCQADFAUZ&type=USER&problemBoxTitle=IM+%EB%8C%80%EB%B9%84&problemBoxCnt=10
indexing 문제
범위를 일일히 계산하기보다 범위 안에 존재할때만 실행하는 방식으로 코드 작성하기
'''
T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    stone = list(map(int, input().split()))

    for _ in range(m):
        i,j = map(int, input().split())
        color = stone[i-1]
        for c in range(j-1):
            if i+c < n:
                stone[i+c] = color

    print(f'#{tc+1}', *stone)