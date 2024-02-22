# 9920_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY1S2R462h4DFAWX&contestProbId=AXHBYZt64wUDFARK&probBoxId=AY3EiucKKtYDFAXh&type=USER&problemBoxTitle=240222_Start_1&problemBoxCnt=4
'''
# 방법 1
binary_dict = {
        '0': '0000',
        '1': '0001', 
        '2': '0010', 
        '3': '0011',
        '4': '0100', 
        '5': '0101', 
        '6': '0110', 
        '7': '0111',
        '8': '1000', 
        '9': '1001', 
        'A': '1010', 
        'B': '1011',
        'C': '1100',
        'D': '1101', 
        'E': '1110', 
        'F': '1111'
    }

T = int(input())

for tc in range(T):
    n, string = input().split()

    for s in range(int(n)):
        print(bin(string[s]))

# 방법 2
# T = int(input())

# for tc in range(T):
#     n, string = input().split()
#     result = ''
#     for s in range(int(n)):
#         result += (str(bin(int(string[s], 16)))[2:].zfill(4))
#     print(f'#{tc+1} {result}')