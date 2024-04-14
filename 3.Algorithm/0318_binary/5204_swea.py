# 5204_swea(병합 정렬)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXWH8zeazMADFAUT&probBoxId=AY4mJvOK_s4DFAUZ&type=USER&problemBoxTitle=240318_%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9_1&problemBoxCnt=4
'''
def division(arr):
    global cnt
    if len(arr) == 1:
        return arr

    left, right = division(arr[:len(arr)//2]), division(arr[len(arr)//2:])
    l_idx, r_idx = 0, 0
    result = []

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1
            if r_idx == len(right):
                cnt += 1

    result += left[l_idx:]
    result += right[r_idx:]

    return result

T = int(input())
for tc in range(T):
    n = int(input())
    num = list(map(int,input().split()))
    cnt = 0
    result = division(num)

    print(f'#{tc+1} {result[n//2]} {cnt}')