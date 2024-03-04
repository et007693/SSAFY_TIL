# 2579_bj(계단 오르기)
'''
https://www.acmicpc.net/problem/2579
'''
# 시간초과
# import sys

# def jump(i, s, cnt):
#     global result
#     if i == n:
#         if s >= result:
#             result = s
#         return
#     if cnt < 2:
#         jump(i+1, s+stair[i], cnt+1)
#         jump(i+1, s, cnt=0)
#     else:
#         jump(i+1, s, cnt=0)

# n = int(input())
# stair = [int(sys.stdin.readline()) for _ in range(n)]
# result = 0

# jump(0,0,0)

# print(result)

n = int(input())
stair = [0]*301
for i in range(n):
    stair[i] = int(input())

dp = [0]*301

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n):
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[n-1])