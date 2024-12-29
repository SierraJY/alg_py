import sys

sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())

matrix = [[0 for _ in range(N+1)]]
for _ in range(N):
    matrix.append([0] + list(map(int, sys.stdin.readline().split())))

prefix_matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_matrix[i][j] = matrix[i][j] + prefix_matrix[i][j-1] + prefix_matrix[i-1][j] - prefix_matrix[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    print(prefix_matrix[x2][y2] - prefix_matrix[x2][y1-1] - prefix_matrix[x1-1][y2] + prefix_matrix[x1-1][y1-1])


# how
# 누적합과 구간합