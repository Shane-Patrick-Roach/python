# collections: counter, namedtuple, ordereddict, defaultdict, deque
# Ordered Dictionary that remembers the order.
# Default Dict allows you to declare a type of the dict, and will return default value when no key is present.
# Deque is a double-ended queue which allows you to add and remove elements from either side of the structure.

from collections import Counter, namedtuple, OrderedDict, deque


a = "aaaaabbbbbcccc"

my_counter = Counter(a)

print(my_counter)
print(list(my_counter.elements()))

ordered_dict = OrderedDict()

ordered_dict['b'] = 2
ordered_dict['a'] = 1
ordered_dict['c'] = 3

print(ordered_dict)


d = deque()

d.append('a')
d.append('b')
d.append('c')
d.appendleft('d')
d.pop()

print(d)



