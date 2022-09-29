# lambda arguments: expression
# map(func, seq)
# filter(func, seq)
# reduce(func, seq)

add10 = lambda x: x + 10
print(add10(5))

def add10_func(x):
    return x + 10
print(add10_func(5))

multi = lambda x,y: x*y
print(multi(3,4))


points2D = [(1,-2),(3,-4),(5,6),(-7,8)]

points2D = sorted(points2D, key=lambda x: x[0])
print(points2D)

a = [1,2,3,4,5,6]
# list comprehension
b = [x for x in a if x % 2 == 0]
print(b)





