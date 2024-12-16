import sys

sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
liquids = list(map(int, sys.stdin.readline().split()))

left, min_left = 0, 0
right, min_right = N-1, N-1

min_fusion = 1e10

while left < right:
    fusion = liquids[left] + liquids[right]

    if abs(fusion) < min_fusion :
        min_fusion = abs(fusion)
        min_left = left
        min_right = right

    if fusion < 0 :
        left += 1

    elif fusion >= 0 :
        right -= 1

print(liquids[min_left], liquids[min_right])

# what
# 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성 값
# 같은 경우 아무거나

# how
# two pointer(bisect 개념이 조금 섞인)