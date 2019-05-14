from tax import get_tax_list

class Product:

    def __init__(self,name, base_price, tax_class='standard', quantity=1):
        self.name = name
        self.base_price = base_price
        self.tax_class = tax_class
        self.quantity = quantity
    

    def __str__(self):
        return "I am a product of: {} I do worth more than: {}, P.S: tax rate is: {}".format(self.name, self.base_price, self.tax_class)

    def get_total_price(self):
        print('self.tax_class', int(self.tax_class))
        # return (self.base_price + (get_tax_list()[int(self.tax_class)] * self.base_price)) * self.quantity
    
