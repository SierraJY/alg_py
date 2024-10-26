# 현수는 사탕을 좋아합니다 현수에게 사탕이 n개 있습니다
# 현수 엄마는 현수가 요즘 너무 사탕을 많이 먹어 건강에 좋지 않다고 생각해 현수에게 가지고
# 있는 사탕의 절반 (n/2)개만 먹으라고 했습니다 n은 항상 짝수입니다
# 매개변수 nums에 현수가 가지고 있는 n개의 사탕의 종류 정보가 주어지면
# 현수가 n/2개의 사탕을 먹는다면 최대 몇 종류의 사탕을 먹을 수 있는지를 반환하는 프로그램을 작성하세요.

# Set으로 풀이 가능

from collections import deque

def solution(nums):

    n = len(nums)
    nums.sort()
    no_dup = deque()

    i = 0
    while i < n:
        if i < n-1 and nums[i] == nums[i+1]:
            i += 1
            continue
        no_dup.append(nums[i])
        i += 1

    return len(no_dup) if len(no_dup) < n//2 else n//2

print(solution([2, 1, 1, 3, 2, 3, 1, 2]))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solution([100, 200, 300, 400, 500, 600, 700, 800]))
