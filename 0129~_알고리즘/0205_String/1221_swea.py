# 1221_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV14jJh6ACYCFAYD&solveclubId=AY1S2R462h4DFAWX&problemBoxTitle=240205_String_1&problemBoxCnt=3&probBoxId=AY13LDfqMhMDFAWX
'''
T = int(input())
lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(T):
    n, l = input().split()
    l = int(l)
    number = list(input().split())

    result = []
    for num in lst:
        for i in range(l):
            if number[i] == num:
                result.append(num)

    print(f"#{tc+1}")
    print(*result)