class goods (object):
    def __init__(self,name,total):
        self.name = name
        self.product = 10
        self.total = total
    def add_product(self,amount):
        self.product += amount
        print(self.product)


cake = goods("cake",10)
print(cake.product)

cake.add_product(10)
