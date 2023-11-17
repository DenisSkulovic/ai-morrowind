from classes.items.Consumable import Consumable


class Arrow(Consumable):
    def __init__(self, name, base_price, base_damage, quantity):
        super().__init__(name, base_price, quantity)
        self.base_damage = base_damage
        
    def __str__(self):
        return super().__str__() + f"\nArrow Quality: {self.quantity}"
