import sys

sys.stdin = open('input.txt', 'r')
N, S = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

l = 0
r = 0
cur_sum = 0
min_len = 1e9

while r < N:
    cur_sum += arr[r]
    r += 1

    while cur_sum >= S :
        min_len = min(min_len, r - l)
        cur_sum -= arr[l]
        l += 1

print(0 if min_len == 1e9 else min_len)

# how
# 누적합 & 슬라이딩 윈도우(X)
# 누적합 and 투 포인터(O)
# 순수 투 포인터(O)

