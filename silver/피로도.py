from itertools import permutations

def solution(k, dungeons):
    LEN = len(dungeons)
    permutation_list = permutations(dungeons, LEN)

    max_d_cnt = 0
    for p in permutation_list:
        tmp_k = k
        d_cnt = 0
        for d in p:
            if tmp_k >= d[0]:
                tmp_k -= d[1]
                d_cnt += 1

        max_d_cnt = max(max_d_cnt, d_cnt)

    return max_d_cnt

# what
# 탐험할 수 있는 최대 던전 수

# how
# 1
# 필요한 최소 피로도는 큰 순으로 정렬, 소모되는 피로도는 작은 순으로 정렬
# 반례 : [[80,70], ....]

# 2
# 소모되는 피로도(작은 순) 다음 필요한 최소 피로도(큰 순으로)로 정렬
# 반례 : [[80,20],[50,40],[30,10]]

# 3
# BF
# 어차피 던전 최대 개수는 8개 : 8! == 40320

# 4
# DFS