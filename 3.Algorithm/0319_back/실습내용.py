# arr = [i for i in range(1, 4)]
# path = [0] * 3

# def dfs(level):
#     if level == 3:
#         return
        
#     for i in range(len(arr)):
#         if arr[i] not in path:
#             continue

#         path[level] = arr[i]
#         dfs(level + 1)
#         path[level] = 0

# dfs(0)

def dfs(i, s, li):
    if i == 9 or s > 10:
        return

    if s == 10:
        print(li)
        return
    
    dfs(i+1, s+arr[i], li+str(arr[i]))
    dfs(i+1, s, li)


arr = [i for i in range(1, 11)]

dfs(0, 0, '')
