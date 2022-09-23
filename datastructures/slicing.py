from collections import Counter

word = "hello"

print(word[::-1])


cnt = Counter()


tally = ["hello","hello","hello","hello","hello"]

for i in tally:
    cnt[i] += 1


print(cnt["hello"])



