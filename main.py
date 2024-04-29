import sys

sys.stdin = open('input.txt', 'r')

dice = list(map(int, sys.stdin.readline().split()))
dice_set = set(dice)

if len(dice_set) == 1:
    print(10000 + dice[0] * 1000)
elif len(dice_set) == 2:
    for i in range(2):
        if dice.count(tuple(dice_set)[i]) == 2:
            print(1000 + tuple(dice_set)[i] * 100)
            break;
else:
    print(max(dice_set)*100)
