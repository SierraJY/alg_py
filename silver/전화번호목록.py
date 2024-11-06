# 프로그래머스

from collections import defaultdict, Counter

def solution(phone_book):
    pb_cnt = defaultdict(int)

    for pn in phone_book:
        for l in range(len(pn)-1, 0, -1):
            pb_cnt[pn[:l]]
    for pn in phone_book:
        if pn in pb_cnt : return False

    return True

# what
# 어떤 번호가 다른 번호의 접두어인지 확인
# 접두어인 경우가 있으면 false / 없으면 true

# how
# 특정 전화번호의 뒤에서 부터 줄여보면서 가능한 접두어 해시 테이블 생성
# 원본 전화번호들이 해시테이블에 있는지 확인 후 없으면 해시테이블에 추가

# 알아야할 파이썬
# defaultdict : ddict['key']로 한번이라도 접근해야 key:default value 쌍이 생김