import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
requires = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

left = 0
right = max(requires)

def requires_cutted_sum(mid):
    sum = 0
    for r in requires:
        if r <= mid : sum += r
        else : sum += mid
    return  sum

while left <= right:
    mid = (left+right)//2
    sum = requires_cutted_sum(mid)

    if sum <= M :
        left = mid + 1
    else:
        right = mid-1

print(right)


# what
# 배정된 예산들 중 최댓값
# 모든 요청이 배정될 수 있는 경우, 요청한 금액을 그대로 배정
# 모든 요청이 배정될 수 없는 경우, 특정한 정수 상한액을 계산,
# 그 이상인 예산요청에는 모두 상한액을 배정,
# 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정

# how
# bisect