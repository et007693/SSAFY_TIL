# 2068_swea

T = int(input())

for tc in range(T):
    number = list(map(int, input().split()))

    max_idx = 0
    for num in range(10):
        if number[max_idx] < number[num]:
            max_idx = num

    print(f'#{tc+1} {number[max_idx]}')