# Errors and Exceptions

x = -10
# if x < 0:
#     raise Exception('x should be positive')
#
#
# assert (x >= 0), 'x is not positive'

try:
    a = 5 / 1
    b = a + 0
# handle multiple exceptions
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up...')


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)

try:
    test_value(-200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)





