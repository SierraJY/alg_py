from itertools import combinations

T = int(input())

for t in range(T):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    min_sum = 1e9

    for i in range(1, 1<<N):
        sum_h = 0

        for j in range(N):
            if i & (1<<j):
                sum_h += H[j]

        if sum_h >= B:
            min_sum = min(min_sum, sum_h)

    print(f"#{t+1} {min_sum - B}")

# how
# 비트마스크

# 알아야할 것
# 비트마스크 연산자