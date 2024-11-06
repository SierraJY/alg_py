from collections import defaultdict


def solution(clothes):
    clothes_kind = defaultdict(int)
    for c, k in clothes:
        clothes_kind[k] += 1

    total_cnt = 1
    for cnt in clothes_kind.values():
        total_cnt *= (cnt + 1)

    return total_cnt - 1

# what
# 서로 다른 옷의 조합의 수 구하기

# how
# Count dict & 경우의수 곱 법칙
# 1. 옷 종류별 개수 집계
# 2. 각 종류별 선택 가능한 경우의 수 계산 (해당 종류 선택 안 함 포함)
# 3. 모든 종류의 경우의 수를 곱하여 전체 조합 수 계산
# 4. 아무것도 입지 않는 경우 1가지를 제외하고 반환