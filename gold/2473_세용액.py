import sys

sys.stdin = open(0, 'r')
input = sys.stdin.readline

N = int(input())

liquids = list(map(int, input().split()))
liquids.sort()

min_diff = float('inf')
min_l = 0
min_r = 0
min_rest = 0

for i in range(N):
    new_liquids = liquids[:i] + liquids[i+1:]
    l = 0
    r = N-2

    while l < r:
        total = liquids[i] + new_liquids[l] + new_liquids[r]

        if abs(total) < min_diff:
            min_diff = abs(total)
            min_l = new_liquids[l]
            min_r = new_liquids[r]
            min_rest = liquids[i]

        if total < 0:
            l += 1
        elif total > 0:
            r -= 1
        else:
            break

result = [min_l, min_rest, min_r]
result.sort()
print(" ".join(map(str, result)))


# 아이디어 & 알고리즘
# 3가지 용액 어떻게 혼합?

# 2가지면?
# => 투 포인터, 이분 탐색..인 것 같은데

# 3가지면?
# => 2가지 찾고 한 가지 찾기? X
# -99, -5, 3, 5, 96

# => 한가지 고정하고 2가지 찾기?

# 주의할 것
# 틀린 이유 1
# 최대값 초기 설정 1e9로 하면 틀림