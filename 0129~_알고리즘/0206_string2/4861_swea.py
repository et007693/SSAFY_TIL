# 4861_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXQhOG1qYbMDFAXS&probBoxId=AY15MYu6dNADFAWX&type=USER&problemBoxTitle=240206_String_2&problemBoxCnt=3
문자열이 같은지 확인할 때 arr[::-1] 사용하기!
'''
'''
arr[::-1] 사용하지 않았을 때 코드

T = int(input())
 
def circular_letter(array, n, m):
    num = m//2
    circular = ''
 
    for i in range(n-m+1):
        arr = array[i:i+m]
        for j in range(num):
            if arr[j] != arr[-j-1]:
                break
            elif j == num-1:
                circular = arr
    return circular
'''

T = int(input())

def circular_letter(array, n, m):
    num = m//2
    circular = ''

    for i in range(n-m+1):
        arr = array[i:i+m]
        if arr == arr[::-1]:
            circular = arr
    return circular

for tc in range(T):
    n, m = map(int, input().split())
    string = [input() for _ in range(n)]
    result = ''

    for i in range(n):
        row = circular_letter(string[i], n, m)
        col = circular_letter([r[i] for r in string], n, m)

        if row:
            result = row
            break
        if col:
            result = col
            break

    print(f'#{tc+1} ', *result, sep='')
