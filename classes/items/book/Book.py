from classes.items.Item import Item


class Book(Item):
    def __init__(self, name, base_price, category="Book"):
        super().__init__(name, category, base_price)

    def read_book(self):
        # Basic reading functionality, can be overridden in subclasses
        print(f"Reading {self.name}...")

    def __str__(self):
        return super().__str__()