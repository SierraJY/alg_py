from collections import deque, Counter

def solution(begin, target, words):
    def not_same_c_cnt(w1, w2):
        cnt = 0
        for c1, c2 in zip(w1, w2):
            if c1 != c2: cnt += 1

        return cnt

    C_LEN = len(begin)
    visited = Counter(words)
    queue = deque()
    queue.append(begin)
    now_level = 0

    while queue:
        now_queue_cnt = len(queue)
        now_level += 1

        for _ in range(now_queue_cnt):
            poped = queue.popleft()

            for w in words:
                if visited[w] == 0: continue
                if not_same_c_cnt(poped, w) == (1):
                    if w == target: return now_level
                    visited[w] = 0
                    queue.append(w)

    return 0

# what
# 가장 짧은 변환 과정의 단계 수

# how
# '최단'문제 -> BFS 고려
# visited에 Counter 사용, 한번 방문(=사용) 했으면 value를 0으로

# 주의할 것
# 해당 문제에서 단어 비교 시에, 잘못된 방식들
# 같은 문자 개수 set union 안됨, 문자 중복 제거 있으니까
# 또한, 아래와 같이 비교하면 안됨
# def count_same(w1, w2):
#         cnt = 0

#         for w in w1:
#             if w in w2 : cnt += 1

#         return cnt
# 반례
# "aaa", "aab" -> 3