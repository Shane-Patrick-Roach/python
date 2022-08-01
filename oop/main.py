## python passes the object itself as its first argument

class Item:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("hello", 4, 6)

total = item1.calculate_total_price()
print(total)


