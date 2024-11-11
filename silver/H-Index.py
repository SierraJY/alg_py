from bisect import bisect_left

def solution(citations):
    LEN = len(citations)
    citations.sort()
    max_h = 0

    for h in range(10001):
        ge_idx = bisect_left(citations, h)
        ge_cnt = LEN - ge_idx
        if ge_cnt >= h and max(max_h, h) == h:
            max_h = h

    return max_h

# what
# H-Index : 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
# 나머지 논문이 h번 이하 인용되었을 때 h의 최댓값

# how
# 정렬하고 순차적으로 탐색하며 max 갱신
# 어차피 인용 횟수 범위 0~10000만까지
# 0~10000까지 반복하며 h번 이상된 논문이 h편 이상인지 확인하고 max_h갱신
# 이분탐색으로 h번 이상된 논문이 몇 편인지 확인

# 주의할 것
# 반례 : [10, 11, 12, 13, 14, 15]일 때 H-Index는 6임
# H-Index와 논문 인용 횟수 배열의 원소와는 관련 없음 -> 전탐색 해야함(?)