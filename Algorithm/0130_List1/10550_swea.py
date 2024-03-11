# # 10550_swea
# '''
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXOvCK76mlUDFAXS&solveclubId=AY1S2R462h4DFAWX&problemBoxTitle=240130_List1_2&problemBoxCnt=5&probBoxId=AY1YYdUalYYDFAWX
# '''
# T = int(input())

# for tc in range(T):
#     cards = input()
#     cnt = [0] * 10
#     # result = 0
#     tripleple = 0
#     run_cnt = 0

#     for c in cards:
#         cnt[int(c) - 1] += 1

#     for i in range(10):
#         while cnt[i] >= 3:
#             cnt[i] -= 3
#             tripleple += 1

#     for i in range(1, 9):
#         if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
#             run_cnt += 1
#             cnt[i] -= 1
#             cnt[i+1] -= 1
#             cnt[i+2] -= 1

#     if tripleple + run_cnt == 2:
#         print(f'#{tc + 1} Baby Gin')
#     else:
#         print(f'#{tc + 1} Lose')

T = int(input())

for tc in range(T):
    cards = input()
    cnt = [0] * 10
    triple = 0
    run_cnt = 0

    for i in range(10):
        triple += cnt[i] // 3
        cnt[i] %= 3

    for i in range(1, 8):
        while True:
            if cnt[i] >= 1 and cnt[i + 1] >= 1 and cnt[i + 2] >= 1:
                cnt[i] -= 1
                cnt[i + 1] -= 1
                cnt[i + 2] -= 1
                run_cnt += 1
            else:
                break
            
    if triple + run_cnt >= 2:
        print(f'#{tc+1} Baby Gin')
    else:
        print(f'#{tc+1} Lose')