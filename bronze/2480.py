import sys

sys.stdin = open(0, 'r')

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


# Set 자료형의 유용함
# Set은 순서가 없기 때문에, Non-Subscribtalbe이고, 인덱스가 없다