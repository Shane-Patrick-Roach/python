# Allow you to use another function as an argument for another function

def start_end_decorator(func):

    def wrapper(*args):
        # do something before
        print('start')
        func(*args)
        #do something after
        print("end")
    return wrapper

@start_end_decorator
def function_as_argument(str):
    return print(str)

function_as_argument("name")


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"this has been executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("hello")

say_hello()
say_hello()
say_hello()