def dfs(tree):
    stack = []
    stack.append(1)

    while stack:
        v = stack.pop()
        print(v, end = " ")
        for vc in [v*2+1, v*2]:
            if vc <= 7:
                stack.append(vc)

dfs([1e9,1,2,3,4,5,6,7]) # 인덱스 0은 편의상 사용 X






