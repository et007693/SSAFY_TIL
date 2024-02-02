# swea_2072

T = int(input())

for tc in range(T):
    number = list(map(int, input().split()))
    num = [n for n in number if n % 2 == 1]

    print(f'#{tc+1} {sum(num)}')