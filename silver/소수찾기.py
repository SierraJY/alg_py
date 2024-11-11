from math import sqrt
from itertools import permutations

def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    all = []

    for i in range(1, len(numbers) + 1):
        all += list(permutations(numbers, i))

    all = set([int("".join(a)) for a in all])

    prime_cnt = 0
    for num in all:
        if is_prime(num): prime_cnt += 1

    return prime_cnt

# what
# 만들 수 있는 소수의 개수

# how
# 브루트 포스(완전 탐색)
# 순열로 가능한 모든 문자열의 조합 생성 후 정수화
# set으로 중복 제거


# 알아야할 파이썬
# itertools permutations

# 알게된 것
# 소수 찾기 팁 :https://www.youtube.com/watch?v=LD-Px5YCd8Y

# 주의할 것
#  0,1 소수 제외