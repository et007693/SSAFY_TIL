# 4864_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXQhKu6KwW0DFAXS&probBoxId=AY13LDfqMhMDFAWX&type=USER&problemBoxTitle=240205_String_1&problemBoxCnt=2
'''
T = int(input())

for tc in range(T):
    s1 = input()
    s2 = input()
    cnt = 0

    for s in s2.split(s1):
        cnt += 1

    if cnt >= 2:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')

# 2 - 구간합 이용
# T = int(input())

# for tc in range(T):
#     s1 = input()
#     s2 = input()
#     length_s1 = 0
#     length_s2 = 0
#     result = 0

#     for s in s1:
#         length_s1 += 1
#     for s in s2:
#         length_s2 += 1

#     for i in range(length_s2-length_s1+1):
#         print(f's2 : {s2[i:i+length_s1]}, s1 : {s1}')
#         if s2[i:i+length_s1] == s1:
#             result = 1

#     print(f'#{tc+1} {result}')