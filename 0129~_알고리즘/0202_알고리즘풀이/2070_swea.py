# 2070_swea

T = int(input())

for tc in range(T):
    a, b = map(int, input().split())

    if a == b:
        result = '='
    elif a > b:
        result = '>'
    else:
        result = '<'

    print(f'#{tc+1} {result}')