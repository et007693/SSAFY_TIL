# 4843_swea
'''

'''
T = int(input())
 
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
 
    for i in range(n-1):
        max_idx, min_idx = i, i
        for j in range(i+1, n):
            if i % 2 == 1:
                if arr[max_idx] > arr[j]:
                    arr[max_idx], arr[j] = arr[j], arr[max_idx]
            else:
                if arr[min_idx] < arr[j]:
                    arr[min_idx], arr[j] = arr[j], arr[min_idx]
 
    print(f'#{tc+1}', *arr[:10])