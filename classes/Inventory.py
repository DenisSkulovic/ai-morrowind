from classes.items.consumable.Consumable import Consumable


class Inventory:
    def __init__(self):
        self.items = {}  # Stores Item objects

    def add_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name].quantity += quantity
        else:
            item.quantity = quantity
            self.items[item.name] = item

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name].quantity >= quantity:
            self.items[item_name].quantity -= quantity
            if self.items[item_name].quantity == 0:
                del self.items[item_name]
            return True
        return False  # Not enough quantity or item does not exist

    def merge_two_consumables(self, consumable_1, consumable_2):
        is_consumable_1_consumable = isinstance(Consumable)
        is_consumable_2_consumable = isinstance(Consumable)
        is_same_name = self.name == consumable_2.name
        is_same_quality = self.quality == consumable_2.quality
        if is_consumable_1_consumable == False:
            raise TypeError("when merging two items, item 1 must be a consumable")
        if is_consumable_2_consumable == False:
            raise TypeError("when merging two items, item 2 must be a consumable")
        if is_same_quality == False:
            raise TypeError("cannot merge two consumables of different quality")
        if is_same_name == False:
            raise TypeError("cannot merge two consumables of different name")
        consumable_1.quantity += consumable_2.quantity
        consumable_2.quantity = 0
        return consumable_1
    
    def merge_consumables(self):
        # TODO
        items_by_type = self._group_items_by_type()
        pass
    
    def _group_items_by_type(self):
        grouped = {}
        for item in self.items.values():
            if item.category not in grouped:
                grouped[item.category] = []
            grouped[item.category].append(item)
        return grouped

            
    def __str__(self):
        if not self.items:
            return "Inventory is empty."

        inventory_str = "Inventory Contents:\n"
        grouped_items = self._group_items_by_type()

        for item_type, items in grouped_items.items():
            inventory_str += f"\n{item_type}:\n"
            for item in items:
                inventory_str += f" - {item.name} (Value: {item.base_price}, Quantity: {item.quantity})\n"

        return inventory_str
