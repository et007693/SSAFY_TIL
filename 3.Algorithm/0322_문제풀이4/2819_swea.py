# 2819_swea(격자판의 숫자 이어 붙이기)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV7I5fgqEogDFAXB&probBoxId=AY4mKUKa_twDFAUZ&type=PROBLEM&problemBoxTitle=240322_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B44&problemBoxCnt=8
'''
def dfs(c, x, y, s):
    if c == 7:
        if s not in verify:
            verify.append(s)
        return

    for dx, dy in [0, 1], [0, -1], [1, 0], [-1, 0]:
        mx = x + dx
        my = y + dy
        # mx, my = x + dx, y + dy
        if 0 <= mx < 4 and 0 <= my < 4:
            dfs(c+1, mx, my, s+str(arr[y][x]))

T = int(input())

for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)]
    verify = []
    cnt = 0

    for x in range(4):
        for y in range(4):
            dfs(1, x, y, str(arr[y][x]))

    print(verify)
    print(f'#{tc+1} {len(verify)}')