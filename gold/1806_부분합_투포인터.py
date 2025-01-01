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

# 주의할 점
# 투 포인터의 인덱스 처리가 너무 어려움

# 알게된 것
# 포인터 방식은 크게 두가지 방식이 있는데,
# (1) 앞에서 시작하는 포인터와 끝에서 시작하는 포인터가 만나는 방식 (정렬된 배열에서 주로 사용)
# (2) 두 포인터 모두 앞에서 시작하되 속도가 다르게 움직이는 방식
