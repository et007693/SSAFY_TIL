for tc in range(10):
    n = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))

    # 시작 지점
    start_idx = []
    for s in range(len(ladder[0])):
        if ladder[0][s]:
            start_idx.append(s)

    for s in start_idx:
        y, x = s, 0
        print('start :', x, y)

        # while y != 99:
        #     y += 1
        #
        #     if ladder[y][x-1] and x > 0:
        #         while x > 0 and ladder[y][x-1] == 1:
        #             x -= 1
        #
        #     elif ladder[y][x+1] and x < 99:
        #         while y < 99 and ladder[y][x+1] == 1:
        #             x += 1
        #
        #     if ladder[y][x] == 2:
        #         break
        x += 1
        if y > 0 and ladder[x][y - 1] == 1:
            while y > 0 and ladder[x][y - 1] == 1:
                y -= 1
        elif y < 99 and ladder[x][y + 1] == 1:
            while y < 99 and ladder[x][y + 1] == 1:
                y += 1

        if ladder[x][y] == 2:
            result = s
            break
            print(result)

        print(f'#{tc+1} {result}')
