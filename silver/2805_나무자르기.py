import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(trees)

while left <= right:
    h = (left + right) // 2

    cutted_trees = map(lambda x : x-h, trees)
    cutted_trees = [t for t in cutted_trees if t > 0]

    if sum(cutted_trees) >= M:
        left = h + 1
    else:
        right = h - 1

print(right)


# what
# 적어도 M미터이 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값

# how
# bisect

# 주의할 것
# 나의 원래 코드 : 높이를 최댓값 부터 1씩 감소시키며 순차탐색하고
# bisect_right로 각 높이보다 큰 나무들의 위치를 찾음(이 방법은 하수)
# 개선된 코드 : 높이 범위에 대한 이진 탐색 수행
# 가능한 높이를 절반씩 좁혀가며 탐색
# 따라서 정렬도 불필요하고 시간복잡도 크게 차이남

# 알게된 것
# 범위에 대한 이분 탐색
# 이분 탐색하는 범위가 문제에서 준 나무 리스트가 아님!!!
# '플레티넘 : 입국심사'랑 비슷한 느낌

# right를 반환하는 이유에 대하여