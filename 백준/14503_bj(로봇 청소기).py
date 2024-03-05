# 14503_bj(로봇 청소기)
'''
https://www.acmicpc.net/problem/14503
'''
import time

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def check(start): # 4방향 확인
    x, y = start
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < m and 0 <= my < n: # 범위 안에 있고
            # 청소 여부 확인
            if room[my][mx] == 1: # 청소가 되어 있는경우
                continue # 계속 진행
            else: # 청소되지 않은 칸이 있는 경우
                return False
    return True # 4 방향이 모두 청소가 되어 있다면 True 반환

def clean(start, d):
    # time.sleep(0.3)
    global clean_cnt
    print(start, d)
    x, y = start
    if room[y][x] == 0:
        room[y][x] = 1
        clean_cnt += 1

    result = check(start)
    print(result)

    if result:
        # 뒤로 한칸, 방향 고정 -> (d+2)%4
        if 0 <= x + dx[(d+2)%4] < m and 0 <= y + dy[(d+2)%4] < n:
            clean([x + dx[(d+2)%4], y + dy[(d+2)%4]], d)
        else:
            return
    else:
        d = ((d - 1) + 4) % 4
        if room[y+dy[d]][x + dx[d]] == 0:
            print('turn', d)
            x += dx[d]
            y += dy[d]
            clean([x,y], d)

        # while room[y+dy[((d-1)+4) % 4]][x+dx[((d-1)+4) % 4]] == 1:
        #     print([x, y], d)
            # print(d)
        # x += dx[d]
        # y += dy[d]
        # clean([x, y], d)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
clean_cnt = 0

clean([r, c], d)

print(clean_cnt)
print(room)