from classes.items.book.Book import Book


class ReadableBook(Book):
    def __init__(self, name, base_price, content):
        super().__init__(name, base_price)
        self.content = content

    def read_book(self):
        super().read_book()
        print(f"Content: {self.content}")

    def __str__(self):
        return super().__str__() + f"\nContent: {self.content[:50]}..."  # Truncate to keep it brief