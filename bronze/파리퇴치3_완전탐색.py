T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    for i in range(N):
        for j in range(N):

            # +
            plus_sum = matrix[i][j]
            for k in range(1, M):
                # 상
                if i - k >= 0:
                    plus_sum += matrix[i - k][j]
                # 하
                if i + k < N:
                    plus_sum += matrix[i + k][j]
                # 좌
                if j - k >= 0:
                    plus_sum += matrix[i][j - k]
                # 우
                if j + k < N:
                    plus_sum += matrix[i][j + k]

            # X
            x_sum = matrix[i][j]
            for k in range(1, M):
                # 좌상
                if i - k >= 0 and j - k >= 0:
                    x_sum += matrix[i - k][j - k]
                # 우상
                if i - k >= 0 and j + k < N:
                    x_sum += matrix[i - k][j + k]
                # 좌하
                if i + k < N and j - k >= 0:
                    x_sum += matrix[i + k][j - k]
                # 우하
                if i + k < N and j + k < N:
                    x_sum += matrix[i + k][j + k]

            max_sum = max(max_sum, plus_sum, x_sum)

    print(f"#{t} {max_sum}")

# 주의할 것
# 모든 위치에서 스프레이가 분사될 수 있음을 고려해야함
