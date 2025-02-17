import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())


def check_quality(matrix):
    for c in range(W):
        good_col = False
        for r in range(D - K + 1):
            check_cnt = 0
            for i in range(K):
                if matrix[r + i][c] == matrix[r][c]:
                    check_cnt += 1

            if check_cnt == K:
                good_col = True
                break

        if good_col == False:
            return False

    return True


def dfs(now_r, insert_cnt):
    global min_insert_cnt

    if min_insert_cnt <= insert_cnt:
        return

    if check_quality(matrix):
        min_insert_cnt = insert_cnt
        return

    if now_r == D:
        return

    # 현재 행을 임시 저장
    temp = matrix[now_r][:]

    # 약품을 투입하지 않는 경우
    dfs(now_r + 1, insert_cnt)

    # A 약품을 투입하는 경우
    matrix[now_r] = [0] * W
    dfs(now_r + 1, insert_cnt + 1)

    # B 약품을 투입하는 경우
    matrix[now_r] = [1] * W
    dfs(now_r + 1, insert_cnt + 1)

    # 원래 상태로 복구
    matrix[now_r] = temp


for t in range(T):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]

    min_insert_cnt = 1e9

    dfs(0, 0)

    print(f"#{t + 1} {min_insert_cnt}")

# 문제 & 알고리즘
# <각 열에 k개 연속 동일 값이 있는지 확인은 어떻게?>
# 반복문

# <어디에 약품을 넣어야?>
# 완전탐색(DFS(재귀) & 백트래킹)
# 현재의 선택(약품 투입)이 미래에 미치는 영향을 예측할 수 없기 때문

# 일단 순서대로, 특정 행에 넣지 않기, A약품 넣기, B약품 넣기 재귀
# !!!!!처음에는 매트릭스 복사 방식을 사용했음!!!!!!
# 생각해보면 충분히 해당 행만 원복 시킬 수 있음
# 행렬 전체를 복사하는 건 결국 중첩 반복문임
# 가지치기 : 이미 최소 횟수가 구했졌거나, 마지막 까지마 다 해봤을 때,

# <약품 넣기는 어떻게?>
# 반복문

# !!!!주의할 것!!!!
# 매트릭스 자체를 복사해야할 경우도 물론 있겠지만,
# 행만 복사 해두어도 되는 경우가 있을 것