# 5178_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXGBNCbaVlUDFARK&probBoxId=AY3EiY6KKq4DFAXh&type=USER&problemBoxTitle=240221_Tree_2&problemBoxCnt=3
재귀 연습
DP 문제 풀기
재귀로 푸는 연습하기
'''
def s(p):
    if p <= n:
        node[p] += s(p*2)
        node[p] += s(p * 2+1)
        return node[p]
    else:
        return 0

T = int(input())

for tc in range(T):
    n, m, l = map(int, input().split())
    node = [0] * (n+1)

    for _ in range(m):
        c, num = map(int, input().split())
        node[c] = num

    s(l)

    print(f'#{tc+1} {node[l]}')