from classes.items.Item import Item
from classes.mixins.Repairable import Repairable
from classes.mixins.Tradable import Tradable


class Armor(Tradable, Repairable, Item):
    def __init__(self, name, base_price, skill, base_defence, durability, enchantment=None):
        super().__init__(name, "Weapon", base_price)
        self.durability = durability
        self.skill = skill
        self.base_defence = base_defence
        self.enchantment = enchantment

    def __str__(self):
        return (super().__str__() + "\n"
                f"Durability: {self.durability}\n"
                f"Enchantment: {self.enchantment if self.enchantment else 'None'}")
