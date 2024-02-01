# 10550_swea
'''

'''
T = int(input())

for tc in range(T):
    cards = input()
    cnt = [0] * 9
    result = 0

    for c in cards:
        cnt[int(c) - 1] += 1

    for i in range(9):
        if cnt[i] >= 6:
            result += 2
            break
        elif cnt[i] >= 3:
            result += 1
            cnt[i] -= 3

    for i in range(6):
        if cnt[i]*cnt[i+1]*cnt[i+2] != 0 and cnt[i]+cnt[i+1]+cnt[i+2] >= 3:
            result += 1
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1

    if result == 2:
        print(f'#{tc + 1} Baby Gin')
    else:
        print(f'#{tc + 1} Lose')
