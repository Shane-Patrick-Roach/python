from itertools import permutations, accumulate


a = [1, 2, 3]

perm = permutations(a)

print(list(perm))

acc = accumulate(a)

print(list(acc))

