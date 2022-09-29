


def grid_traveler(n, m, map = {}):
    if (n,m) in map:
        return map[n,m]
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1

    map[n,m] = grid_traveler(n - 1, m, map) + grid_traveler(n, m - 1, map)

    return map[n,m]


print(grid_traveler(2,3))
print(grid_traveler(20,20))

