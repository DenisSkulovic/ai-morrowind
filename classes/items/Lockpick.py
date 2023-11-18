from classes.items.Tool import Tool


class Lockpick(Tool):
    def __init__(self, name, base_price):
        super().__init__(name, "Lockpick", base_price)
