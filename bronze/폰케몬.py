# 프로그래머스

from collections import Counter

def solution(nums):
    total_pkm_cnt = len(nums)
    pkm_cnt = Counter(nums)
    pkm_kinds = len(pkm_cnt.keys())

    return pkm_kinds if pkm_kinds <= total_pkm_cnt // 2 else total_pkm_cnt // 2

# what
# 포켓몬 N/2 마리 가져가기

# condition
# 최대한 다양하게

# how
# Counter로 종류 개수 파악
# 종류가 N/2 큰지 작은지 파악