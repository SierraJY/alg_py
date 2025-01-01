import sys

sys.stdin = open('input.txt', 'r')

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

N , M , K = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    matrix[r-1][c-1] = 1

def dfs() :
    size = 1
    while stack:
        (r,c) = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 1:
                size += 1
                matrix[nr][nc] = 'c'
                stack.append((nr,nc))

    return size

biggest_size = 0
stack = []

for r in range(N):
    for c in range(M):
        if matrix[r][c] == 1:
            matrix[r][c] = 'c'
            stack.append((r,c))
            biggest_size = max(biggest_size, dfs())

print(biggest_size)



# what
# 서로 상하좌우로 들러 붙은 음식물의 가장 큰 크기

# how
# dfs & 구현

# 주의할 것
# 체크완료 해두는 코드