# 1697_bj(숨바꼭질)
'''
https://www.acmicpc.net/problem/1697
'''
# DFS는 시간초과 -> BFS로 풀어야 함
# def dfs(p, cnt):
#     global result
#     if cnt > result:
#         return

#     if p >= k:
#         cnt += p-k
#         if result > cnt:
#             result = cnt
#         return

#     elif p > 0:
#         dfs(p*2, cnt+1)
#         dfs(p+1, cnt+1)
#         dfs(p-1, cnt+1)

# n, k = map(int, input().split())
# result = 100001
# dfs(n, 0)

# print(result)