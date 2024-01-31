# swea_4836

T = int(input())

for tc in range(T):
    n = int(input())
    cnt = 0
    red = set()
    blue = set()
    

    for _ in range(n):
        point = list(map(int, input().split()))
        tmp = []

        for x in range(point[2] - point[0]):
            for y in range(point[3] - point[1]):
                tmp.append((point[0]+x, point[1]+y))
            
        if point[-1] == 1:
            red.add(tmp)
        else:
            blue.add(tmp)
        
    for r in red:
        for b in blue:
            if r == b:
                cnt += 1
    
    print(f'#{tc+1} {cnt}')