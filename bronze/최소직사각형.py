def solution(sizes):
    max_w = 0
    max_h = 0
    for w, h in sizes:
        if max(w, h) == h:
            tmp = w
            w = h
            h = tmp

        max_w = max(max_w, w)
        max_h = max(max_h, h)
    return max_w * max_h

# what
# 모든 명함을 수납할 수 있는 사이즈

# how
# 브루트 포스

# 주의할 것
# 세로로 긴 명함을 눕히는 경우도 있음

# 개선가능
# 긴 변 중에 가장 긴 변과 짧은 변 중 가장 긴 것의 곱셈 결과가 정답이므로,
# def solution(sizes):
#    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
