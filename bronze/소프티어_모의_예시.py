import sys

sys.stdin = open(0, 'r')

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

cnt = 0
size = []


def dfs(coor):
    cnt = 1
    matrix[coor[0]][coor[1]] = 'c'

    for d in range(4):
        nr = coor[0] + dr[d]
        nc = coor[1] + dc[d]
        if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == 1:
            cnt += dfs((nr, nc))

    return cnt


for r in range(N):
    for c in range(N):
        if matrix[r][c] == 1:
            cnt += 1
            size.append(dfs((r, c)))

size.sort()
print(cnt)
for s in size:
    print(s, end=" ")