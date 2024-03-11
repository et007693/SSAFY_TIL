# 4834_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXO0qUWay58DFAXS&probBoxId=AY1YYdUalYYDFAWX&type=USER&problemBoxTitle=240130_List1_2&problemBoxCnt=5

내장 함수 사용하지 않고 풀이
가장 많은 값이 두 개 이상 존재할 때 가장 마지막에 있는 index 반환
[::-1]을 사용해서 진행하려 했으나 복잡해서 포기
> 대신 >=를 사용해서 가장 마지막에 있는 값을 출력
'''

T = int(input())

for tc in range(T):
    n = int(input())
    cards = input()

    cnt = [0]*10

    for card in cards:
        cnt[int(card)] += 1

    max_cnt = 0
    for c in range(10):
        if cnt[c] >= max_cnt:
            max_cnt = cnt[c]
            max_idx = c

    print(f'#{tc+1} {max_idx} {max_cnt}')