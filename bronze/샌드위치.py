def solution(nums):

    stack = []
    s_cnt = 0

    for c in nums:
        if c == 1 and len(stack) >=2 and stack[-1] == 2 and stack[-2] == 1:
            s_cnt += 1
            stack.pop()
            stack.pop()
        else:
            stack.append(c)

    return s_cnt

print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
print(solution([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
print(solution([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
print(solution([2, 1, 1, 1, 2, 1, 2]))
print(solution([1, 1, 1, 1, 1, 1, 1]))

# 왜 슬라이딩 윈도우로는 안되는지 생각해보기~