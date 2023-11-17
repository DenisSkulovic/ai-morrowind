from classes.Inventory import Inventory
from classes.creatures.Creature import Creature


class HasInventory(Creature):
    def __init__(self):
        super().__init__()
        
    def set_inventory(self, inventory: Inventory) -> None:
        self.inventory = inventory
    def get_inventory(self) -> Inventory:
        return self.inventory
    