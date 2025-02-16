import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def find_best(honeys, i, now_sum, result):
    global max_honey
    if i == M :
        if now_sum <= C:
            max_honey = max(max_honey, result)
        return

    for j in range(i+1, M+1):
        find_best(honeys, j, now_sum, result)
        find_best(honeys, j, now_sum+honeys[i], result+(honeys[i]**2))

T = int(input())

for t in range(T):

    N, M, C = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    best_matrix = [[0 for _ in range(N - M + 1)] for _ in range(N)]
    total_max_honey = 0

    for r in range(N):
        for c in range(N - M + 1):
            max_honey = 0
            find_best(matrix[r][c:c + M], 0, 0, 0)
            best_matrix[r][c] = max_honey

    for f_r in range(N):
        for f_c in range(N - M + 1):
            f_max_honey = best_matrix[f_r][f_c]

            for s_r in range(f_r, N):
                s_c_start = f_c + M if s_r == f_r else 0
                for s_c in range(s_c_start, N - M + 1):
                    s_max_honey = best_matrix[s_r][s_c]
                    total_max_honey = max(f_max_honey+s_max_honey, total_max_honey)

    print(f"#{t + 1} {total_max_honey}")


# 문제 & 알고리즘
# <벌통 선택 어떻게?>
# => 완전탐색(반복문)
# <각 일꾼의 벌통 선택은 어떻게??>
# => 완전탐색(dfs(재귀))

# 개선한점
# 미리 각 벌통 시작점에서 얻을 수 있는 최대수확을 얻어둔 2차원 배열 사용

