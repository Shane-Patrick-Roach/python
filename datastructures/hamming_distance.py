import sys

hammingDistance = 0
getbinary = lambda x, n: format(x, 'b').zfill(n)

x_str = str(getbinary(10, 32))
y_str = str(getbinary(1, 32))


print(int(x_str))
# print(bin(int(x_str)) >> 1)

num = int(format(4, 'b'))
num2 = num >> 1
print(num)
print(num2)



# print(y_str)
#
# print(len(format(sys.maxsize, 'b')))
#
# print(11 % 31)





