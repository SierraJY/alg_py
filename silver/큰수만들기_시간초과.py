def solution(number, k):
    nums = [int(c) for c in number]
    LEN = len(nums)

    new_nums = []
    left = 0 # 선택할 수 있는 숫자들 시작점
    right = k + 1 # 선택할 수 없는 숫자들 시작점

    for _ in range(LEN-k):
        tmp_max = max(nums[left:right])
        new_nums.append(str(tmp_max))
        tmp_max_idx = left + nums[left:right].index(tmp_max)

        left = tmp_max_idx + 1
        right += 1

    return "".join(new_nums)

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))

# what
# number에섯 숫자 두 개만 제거했을 떄 얻을 수 있는 가장 큰 숫자
# numbser 순서를 바꿀 수는 없나봄

# how
# k 보다 같거나 작은 idx에 있는 수들 중 가장 큰 값을 찾아 첫째 자리 수 부터 선택
# 위에서 선택한 idx와 보다 작은 위치에 있는 수들 중 가장 큰 값을 찾아 두째 자리 수 선택
# 반복

# 주의사항
# 시간초과 : O(n^2)

