from collections import defaultdict, deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

T = int(input().strip())
for t in range(1, T + 1):
    N = int(input().strip())

    total_e = 0
    coor = defaultdict(deque)
    for _ in range(N):
        x, y, d, e = map(int, input().split())
        coor[(x * 2, y * 2)].append((d, e))

    while len(coor) > 1 :
        for k in list(coor.keys()):
            ele = coor[k].popleft()
            x, y = k[0], k[1]
            d, e = ele[0], ele[1]
            nx, ny = x+dx[d], y+dy[d]
            del coor[k]

            if -2000<= nx <= 2000 and -2000<= ny <= 2000:
                coor[(nx, ny)].append((d,e))
            else:
                N -= 1

        for k in list(coor.keys()):
            if len(coor[k]) >= 2:
                for d, e in coor[k]:
                    total_e += e
                N -= len(coor[k])
                del coor[k]

    print(f"#{t} {total_e}")
