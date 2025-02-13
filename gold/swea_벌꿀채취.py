import sys
from itertools import combinations

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def find_best(honeys):
    max_sum = 0
    best_comb = None

    for r in range(len(honeys), 0, -1):
        combs = combinations(honeys, r)
        for comb in combs:
            if sum(comb) > C:
                continue
            else:
                if sum(map(lambda x: x ** 2, comb)) > max_sum:
                    best_comb = comb
                    max_sum = sum(map(lambda x: x ** 2, best_comb))

    return best_comb


T = int(input())

for t in range(T):

    N, M, C = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_honey = 0

    for f_r in range(N):
        for f_c in range(N - M + 1):
            getted_f = find_best(matrix[f_r][f_c:f_c + M])

            for s_r in range(f_r, N):
                s_c_start = f_c + M if s_r == f_r else 0
                for s_c in range(s_c_start, N - M + 1):
                    getted_s = find_best(matrix[s_r][s_c:s_c + M])

                    tmp_total = 0
                    for h in getted_f + getted_s:
                        tmp_total += (h ** 2)

                    max_honey = max(tmp_total, max_honey)

    print(f"#{t + 1} {max_honey}")


# 문제 & 알고리즘
# <벌통 선택 어떻게?>
# => 완전탐색(반복문)
# <각 일꾼의 벌통 선택은 어떻게??>
# => 완전탐색(조합)
# <똑같은 선택지 ?>
# 프루닝