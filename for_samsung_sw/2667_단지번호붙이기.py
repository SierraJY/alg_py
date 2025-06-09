import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
matrix = [input().strip() for _ in range(N)]

chunk_cnt = 0
house_cnt = []


dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
visited = [[False for _ in range(N)] for _ in range(N)]

def dfs(a):
    visited[a[0]][a[1]] = True
    cnt = 1

    for d in range(4):
        nr = a[0] + dr[d]
        nc = a[1] + dc[d]
        if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == '1' and visited[nr][nc] == False:
            cnt += dfs((nr,nc))

    return cnt

for r in range(N):
    for c in range(N):
        if matrix[r][c] == '1' and visited[r][c] == False:
            chunk_cnt += 1
            house_cnt.append(dfs((r,c)))

print(chunk_cnt)
house_cnt.sort()
for c in house_cnt:
    print(c)

