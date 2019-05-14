from product import Product
from tax import *

class Shopping_Cart:

    # def __init__(self,products={}):
    #     self.products = products

    def __init__(self,products=[]):
        self.products = products

    def __str__(self):
        message = ''
        for product in self.products:
            message += product.quantity*"Item: {} base_price: {} tax_rate: {} \n".format(product.name,product.base_price, get_tax_list()[product.tax_class])
        return message

    def add_product(self, *products):
        for product in products:
            self.products.append(product)

    def remove_product(self,*products):
        for product in products:
            self.products.remove(product)

    def calc_before_tax(self):
        total_price = 0
        for product in self.products:
            total_price += product.base_price * product.quantity
        return total_price

    def calc_after_tax(self):
        total_price = 0
        for product in self.products:
            total_price += product.get_total_price()
        return total_price

    def find_expensive_item(self):
        return max(self.products,key = lambda a: a.base_price) 


products = [Product('p1',10,quantity=2), Product('p2',20), Product('p3',20)]


my_sc = Shopping_Cart(products)
after = my_sc.calc_after_tax()
before = my_sc.calc_before_tax()


print('after:',after)
print('before:',before)
print(my_sc)


aa = my_sc.find_expensive_item()
print('::',aa)