from collections import Counter

# Reversing a string

word = "hello"
print(word[::-1])

# Joining a list of items

a = ["Geeks", "For", "Geeks"]

print(" ".join(a))

# Counter


def isAnagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(isAnagram("hello", "lloeh"))


