for c in range(10):
    n = int(input())
    height = list(map(int, input().split()))
    cnt = 0

    for index in range(2, n-2):
        view = height[index] - max(*height[index-2:index], *height[index+1:index+3])
        if view > 0:
            cnt += view

    print(f'#{c+1} {cnt}')