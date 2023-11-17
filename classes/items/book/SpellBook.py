from classes.items.book.Book import Book


class SpellBook(Book):
    def __init__(self, name, base_price, spell_name):
        super().__init__(name, base_price)
        self.spell_name = spell_name
        self.used = False

    def read_book(self):
        if not self.used:
            super().read_book()
            print(f"You have learned the spell: {self.spell_name}")
            self.used = True
            return self.spell_name
        else:
            print("You have already learned the spell from this book.")
            return None
    def __str__(self):
        used_status = "Used" if self.used else "New"
        return super().__str__() + f"\nSpell Name: {self.spell_name}\nStatus: {used_status}"