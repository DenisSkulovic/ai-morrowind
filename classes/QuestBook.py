class QuestBook:
    def __init__(self):
        self.active_quest = None
        self.available_quests = []
        self.completed_quests = []
        self.failed_quests = []

    def add_quest(self, quest):
        self.available_quests.append(quest)

    def start_quest(self, quest_name):
        quest = next((q for q in self.available_quests if q.name == quest_name), None)
        if quest:
            self.active_quest = quest
            self.available_quests.remove(quest)

    def complete_quest(self):
        if self.active_quest:
            self.completed_quests.append(self.active_quest)
            self.active_quest = None

    def fail_quest(self):
        if self.active_quest:
            self.failed_quests.append(self.active_quest)
            self.active_quest = None

    def cancel_quest(self, quest_name):
        quest = next((q for q in self.available_quests if q.name == quest_name), None)
        if quest:
            self.available_quests.remove(quest)
        elif self.active_quest and self.active_quest.name == quest_name:
            self.active_quest = None

    # Additional methods as needed for quest management
    
    def __str__(self):
        book_info = ""

        if self.active_quest:
            book_info += "Currently Active Quest:\n"
            book_info += str(self.active_quest) + "\n"

        if self.available_quests:
            book_info += "Available Quests:\n"
            for quest in self.available_quests:
                book_info += f" - {quest.name}\n"

        if self.completed_quests:
            book_info += "Completed Quests:\n"
            for quest in self.completed_quests:
                book_info += f" - {quest.name}\n"

        if self.failed_quests:
            book_info += "Failed Quests:\n"
            for quest in self.failed_quests:
                book_info += f" - {quest.name}\n"

        return book_info if book_info else "No quest information available."

