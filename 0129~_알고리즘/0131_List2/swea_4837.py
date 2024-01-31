# swea_4837
T = int(input())
A = [i for i in range(1, 13)]

for tc in range(T):
    n, k = map(int, input().split())
    cnt = 0
    subsets = []

    for i in range(1<<len(A)):
        subsets.append([A[j] for j in range(len(A)) if (i & (1 << j))> 0])

    subsets = [i for i in subsets if len(i) == n]

    for sub in subsets:
        if sum(sub) == k:
            cnt +=1

    print(f'#{tc+1} {cnt}')