a = int(input())

for i in range(a):
    n = int(input())
    num = list(map(int, input().split()))
    
    max_num = 0
    min_num = num[0]

    for n in num:
        if n >= max_num:
            max_num = n
        if n <= min_num:
            min_num = n

    print(f'#{i+1} {max_num - min_num}')