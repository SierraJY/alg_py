import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
K = int(input())

zero_cnt_each_row = [0 for _ in range(N)]
for r in range(N):
    zero_cnt_each_row[r] = M - sum(matrix[r])

max_turnon_cnt = 0
for r in range(N):
    if zero_cnt_each_row[r] <= K and zero_cnt_each_row[r]%2 == K%2:
        same_row_cnt = 0
        flag_row = "".join(map(str,matrix[r]))
        for r2 in range(N):
            compare_row = "".join(map(str,matrix[r2]))
            if flag_row == compare_row :
                same_row_cnt += 1
        max_turnon_cnt = max(max_turnon_cnt,same_row_cnt)

print(max_turnon_cnt)

# 한 행이 모두 켜질 수 있는 조건은
# 한 행의 0의 개수가 K보다 작고, K가 짝수이면 0의 개수도 짝수, 홀수이면 0의 개수도 홀수