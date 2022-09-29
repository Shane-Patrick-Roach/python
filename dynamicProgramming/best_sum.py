def best_sum(target, choices, memo={}):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_comb = None

    for num in choices:
        remainder = target - num
        possible_sum = best_sum(remainder, choices, memo)
        if possible_sum is not None:
            new_sum = possible_sum.copy() + [num]
            if shortest_comb is None or len(new_sum) < len(shortest_comb):
                shortest_comb = new_sum

    memo[target] = shortest_comb

    return memo[target]


print(best_sum(500, [1, 2])) # 250

