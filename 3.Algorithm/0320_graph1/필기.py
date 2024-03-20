def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

N, M = map(int, input().split())
arr = list(map(int, input().split()))
p = [i for i in range(N)]
for i in range(M):
    a, b = arr[i*2], arr[1*2+1]
    union(a,b)

for t in range(1, T+1):
    n, m = map(int, input().split())
 
    parents = [i for i in range(N+1)]
    arr = list(map(int, input().split()))

    for i in range(m):
        l, r = arr[i*2], arr[i*2+1]
        union(l, t)

        ans = [0]*n
        for i in range(1, n+1):
            ans[i-1] = find_set(i)
            