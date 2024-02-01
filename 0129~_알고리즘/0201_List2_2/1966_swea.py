# 1966_swea
'''
선택정렬
'''
T = int(input())

for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    print(f'#{tc+1}', end=' ')
    print(*arr)