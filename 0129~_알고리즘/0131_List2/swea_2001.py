# swea_2001
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
