from classes.items.Item import Item


class Consumable(Item):
    def __init__(self, name, base_price, quantity):
        super().__init__(name, "Consumable", base_price)
        self.quantity = quantity

    def consume(self, amount=1):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False
    
    def __str__(self):
        return super().__str__() + f"\nQuantity: {self.quantity}"
