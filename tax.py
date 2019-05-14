"""
TODO
"""
from product import Product

def get_tax_list():
    tax = {
        'standard': 0.1,
        'tax_exempt': 0,
        'imported':0.2
        }

    return tax

def calc_tax_4_item(product):
    return product.base_price * product.quantity * get_tax_list()[int(product.tax_class)] 


print(get_tax_list())

print(':::',calc_tax_4_item(Product('p1',10,quantity=2)))
