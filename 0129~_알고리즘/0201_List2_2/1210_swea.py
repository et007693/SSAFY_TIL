# 1210_swea
'''
사다리 타고 내려가기

! 주의할점 : 옆으로 이동했을 때 다시 되돌아 갈 수 있음

어려웠던 점
1. 인덱스가 범위를 벗어남
2. 코드가 같은 코드였는데 왜 실행이 안됐는지 의문
'''

for _ in range(10):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start_idx = [s for s in range(100) if ladder[0][s] == 1]

    for s in start_idx:
        x, y = s, 0
        while y < 99:
            y += 1
            if x > 0 and ladder[y][x-1]:
                while x > 0 and ladder[y][x-1]:
                    x -= 1
            elif x < 99 and ladder[y][x+1]:
                while x < 99 and ladder[y][x+1]:
                    x += 1

            if ladder[y][x] == 2:
                result = s
                break

    print(f'#{n} {result}')
