from classes.items.Consumable import Consumable


class Potion(Consumable):
    def __init__(self, name, base_price, quantity, effect):
        super().__init__(name, "Potion", base_price, quantity)
        self.effect = effect

    def use_potion(self):
        if self.quantity > 0:
            self.quantity -= 1
            return self.effect
        return None
    
    def __str__(self):
        return super().__str__() + f"\nEffect: {self.effect}"
