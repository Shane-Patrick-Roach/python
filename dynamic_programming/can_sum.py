from collections import defaultdict


def can_sum(target_sum, choices, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in choices:
        remainder = target_sum - num
        if can_sum(remainder, choices, memo) == True:
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


print(can_sum(7, [2, 4]))




