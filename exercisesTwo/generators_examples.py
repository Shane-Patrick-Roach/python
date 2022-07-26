# powerful python tool, very memory efficent

def mygenerator():
    yield 1
    yield 2
    yield 3


g = mygenerator()
print(g)

for i in g:
    print(i)


def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -= 1

mygenerator_two = (i for i in range(10) if i % 2 == 0 )
for i in mygenerator_two:
    print(i)