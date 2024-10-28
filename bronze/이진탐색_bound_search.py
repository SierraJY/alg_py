# 이진 탐색 (반드시 정렬이 되어 있어야 함)
# lower bound search : target보다 크거나 같은 값들 중 가장 작은 값을 찾는 방법
# upper bound search : target보다 큰 값들 중 가장 작은 값을 찾는 방법
def solution(nums, target):

    left = 0
    right = len(nums)

    while left < right: # left <= right면 무한 루프돔
        mid = (left + right) // 2

        if nums[mid] >= target : right = mid     # upper 등호 제거
        elif nums[mid] < target : left = mid + 1 # upper 바운드면 여기에 등호

    return -1 if right == len(nums) else right


print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 4))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], -4))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 11))
print(solution([3, 6, 9, 12, 17, 29, 33], 30))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))




# 주의할 것
# l, m , r은 인덱스고 target은 값이다

# 몰랐던 것
# upper & lower bound의 의미를 잘못알고있었음
# UpperBound : 원하는 값을 초과하는 첫번째 위치를 반환
# LowerBound : 원하는 값 이상의 첫번째 위치를 반환
# 어떤 방식이냐에 따라서 while 문 안의 조건 등호 여부가 달라진다

# 알게된 방법
# right를 len(nums) out of range index를 가리키도록 두고 시작한다
# right를 반환한다
# right는 mid로 옮기고 left는 mid+1로 옮긴다

# 숙지해야할 파이썬 함수
# from bisect import bisect_left, bisect_right
# bisect_left( , ) : lower bound
# bisect_right( , ) : upper bound
