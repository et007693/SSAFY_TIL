# 5247_swea(연산)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXI1FK3qVisDFAXR&probBoxId=AY4mJ5Tq_tIDFAUZ&type=USER&problemBoxTitle=240320_%EA%B7%B8%EB%9E%98%ED%94%84_1&problemBoxCnt=2
bfs에서 queue에 넣는 새로운 방식
list에 값을 저장해서, 조건에 맞는 값만 q에 append하는 방식
'''
def bfs(s, c):
    visited = [1000001] * 1000001
    q = [(s, c)]
    while q:
        s, c = q.pop(0)
        if s == m:
            return c

        operations = [s+1, s-1, s*2, s-10]
        for num in operations:
            if 0 < num <= 1000000 and c < visited[num]:
                visited[num] = c
                q.append((num, c+1))

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    cnt = bfs(n, 0)
    print(f'#{tc+1} {cnt}')