# N 개의 카드가 일렬로 놓여져 있습니다 각 카드에는 숫자가 적혀있습니다
# 현수는 카드가 일렬로 놓여진 줄의 양 끝 즉 왼쪽 맨 끝카드와
# 오른쪽 맨 끝 카드 둘 중 하나를 가져갈 수 있습니다.
# 현수는 양 끝에서 가져가는 방식으로 k개의 카드를 가져갈 수 있습니다
# 그리고 가져간 카드에 적혀진 숫자의 총합이 현수가 얻는 점수입니다
# 일려로 놓여진 각 카드의 숫자가 매개변수 nums에 주어지고
# 현수가 가져갈 수 있는 카드의 개수 k가 주어지면 현수가 얻을 수 있는
# 최대 점수를 반환하는 프로그램을 작성하시오

def solution(nums, k):

    total_sum = sum(nums)
    not_selected_cnt = len(nums)-k

    min_sum_not_selected = sum(nums[:not_selected_cnt]) # 첫 번째 슬라이딩 윈도우 값들의 합

    for i in range(1, k+1):
        min_sum_not_selected = min(min_sum_not_selected, sum(nums[i:i + not_selected_cnt]))

    return total_sum - min_sum_not_selected

print(solution([1,2,3,4], 2))
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))

# how
# 가져갈 수 없는 카드 개수만큼의 크기의 슬라이딩 윈도우를 움직이며
# 가져갈 수 없는 카드 개수의 최소합을 찾는다 => 가져갈 수 있는 카드로는 최대합을 찾을 수 있음

# 그리디 방식으로 하면 틀림
# 슬라이딩 윈도우 방식 O(n)
# 슬라이딩 윈도우가 선택하는 카드들은 선택되지 않는 카드들임