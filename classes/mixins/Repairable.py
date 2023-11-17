from classes.items.Item import Item


class Repairable(Item):
    def degrade(self, used_durability = 1):
        if self.durability > 0:
            self.durability -= used_durability
            return True
        return False
    
    def repair(self, repair_amount):
        if repair_amount > 0:
            self.durability += repair_amount
        else:
            raise ValueError("Repair amount must be greater than 0")
