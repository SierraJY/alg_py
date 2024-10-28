# 이진 탐색 (반드시 정렬되어있어야함)

def solution(nums, target):

    left = 0
    right = len(nums)-1

    while left <= right: #left와 right가 같을 때도 탐색해봐야함
        mid = (left + right) // 2

        if nums[mid] == target : return mid

        elif nums[mid] > target : right = mid-1

        elif nums[mid] < target : left = mid + 1

    return -1


print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))

# 주의할 것
# 왜 left <= right 까지 해야되는지 예시 생각해보기

# 알게된 것
# 이진탐색(이분탐색) : 정렬되어 있는 데이터에서 특정한 값을 찾아내는 알고리즘
# 탐색 범위를 반으로 나누어 찾는 값을 포함하는 범위를 좁혀가는 방식으로 동작