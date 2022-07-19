# Dictionary: Key-value pairs, Unordered, Mutable

myDict = {"name": "Max", "color": "blue"}

print(myDict["name"])


try:
    print(myDict["last"])
except:
    print("not in dict")

for key in myDict.keys():
    print(key)

myNumDict = { 1: "hello", 3: "four"}

for key in myNumDict.keys():
    print(key)


