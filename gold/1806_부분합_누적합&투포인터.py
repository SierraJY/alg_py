import sys

sys.stdin = open('input.txt', 'r')
N, S = map(int, sys.stdin.readline().split())

# 입력 배열 앞에 0을 추가하여 1-based indexing 사용
arr = [0] + list(map(int, sys.stdin.readline().split()))

# 누적합 배열 생성
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

left = 0
right = 1
min_len = 1e9

while right <= N:
    current_sum = prefix_sum[right] - prefix_sum[left]
    if current_sum >= S:
        min_len = min(min_len, right-left)
        left += 1
    else:
        right += 1

print(0 if min_len == 1e9 else min_len)

# how
# 누적합 & 슬라이딩 윈도우(X)
# 누적합 and 투 포인터(O)
# 순수 투 포인터(O)

