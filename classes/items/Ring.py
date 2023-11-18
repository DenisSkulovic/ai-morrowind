from classes.items.Item import Item


class Ring(Item):
    def __init__(self, name, base_price):
        super().__init__(name, "Ring", base_price)
