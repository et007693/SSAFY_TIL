# 2071_swea

T = int(input())

for tc in range(T):
    number = list(map(int, input().split()))
    s = 0
    cnt = 0

    for n in number:
        s += n
        cnt += 1

    if s/cnt - int(s/cnt) >= 0.5:
        avg = int(s/cnt) + 1
    else:
        avg = int(s/cnt)

    print(f'#{tc+1} {avg}')