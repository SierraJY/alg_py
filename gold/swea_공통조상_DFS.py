import sys

sys.stdin = open('input.txt', 'r')
input =sys.stdin.readline

T = int(input())

def find_same_ans(v1, v2):
    if v1_anses.intersection(v2_anses) :
        return list(v1_anses.intersection(v2_anses))[0]

    if up_graph[v1] :
        v1_anses.add(up_graph[v1][0])
        v1 = up_graph[v1][0]

    if up_graph[v2] :
        v2_anses.add(up_graph[v2][0])
        v2 = up_graph[v2][0]

    return find_same_ans(v1,v2)

def dfs_cnt_childs(v1):
    cnt = 1
    for v2 in down_graph[v1]:
        cnt += dfs_cnt_childs(v2)

    return cnt



for t in range(T):
    V, E, a, b = map(int, input().split())
    edges = list(map(int, input().split()))

    up_graph = [[] for _ in range(V+1)] #그래프 1부터
    down_graph = [[] for _ in range(V + 1)]  # 그래프 1부터
    for i in range(0,len(edges)-1, 2):
        parent = edges[i]
        child = edges[i+1]

        up_graph[child].append(parent)
        down_graph[parent].append(child)

    v1_anses = set()
    v2_anses = set()
    same_ans = find_same_ans(a,b)
    print(f"#{t+1} {same_ans} {dfs_cnt_childs(same_ans)}")


# 문제 및 아이디어
# <임의 두 노드의 가까운 공통 조상은 어떻게 찾을 것 인가>
# => dfs
# 각각의 노드에 대해 조상 집합(set)을 만들어고, 조상을 추가하면서 올라감
# 교집합이 생기면 재귀 종료하고Return

# <공통 조상을 루트로 하는 트리 크기>
# => dfs

# <⭐️트리는 어떻게 구현할 것인가>
# 인접리스트 그래프 형태
# 다만 이렇게 저장하면 상하관계가 뭉개지기 때문에
# 루트노드로 올라가는 그래프 & 내려가는 그래프 형태를 따로 저장함


# 백트래킹 방식으로 풀면??