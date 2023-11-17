class Journal:
    def __init__(self):
        self.entries = []  # List to store journal entries

    def add_entry(self, entry):
        """ Add a new entry to the journal. """
        self.entries.append(entry)

    def __str__(self):
        """ Return a string representation of the journal's contents. """
        if not self.entries:
            return "Journal is empty."

        journal_str = "Journal Contents:\n"
        for index, entry in enumerate(self.entries, 1):
            journal_str += f"Entry {index}:\n{entry}\n"

        return journal_str

