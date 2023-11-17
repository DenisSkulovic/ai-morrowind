from classes.items.book.Book import Book


class SkillBook(Book):
    def __init__(self, name, base_price, skill, skill_improvement):
        super().__init__(name, base_price)
        self.skill = skill
        self.skill_improvement = skill_improvement
        self.used = False

    def read_book(self):
        if not self.used:
            super().read_book()
            self.used = True
            return self.skill_improvement
        else:
            print("You have already learned everything this book has to offer.")
            return None

    def __str__(self):
        used_status = "Used" if self.used else "New"
        return super().__str__() + f"\nSkill Improvement: {self.skill_improvement}\nStatus: {used_status}"
