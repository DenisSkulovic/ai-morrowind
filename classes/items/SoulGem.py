from classes.items.Item import Item


# for simplicity the soul gem will be True/False for full/empty
class SoulGem(Item):
    def __init__(self, name, base_price, soul_capacity, is_filled = False):
        super().__init__(name, "SoulGem", base_price)
        self.soul_capacity = soul_capacity
        self.is_filled = is_filled

    def fill_soul_gem(self, soul_size):
        if soul_size <= self.soul_capacity and not self.is_filled:
            self.is_filled = True
            return True
        return False

    def __str__(self):
        filled_status = "Filled" if self.is_filled else "Empty"
        return super().__str__() + f"\nSoul Capacity: {self.soul_capacity}\nFilled: {filled_status}"
