# note : 세그먼트 트리 -> 합 대신 최소 저장

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
seg_tree = [0 for i in range(4*len(arr))]
M = int(input())

def make_tree(start, end, node_i):
    if start == end:
        seg_tree[node_i] = start

        return seg_tree[node_i]

    else:
        mid = (start +end)//2
        left = make_tree(start, mid, 2 * node_i)
        right = make_tree(mid+1, end, 2 * node_i + 1)

        if arr[left] <= arr[right]:
            seg_tree[node_i] = left
        else:
            seg_tree[node_i] = right

        return seg_tree[node_i]

def update_tree(start, end, node_i, change_i):
    if start == end:
        return seg_tree[node_i]
    else:
        mid = (start + end) // 2
        if start <= change_i <= mid:
            update_tree(start, mid, node_i * 2, change_i)
        elif mid+1 <= change_i <= end:
            update_tree(mid+1, end, node_i * 2 + 1, change_i)

        if arr[seg_tree[node_i*2]] <=  arr[seg_tree[node_i*2+1]]:
            seg_tree[node_i] = seg_tree[node_i*2]
        else:
            seg_tree[node_i] = seg_tree[node_i*2+1]

        return seg_tree[node_i]


def query_min(start, end, left, right, node_i):
    if right < start or end < left:
        return -1  # 범위 밖인 경우

    if left <= start and end <= right:
        return seg_tree[node_i]

    mid = (start + end) // 2
    left_min = query_min(start, mid, left, right, 2 * node_i)
    right_min = query_min(mid + 1, end, left, right, 2 * node_i + 1)

    if left_min == -1:
        return right_min
    if right_min == -1:
        return left_min

    if arr[left_min] <= arr[right_min]:
        return left_min
    else:
        return right_min

make_tree(0, len(arr)-1, 1)

for _ in range(M):
    ord, a, b = map(int, input().split())

    if ord == 1:
        arr[a-1] = b
        update_tree(0, len(arr)-1, 1, a-1)

    elif ord == 2:
        print(query_min(0, len(arr)-1, a-1, b-1, 1)+1)