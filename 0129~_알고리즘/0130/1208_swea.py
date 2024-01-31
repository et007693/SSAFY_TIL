# 1208_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV139KOaABgCFAYh&probBoxId=AY1YYdUalYYDFAWX&type=PROBLEM&problemBoxTitle=240130_List1_2&problemBoxCnt=5

내장 함수를 사용하지 않고 풀이
내장 함수를 사용 못하니까 카운트 정렬을 사용해서 풀어보는 방식을 시도했지만 실패

어려웠던 점
    1. 가장 낮은 박스를 특정 위치로 옮기고 가장 높은 박스에서 빼기
        특정 위치는 어디로 설정해야 하는지
        높은 박스를 어떻게 처리할것인지

    2. 가장 낮은 박스를 다음 index로 옮기기
        높은 박스를 어떻게 처리할것인지

    3. for 문을 써야 하는지 if 문을 써야 하는지 

배운 것
    1. 정렬할 때 index만 사용
    -> for i in arr 대신 for i in range(arr) 사용
'''
for tc in range(10):
    n = int(input())
    boxes = list(map(int, input().split()))

    def min_max():
        max_idx = 0
        min_idx = 0
        for idx in range(1, 100):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            if boxes[idx] < boxes[min_idx]:
                min_idx = idx
        return max_idx, min_idx

    while True:
        max_idx, min_idx = min_max()
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        n -= 1

        if n <= 0:
            break
    max_idx, min_idx = min_max()
    print(f'#{tc+1} {boxes[max_idx] - boxes[min_idx]}')