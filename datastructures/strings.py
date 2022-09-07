
s = "hello"

repeats = {}

longestSub = 1
l_idx = 0

for i in range(len(s)):

    if s[i] in repeats:

        move_idx = repeats[s[i]] + 1

        while l_idx < move_idx:
            del repeats[s[l_idx]]
            l_idx += 1

        repeats[s[i]] = i

    else:
        repeats[s[i]] = i

    longestSub = max(longestSub, i - l_idx + 1)

print(longestSub)