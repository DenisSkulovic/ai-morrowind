from classes.items.Item import Item


class Tool(Item):
    def __init__(self, name, base_price):
        super().__init__(name, "Tool", base_price)
