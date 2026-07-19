class Product:
    storename = "Smart Mart"
    def __init__(self,productname,price,quantity):
        self.productname = productname
        self.price = price
        self.quantity = quantity
    def totalprice(self):
        total = self.price*self.quantity
        return total

    def displayproduct(self):
        print("Storename:",Product.storename)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
        print("Total Price:",self.totalprice())

pr = Product("Apple",120,2)
pr.displayproduct()