# 1231_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV140YnqAIECFAYD&probBoxId=AY2YXC0qjRsDFAXh&type=PROBLEM&problemBoxTitle=240220_Tree_1&problemBoxCnt=3
'''
def mid_order(root):
    root = int(root)-1
    if len(tree[root]) == 4:
        mid_order(tree[root][2])
        print(tree[root][1], end='')
        mid_order(tree[root][3])
    elif len(tree[root]) == 3:
        mid_order(tree[root][2])
        print(tree[root][1], end='')
    else:
        print(tree[root][1], end='')

for tc in range(10):
    n = int(input())
    tree = [input().split() for _ in range(n)]

    print(f'#{tc+1}', end=' ')
    mid_order(1)
    print()