def solution(nums, target):
    answer = [0,0]

    nums.sort()

    left_idx = 0
    right_idx = len(nums)-1

    while left_idx < right_idx:
        sum = nums[right_idx] + nums[left_idx]
        if sum < target:
            left_idx += 1
        elif sum > target:
            right_idx -=1
        else:
            answer = [nums[left_idx], nums[right_idx]]
            break

    return answer


print(solution([3, 7, 2, 12, 9, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))
