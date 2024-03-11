# 2063_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AV5QPsXKA2UDFAUq&probBoxId=AY1arnWaAEQDFAWX&type=PROBLEM&problemBoxTitle=D1+%EB%AC%B8%EC%A0%9C+_+%ED%95%84%EC%88%98+%EC%95%84%EB%8B%98&problemBoxCnt=11
'''
n = int(input())
number = list(map(int, input().split()))

mid = n // 2
for i in range(n-1):
    for j in range(i, n):
        if number[i] < number[j]:
            number[j], number[i] = number[i], number[j]
            
print(number[mid])