a = int(input())

for i in range(a):
    n, m = map(int, input().split())
    section = list(map(int, input().split()))
    min_section, max_section = sum(section),0
    for s in range(n-m+1):
        if sum(section[s:s+m]) <= min_section:
            min_section = sum(section[s:s+m])
        if sum(section[s:s+m]) >= max_section:
            max_section = sum(section[s:s+m])
    
    print(f'#{i+1} {max_section - min_section}')