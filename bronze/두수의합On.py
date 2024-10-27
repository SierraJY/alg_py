# 정수 수열 안에서 수열의 원소 두 개의 합이 target값이 되는 경우를 찾고 싶습니다
# 매개변수 nums에 길이가 n인 수열이 주어지고 매개변수 target에 자연수 값이 주어지면,
# 이 수열안에서 두 개의 원소의 합이 정수 target값이 되는 두 원소를 구해 배열에 오름차순으로 담아 반환합니다.
# 두 개의 원소의 합이 target 값이 되는 경우는 오직 한가지 뿐인 입력만 주어집니다.
# 한 원소를 두 번 더하는 것은 안됩니다 nums의 각 원소는 유일값입니다.
# 답이 없을 경우 [0, 0] 을 반환합니다

from collections import defaultdict

def solution(nums, target):

    nums_cnt = defaultdict(int)

    for n1 in nums:
        n2 = target - n1

        if n2 in nums_cnt:
            return sorted([n1,n2])
        else:
            nums_cnt[n1] += 1

    return [0,0]

# defaultdict 인자로 nums 넘길 수 없음, 이터러블을 인자로 사용할 수 없음
# 해시테이블 접근 시간 O(1)

print(solution([3, 7, 2, 12, 9, 15, 8], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))

