## python functions have to be indented

def say_hi(name, age):
    print(name + " " + age)

say_hi("Mike", "12")


def cube(num):
    result = pow(num, 10)
    if (result > 100):
        return result
    else:
        return "nope"


print(cube(10))
