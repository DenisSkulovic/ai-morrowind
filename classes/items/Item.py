class Item:
    def __init__(self, name, category, base_price=0, rarity=1, demand=1, special_circumstances=1):
        self.name = name
        self.category = category
        self.base_price = base_price
        self.rarity = rarity
        self.demand = demand
        self.special_circumstances = special_circumstances

    def __str__(self):
        return (f"Item: {self.name}\n"
                f"Category: {self.category}\n"
                f"Base Price: {self.base_price}\n"
                f"Rarity: {self.rarity}\n"
                f"Demand: {self.demand}\n"
                f"Special Circumstances: {self.special_circumstances}")