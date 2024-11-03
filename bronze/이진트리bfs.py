from collections import deque
def bfs(tree):
    queue = deque()
    queue.append(1)
    level = 0

    while queue:
        now_level_cnt = len(queue)
        print(f"{level} level : ", end="")

        for _ in range(now_level_cnt):
            v = queue.popleft()
            print(v, end = " ")

            for vc in [v*2, v*2+1]:
                if vc <= 7 : queue.append(tree[vc])

        level += 1
        print()

bfs([1e9,1,2,3,4,5,6,7]) # 인덱스 0은 편의상 사용 X






