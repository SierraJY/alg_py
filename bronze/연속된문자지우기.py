# 연속된 문자 지우기

def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c : stack.pop()
        else : stack.append(c)

    return "".join(stack)

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))

# 알아야할 것
# 쌍, 짝 같은 문제는 스택

# 알아야할 파이썬
# list(stack), queue(deque) 타입이 비어있으면 False로 간주된다