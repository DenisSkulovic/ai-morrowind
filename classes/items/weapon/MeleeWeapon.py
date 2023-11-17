from classes.items.Weapon import Weapon


class MeleeWeapon(Weapon):
    def __init__(self, name, base_price, skill, base_damage, durability, enchantment=None):
        super().__init__(name, base_price, skill, base_damage, durability, enchantment)
