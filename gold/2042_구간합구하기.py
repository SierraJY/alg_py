import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())

origin_arr = [int(input()) for _ in range(N)]
seg_tree = [0 for _ in range(N*4)]

def make_tree(start, end, node_i):
    # start와 end 매개변수는 세그먼트 트리의 현재 노드(node_i)가 담당하는 원본 배열의 인덱스 범위
    if start == end:
        seg_tree[node_i] = origin_arr[start]
    else:
        mid = (start + end) // 2
        left = make_tree(start, mid, node_i * 2)
        right = make_tree(mid+1, end, node_i * 2 + 1)

        seg_tree[node_i] = left + right

    return seg_tree[node_i]


make_tree(0, N - 1, 1)

def update(start, end, node_i, change_i, new_val):
    if start == end:
        # 종료 조건 start == end일 때, 자동으로 해당 노드는 change_i에 대한 리프노드가 됨
        # 그래서 해당 노드만 수정하고 올라가면서 부모(내부)노드만 갱신해주면 됨
        seg_tree[node_i] = new_val
        return
    else:
        mid = (start + end) // 2

        if start <= change_i <= mid:
            update(start, mid, node_i * 2, change_i, new_val)
        else:
            update(mid+1, end, node_i * 2 + 1, change_i, new_val)

    seg_tree[node_i] = seg_tree[node_i * 2] + seg_tree[node_i * 2 + 1]

def query(start, end, node_i, l, r):
    if r < start or end < l:
        return 0
    elif l <= start and end <= r:
        return seg_tree[node_i]

    mid = (start + end) // 2
    left = query(start, mid, node_i * 2, l, r)
    right = query(mid+1, end, node_i * 2 +1, l, r)

    return left + right

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        update(0, N - 1, 1, b-1, c)
    elif a == 2:
        print(query(0, N-1, 1, b-1, c-1))


