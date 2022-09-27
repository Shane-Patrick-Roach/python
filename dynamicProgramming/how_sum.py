def how_sum(target_sum, choices, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in choices:
        remainder = target_sum - num
        get_remainder = how_sum(remainder, choices, memo)
        if get_remainder is not None:
            get_remainder.append(num)
            memo[target_sum] = get_remainder
            return memo[target_sum]

    memo[target_sum] = None
    return None


print(how_sum(49,[7]))
