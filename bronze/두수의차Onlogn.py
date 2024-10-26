# 두 수의 차가 가장 작은 쌍 찾기
# O(nlogn)으로 풀이할 것
# 정렬된 자료의 특징 확인

def solution(nums):

    # 정렬된 자료의 특징
    # num[i]와 가장 값이 가까운 자료는 num[i-1] or num[i+1]
    nums.sort(reverse=True)

    answer = []
    min_diff = 1e4

    for i in range(0, len(nums)-1):
        diff = nums[i] - nums[i + 1]

        if diff < min_diff:
            answer.clear()
            min_diff = diff
            answer.append(sorted([nums[i+1], nums[i]]))

        elif diff == min_diff:
            answer.append([nums[i+1], nums[i + 1]])

    return answer


print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))
