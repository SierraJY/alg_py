import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
K = int(input())

def count_turon_row(matrix):
    global max_turnon_row_cnt

    turnon_row_cnt = 0
    for r in matrix:
        if sum(r) == M:
            turnon_row_cnt += 1

    if turnon_row_cnt > max_turnon_row_cnt:
        max_turnon_row_cnt = turnon_row_cnt

    return

def switch_column(matrix, now_c):
    for r in range(N):
        if matrix[r][now_c] == 0:
            matrix[r][now_c] = 1
        else:
            matrix[r][now_c] = 0

def switch_dfs(matrix, now_k):

    if now_k == K :
        count_turon_row(matrix)
        return

    if M == 1 :
        if K % 2 == 0 :
            count_turon_row(matrix)
            return
        else:
            if now_k == 1:
                count_turon_row(matrix)
                return

    if now_k > max_case_cnt :
        count_turon_row(matrix)
        return

    for next_c in range(M):
        switch_column(matrix, next_c)
        switch_dfs(matrix, now_k +1)
        switch_column(matrix, next_c)

max_turnon_row_cnt = 0
max_case_cnt = M**M
switch_dfs(matrix, 0)
print(max_turnon_row_cnt)

# 틀린이유
# 완전탐색 : dfs(재귀) + 백트래킹로 구현하려 했음
# 코드 자체는 틀린 것 같지 않음
# 그런데 문제 조건을 읽었었나..??????????
# 어떤 완전 탐색인지 고민했었나? 순열인지 중복순열인지????
# 중복순열로 최악의 경우 50**1000임
