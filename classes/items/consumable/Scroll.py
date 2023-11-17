from classes.items.Consumable import Consumable


class Scroll(Consumable):
    def __init__(self, name, base_price, spell_effect):
        super().__init__(name, "Scroll", base_price)
        self.spell_effect = spell_effect

    def use_scroll(self):
        # TODO Implement the effect of using the scroll
        print(f"Using scroll: {self.spell_effect}")
    
    def __str__(self):
        return super().__str__() + f"\nSpell Effect: {self.spell_effect}"

