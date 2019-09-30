import random as r


class Product():
    # Constructor method with appropriate defaults
    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                 identifier=r.randrange(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    # Method to stealibility
    def stealability(self):
        pw = self.price / self.weight
        if pw < 0.5:
            return "Not so stealable..."
        elif pw > 0.5 and pw < 1.0:
            return "Kinda stealable"
        else:
            return "Very stealable!"

    # Method to determine expodeability
    def explode(self):
        fw = self.flammability * self.weight
        if fw < 10:
            return "...fizzle."
        if fw >= 10 and fw < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):

    def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                 identifier=r.randrange(1000000, 10000000)):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability, identifier=identifier)

    # Override the explode method of Product
    def explode(self):
        return "...it's a glove."

    # Punch method
    def punch(self):
        if self.weight < 5:
            return "Hey that hurt!"
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
