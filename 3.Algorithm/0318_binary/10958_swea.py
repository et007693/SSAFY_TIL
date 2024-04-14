# 10958_swea(퀵 정렬)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXWLcZIqOdgDFAUT&probBoxId=AY4mJvOK_s4DFAUZ&type=USER&problemBoxTitle=240318_%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9_1&problemBoxCnt=4
'''
def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less, equal, greater = [], [], []
    for a in arr:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            greater.append(a)
        else:
            equal.append(a)
    return quick(less) + equal + quick(greater)


T = int(input())
for tc in range(T):
    n = int(input())
    num = list(map(int,input().split()))

    result = quick(num)

    print(f'#{tc+1} {result[n//2]}')