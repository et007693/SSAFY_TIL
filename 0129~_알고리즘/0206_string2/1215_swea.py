# 1215_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV14QpAaAAwCFAYi&probBoxId=AY15MYu6dNADFAWX&type=PROBLEM&problemBoxTitle=240206_String_2&problemBoxCnt=4
'''
def circular_letter(array, m, n=8):
    cnt = 0

    for i in range(n - m + 1):
        arr = array[i:i + m]
        if arr == arr[::-1]:
            cnt += 1
    return cnt

for tc in range(10):
    m = int(input())
    string = [input() for _ in range(8)]
    cnt = 0

    for i in range(8):
        row = circular_letter(string[i], m)
        col = circular_letter([r[i] for r in string], m)

        if row:
            cnt += row
        if col:
            cnt += col

    print(f'#{tc + 1} {cnt}')