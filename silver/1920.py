import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for target in B:
    left = 0
    right = len(A)-1

    is_there = 0

    while left <= right:

        mid = (left + right)//2

        if A[mid] == target :
            is_there = 1
            break

        elif A[mid] > target :
            right = mid - 1

        elif A[mid] < target :
            left = mid + 1

    print(is_there)

# what
# A[] : N개의 정수
# M개의 정수들이 A[i]들이 있는지 찾아라

# 주의할 것
# 이분탐색 전 반드시 정렬이 되어 있어야 한다.