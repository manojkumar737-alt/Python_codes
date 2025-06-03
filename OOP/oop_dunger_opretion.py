class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, order):
        return self.price > order.price
    
odr1 = order("apple", 30)
odr2 = order("banana", 20)

print(odr1 > odr2)  # Output: False