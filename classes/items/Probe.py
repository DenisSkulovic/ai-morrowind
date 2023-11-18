from classes.items.Tool import Tool


class Probe(Tool):
    def __init__(self, name, base_price):
        super().__init__(name, "Probe", base_price)
