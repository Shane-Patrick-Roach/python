from collections import defaultdict

maps = defaultdict(int)


maps["a"] = 1

print(maps["a"])
print(maps["b"])


word = "hello"
key = [0] * 26

for w in word:
    word_val = ord(w) - ord("a")

    key[word_val] += 1

maps[str(key)] = 1



