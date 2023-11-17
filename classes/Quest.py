class Quest:
    def __init__(self, name, description, location, objective):
        self.name = name
        self.description = description
        self.location = location
        self.involved_characters = []
        self.required_items = []
        self.progress_updates = []
        self.current_objective = objective

    def add_character(self, character):
        self.involved_characters.append(character)

    def add_required_item(self, item):
        self.required_items.append(item)

    def update_progress(self, update_text):
        if len(update_text) > 0:
            self.progress_updates.append(update_text)

    def update_objective(self, new_objective):
        self.current_objective = new_objective

    # Additional methods as needed
    
    def __str__(self):
        quest_info = f"Quest Name: {self.name}\n"
        quest_info += f"Description: {self.description}\n"
        quest_info += f"Location: {self.location}\n"
        quest_info += f"Current Objective: {self.current_objective}\n"
        quest_info += "Involved Characters: " + ", ".join([char.name for char in self.involved_characters]) + "\n"
        quest_info += "Required Items: " + ", ".join([item.name for item in self.required_items]) + "\n"
        quest_info += "Progress Updates:\n"
        for update in self.progress_updates:
            quest_info += f" - {update}\n"
        return quest_info
