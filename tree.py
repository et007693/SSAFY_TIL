def pre_order(t):
    if t:
        print(t)
        pre_order(left[t])
        pre_order(right[t])


n = int(input())
arr = list(map(int, input().split()))
left = [0]*(n+1)
right = [0]*(n+1)
par = [0]*(n+1)

for i in range(n):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = n
while par[c] != 0:
    c = par[c]
root = 0
print(root)
pre_order(root)