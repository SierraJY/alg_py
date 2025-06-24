# note : 문제에서 "첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지를 출력한다."라고 했는데,
# 최종 출력에서만 나누면 '시간 초과'
# 세그먼트 트리에 갑 추가 or 업데이트 될 때 마다 미리 나머지로 넣어 두면 해결
# 계산 중 매우 큰 수가 연산되기 때문에 시간초과 발생했을 것으로 추정

# note : 모듈로 연산 성질
# (a * b) % MOD = ((a % MOD) * (b % MOD)) % MOD

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

MOD = 1000000007

N, M, K = map(int, input().split())

origin_arr = [int(input()) for _ in range(N)]
seg_tree = [1 for _ in range(N * 4)]


def make_tree(start, end, node_i):
    if start == end:
        seg_tree[node_i] = origin_arr[start]
        return seg_tree[node_i]

    mid = (start + end) // 2
    left = make_tree(start, mid, node_i * 2)
    right = make_tree(mid + 1, end, node_i * 2 + 1)

    seg_tree[node_i] = left * right
    return seg_tree[node_i]


def update(start, end, node_i, change_i, new_val):
    if change_i < start or end < change_i:
        return seg_tree[node_i]

    if start == end:
        seg_tree[node_i] = new_val
        return seg_tree[node_i]

    mid = (start + end) // 2
    left = update(start, mid, node_i * 2, change_i, new_val)
    right = update(mid + 1, end, node_i * 2 + 1, change_i, new_val)

    seg_tree[node_i] = left * right
    return seg_tree[node_i]


def query(start, end, node_i, l, r):
    if r < start or end < l:
        return 1

    if l <= start and end <= r:
        return seg_tree[node_i]

    mid = (start + end) // 2
    left = query(start, mid, node_i * 2, l, r)
    right = query(mid + 1, end, node_i * 2 + 1, l, r)

    return left * right


# 세그먼트 트리 초기화
make_tree(0, N - 1, 1)

# 쿼리 처리
for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:  # 업데이트 쿼리
        update(0, N - 1, 1, b - 1, c)
        origin_arr[b - 1] = c
    else:  # 곱셈 쿼리
        print(query(0, N - 1, 1, b - 1, c - 1) % MOD)