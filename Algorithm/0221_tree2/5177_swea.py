# 5177_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXGBNCbaVlUDFARK&probBoxId=AY3EiY6KKq4DFAXh&type=USER&problemBoxTitle=240221_Tree_2&problemBoxCnt=3
완전 이진 트리 개념
enq -> 부모 노드의 값이 항상 자식 노드의 값보다 크도록 만드는 함수
'''
def enq(n):
    global last
    last += 1
    node[last] = n
    c = last
    p = last//2
    while p and node[p] > node[c]:
        node[c], node[p] = node[p], node[c]
        c = p
        p = c // 2

def last_sum(last):
    cnt = 0
    while last:
        last //= 2
        cnt += node[last]
    return cnt

T = int(input())

for tc in range(T):
    n = int(input())
    number = list(map(int, input().split()))
    node = [0] * (n+1)
    last = 0

    for num in number:
        enq(num)
    result = last_sum(n)

    print(f'#{tc+1} {result}')