# collections: counter, namedtuple, ordereddict, defaultdict, deque


from collections import Counter, namedtuple


a = "aaaaabbbbbcccc"

my_counter = Counter(a)

print(my_counter)
print(list(my_counter.elements()))


Point = namedtuple('Point')


