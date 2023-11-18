import random
from classes.Inventory import Inventory
from classes.creatures.character.Character import Character
from generator.ItemFactory import ItemFactory
from config.generation.inventory.InventoryClassMandatoryItems import inventory_class_mandatory_items
from config.generation.inventory.inventory_class_optional_items import inventory_class_optional_items
from config.generation.inventory.inventory_background_items import inventory_background_items

class CharacterInventoryGenerator:
    def __init__(self):
        self.item_factory = ItemFactory()

    def generate_inventory(self, character: Character)->Inventory:
        inventory = Inventory()
        class_type = character.get_class()
        background_type = character.get_background()

        # Create a dictionary to store the combined probabilities of each item
        combined_probabilities = {}

        # Process mandatory, optional and background items separately
        self.process_mandatory_items(inventory, class_type)
        self.process_optional_items(combined_probabilities, class_type)
        self.process_background_items(combined_probabilities, background_type)

        # Iterate over the combined_probabilities dictionary and add items to the inventory
        for item_name, item_info in combined_probabilities.items():
            # Check if the item should be added to the inventory
            if random.random() < item_info["probability"]:
                # Create the item instance
                item_instance = self.item_factory.create_item_instance(item_name)

                # Add the item to the inventory
                inventory.add_item(item_instance, item_info["quantity"])

        return inventory

    def process_mandatory_items(self, inventory, class_type):
        class_mandatory_items = inventory_class_mandatory_items.get(class_type, [])
        # Select an item set based on the probabilities attached to each
        item_set = random.choices(class_mandatory_items, weights=[item["probability"] for item in class_mandatory_items], k=1)[0]
        for item_info in item_set["items"].values():
            for item_name in item_info:
                # If an item set was selected, then each of the items receives a 100% probability
                item_instance = self.item_factory.create_item_instance(item_name)
                inventory.add_item(item_instance, 1)

    def process_optional_items(self, combined_probabilities, class_type):
        class_optional_items = inventory_class_optional_items.get(class_type, [])
        for item in class_optional_items:
            for item_info in item["items"].values():
                for item_name in item_info:
                    self.add_to_combined_probabilities(combined_probabilities, item_name, item["probability"])

    def process_background_items(self, combined_probabilities, background_type):
        background_items = inventory_background_items.get(background_type, [])
        for item in background_items:
            self.add_to_combined_probabilities(combined_probabilities, item["item"], item["probability"], item["quantity"], item.get("std_dev", 0))

    def add_to_combined_probabilities(self, combined_probabilities, item_name, item_probability, item_quantity=1, item_std_dev=0):
        # If the item is already in the combined_probabilities dictionary, calculate the average
        if item_name in combined_probabilities:
            combined_probabilities[item_name]["probability"] = (combined_probabilities[item_name]["probability"] + item_probability) / 2
            combined_probabilities[item_name]["quantity"] = int((combined_probabilities[item_name]["quantity"] + item_quantity) / 2 + random.gauss(0, item_std_dev))
            combined_probabilities[item_name]["std_dev"] = (combined_probabilities[item_name]["std_dev"] + item_std_dev) / 2
        # If the item is not in the combined_probabilities dictionary, add it
        else:
            combined_probabilities[item_name] = {"probability": item_probability, "quantity": int(item_quantity + random.gauss(0, item_std_dev)), "std_dev": item_std_dev}
