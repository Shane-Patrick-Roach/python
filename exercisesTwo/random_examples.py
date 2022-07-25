import random
import secrets

a = random.random()
print(a)

b = random.uniform(1,10)
print(b)

# inclusive, exclusive
c = random.randint(1,10)
print(c)

d = random.normalvariate(1,5)
print(d)

# picks random character from string
mylist = list("ABCDEFGH")
a = random.choice(mylist)
print(a)

# shuffles the list in random order
random.shuffle(mylist)
print(mylist)

# Allows you to reproduce random values
random.seed(1)
print(random.random())
print(random.randint(1,10))


