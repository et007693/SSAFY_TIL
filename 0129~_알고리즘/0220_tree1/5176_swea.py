# 5176_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXR1CohaSRgDFAQT&probBoxId=AY2YXC0qjRsDFAXh&type=USER&problemBoxTitle=240220_Tree_1&problemBoxCnt=3
'''
T = int(input())
def make_tree(t):
    global number
    # 배열이니까 배열크기 넘어가지 않도록
    if t <= n:
        # 왼쪽노드는 현재 인덱스의 2배
        make_tree(t * 2)
        # 더이상 못가면 값넣기
        tree[t] = number
        # 값 넣었으면 증가시키기
        number += 1
        # 우측 노드는 인덱스 2배 + 1
        make_tree(t * 2 + 1)
 
 
for tc in range(T):
    n = int(input())
 
    tree = [0 for i in range(n + 1)]
    number = 1
    make_tree(1)
 
    print(f'#{tc + 1} {tree[1]} {tree[n // 2]}')