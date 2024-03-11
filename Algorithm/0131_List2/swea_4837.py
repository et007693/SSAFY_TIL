# swea_4837
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXO-1Zh6aPEDFAXS&probBoxId=AY1andpK_vQDFAWX&type=USER&problemBoxTitle=240131_List2_1&problemBoxCnt=3

비트 연산자
& : 비트 단위로 and 연산
| : 비트 단위로 or 연산
<< : 피연산자의 비트 열을 왼쪽으로 이동
>> : 피연산자의 비트 열을 오른쪽으로 이동

n = len(arr) # 원소의 갯수
for i in range(1<<n) # 1<<n : 부분 집합의 갯수(2**n)
    for j in range(n): # 원소의 수만큼 비트를 비교
        if i & (1 << j): # i의 j번 비트가 1인 경우
            print(arr[j], end = ",") # j번 원소 출력

어려웠던 점
비트 연산자가 무엇인지, 왜 그런 결과가 나오는지
'''
T = int(input())
A = [i for i in range(1, 13)]

for tc in range(T):
    n, k = map(int, input().split())
    cnt = 0
    subsets = []

    for i in range(1<<len(A)):
        subsets.append([A[j] for j in range(len(A)) if (i & (1 << j))> 0])

    subsets = [i for i in subsets if len(i) == n]

    for sub in subsets:
        if sum(sub) == k:
            cnt +=1

    print(f'#{tc+1} {cnt}')