# 4839_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXO-6AsaadgDFAXS&probBoxId=AY1andpK_vUDFAWX&type=USER&problemBoxTitle=240201_List2_2&problemBoxCnt=5
'''
T = int(input())

for tc in range(T):
    p, a, b = map(int, input().split())
    
    cnt_a = 0
    cnt_b = 0
    result = ''

    def binary(start, end, key):
        cnt = 0
        center = (start+end)//2
        while center != key:
            if key < center:
                end = center
                center = (start + center)//2
            elif key > center:
                start = center
                center = (end + center)//2
            cnt += 1
        return cnt

    cnt_a = binary(1, p, a)
    cnt_b = binary(1, p, b)

    if cnt_a > cnt_b:
        result = 'A'
    elif cnt_b > cnt_a:
        result = 'B'
    else:
        result = 0

    print(f'#{tc+1} {result}')


    