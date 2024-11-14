from itertools import product

def solution(word):
    aeiou = ['A', 'E', 'I', 'O', 'U']
    all = []

    for i in range(1, 6):
        all += ["".join(p) for p in product(aeiou, repeat=i)]

    all.sort()

    return all.index(word) + 1

# what
# 모음 사전에서 주어진 다음의 순서

# how
# BF & 문자열 비교(sort)
# 가능한 모든 경우의 수를 담은 리스트에서 주어진 word의 순서를 index메서드로 찾는다
# 단어 길이는 최대 5글자이고 사용 가능한 원소 수도 5개
# 총 경우의 수 : 중복순열5 + 중복순열4 + 중복순열3 + 중복순열2 + 중복순열1
# 5^5 + 5^4 + 5^3 + 5^2 + 5^1 = 3905

# 알게된 파이썬
# 중복조합 : from itertools import product
# 여러 리스트 간의 데카르트 곱을 반환하는 함수임
# 일반적인 중복조합 처럼 사용하려면 매개변수 repeat 반드시 명시해야함