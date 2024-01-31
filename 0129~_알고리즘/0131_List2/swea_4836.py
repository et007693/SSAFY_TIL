# swea_4836
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXO-0JJaaLYDFAXS&probBoxId=AY1andpK_vQDFAWX&type=USER&problemBoxTitle=240131_List2_1&problemBoxCnt=3

파리퇴치를 풀고 와서 어렵진 않았음
'겹쳐진다'는 2차원의 의미인데 1차원인 좌표의 개념으로 환산하는 생각의 전환이 필요
-> 두 개의 도형에 같은 좌표가 존재할 때 '겹친다'
빨강과 파랑의 좌표가 겹치는 갯수를 세는 방식으로 진행 
각 좌표에 color 값을 더하는 방식도 괜찮아 보였음
'''

T = int(input())

for tc in range(T):
    n = int(input())
    cnt = 0
    red = set()
    blue = set()

    for _ in range(n):
        point = list(map(int, input().split()))
        tmp = []

        for x in range(point[2] - point[0]):
            for y in range(point[3] - point[1]):
                tmp.append((point[0]+x, point[1]+y))
            
        if point[-1] == 1:
            red.add(tmp)
        else:
            blue.add(tmp)
        
    for r in red:
        for b in blue:
            if r == b:
                cnt += 1
    
    print(f'#{tc+1} {cnt}')