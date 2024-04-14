# 20349_swea(국민셔플)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AY3jpQ8qXZ8DFARM&probBoxId=AY3g3meKDkYDFAUZ&type=USER&problemBoxTitle=240226_%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B42&problemBoxCnt=5
'''
def overhand():
    over = int(n*0.37)
    for _ in range(over):
        card.insert(0, card.pop())

def perfect():
    cnt = int(n*0.5)
    back = []
    for _ in range(cnt):
        back.insert(0, card.pop())

    i = 0
    while back:
        card.insert(2*i+1, back.pop(0))
        i += 1


T = int(input())

for tc in range(T):
    n, t = map(int, input().split())
    card = [i for i in range(1, n+1)]

    for _ in range(t):
        overhand()
        perfect()

    print(f'#{tc+1}', *card, sep=' ')
