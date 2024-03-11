# 1389_케빈베이컨의 6단계 법칙
'''
https://www.acmicpc.net/problem/1389
index 처리 때문에 고민한 문제
bfs는 어느정도 이해가 된듯
'''
def bfs(start):
    que = [start]
    while que:
        point = que.pop(0)
        for f in friends[point]:
            if cnt[start][f] == 0 and f != start:
                que.append(f)
                cnt[start][f] = cnt[start][point]+1

n, m = map(int, input().split())
friends = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)

cnt = [[0]*n for _ in range(n)]
for i in range(n):
    bfs(i)

cnt_sum = [sum(i) for i in cnt]
print(cnt_sum.index(min(cnt_sum))+1)