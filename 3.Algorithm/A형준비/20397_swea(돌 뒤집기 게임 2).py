# 20397_swea(돌 뒤집기 게임 2)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AY3o7m4axawDFAUZ&probBoxId=AY3tCHGaCQADFAUZ&type=USER&problemBoxTitle=IM+%EB%8C%80%EB%B9%84&problemBoxCnt=10
'''
T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    stone = list(map(int, input().split()))

    for _ in range(m):
        i, j = map(int, input().split())
        i -= 1
        for c in range(1,j+1):
            color = 1 if stone[i-c] == 0 else 0
            if 0 <= i-c and i+c < n and stone[i-c] == stone[i+c]:
                stone[i+c] = color
                stone[i-c] = color

    print(f'#{tc+1}', *stone)