def powerset(depth, included):
    if depth == len(included):
        cur_subset = [l[i] for i in range(len(included)) if included[i]]
        subsets.append(cur_subset)
        return

    included[depth] = False
    powerset(depth+1, included)

    included[depth] = True
    powerset(depth + 1, included)

subsets = []
l = ['A', 'B', 'C', 'D']
initial_included = [False] * len(l)
powerset(0, initial_included)
print(subsets)
print(len(subsets))

# 종료 조건만 적어놓고,
# 실제 종료(return) 까먹음