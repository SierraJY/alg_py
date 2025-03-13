import sys

sys.stdin = open(0, 'r')
input = sys.stdin.readline

def dfs(now_i, now_cnt, now_alp):
    global max_possible

    if now_cnt == remain_K:
        possible_cnt = 0 # 비트마스킹 연산으로 가능한지 판단
        for w_bit in words:
            if w_bit & ~now_alp == 0:
                possible_cnt += 1
        max_possible = max(max_possible, possible_cnt)
        return

    if now_i == 26: #알파벳 개수 26
        return

    # 현재 알파벳이 기본 알파벳인 경우 건너뛰기
    if (1 << now_i) & alp:
        dfs(now_i + 1, now_cnt, now_alp)
        return

    # 현재 알파벳 선택
    dfs(now_i + 1, now_cnt + 1, now_alp | (1 << now_i))
    # 현재 알파벳 선택하지 않음
    dfs(now_i + 1, now_cnt, now_alp)


N, K = map(int, input().split())

# antic 비트 추가해둠
alp = 0
for c in ['a', 'n', 't', 'i', 'c']:
    alp |= (1 << (ord(c) - ord('a')))

# 각 단어에 필요한 antic제외 알파벳 비트마스크
words = []
for _ in range(N):
    w = input().strip()
    w_bit = 0
    for c in w:
        w_bit |= (1 << (ord(c) - ord('a')))
    # 기본 알파벳 외에 필요한 알파벳만 저장
    words.append(w_bit & ~alp)

if K < 5:  # K가 5보다 작으면 어떤 단어도 읽을 수 없음
    max_possible = 0
elif K >= 26:
    max_possible = N
else:
    remain_K = K - 5
    max_possible = 0
    dfs(0, 0, alp)

print(max_possible)


# 문제 이해
# - k개의 글자만 가르쳐서 읽을 수 있는 단어개수

# 아이디어 & 알고리즘
# anta 와 tica는 반드시 읽을 수 있어야함
# => a, n, t, i, c  :5개

# 읽을 수 있는 단어의 최대 개수는 어떻게?
# => 단순히 공통적으로 많이 나오는 것부터 -> 불가
# => a, n, t, i, c 제외 짧은 단어 부터 처리 -> 불가

# => 완전탐색(DFS)
# 데이터가 그렇게 많아 보이지 않음
# 백트래킹 : 그 단어를 말할 수 있을 때와 없을 때

# => 일반 DFS는 시간초과

# 힌트
# 비트마스킹