class Art:

    def __init__(self, name, artist, price):
        self.name = name
        self.artist = artist
        self.price = price

    
    def __str__(self):
        return f"Art: {self.name} by {self.artist}, worth: {self.price:.2f}"


class Gallery:

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.artwork = []

    def add(self, *arts):
        for art in arts:
            self.artwork.append(art)
    
    def __str__(self):
        message = f'{self.name} in {self.city} has Collection contains: \n'
        if self.artwork == []:
            message = f'{self.name} in {self.city} has Nothing to show!'
            return message
        else:
            for art in self.artwork:
                message += art.__str__() + '\n'
        
        return message

    def print_inventory(self):
        print(self)




aa = Gallery('AGO', 'Toronto')
aa.add(Art('name1','arty 1',100), Art('name2', 'arty2', 120))
aa.print_inventory()