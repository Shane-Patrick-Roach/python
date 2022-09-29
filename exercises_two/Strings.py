# Strings: ordered, immutable, text representation

my_string = "Hello World how are you doing"


my_list = my_string.split(" ")
print(my_list)


new_string = ', '.join(my_list)
print(new_string)


var = 3.12
var2 = 6

my_string2 = f"the variables are {var} and {var2}"
print(my_string2)