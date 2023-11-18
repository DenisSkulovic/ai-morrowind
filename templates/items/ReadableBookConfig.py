from enum.items.ReadableBookEnum import ReadableBookEnum as RBkE
from classes.items.book.ReadableBook import ReadableBook


class ReadableBookConfig:
    """
    This class represents the mapping of readable book items to their details.
    Each readable book is represented by a tuple of four values: item, base_price, content.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "content": 2}
        self._config = {
            RBkE.LUSTY_ARGONIAN_MAID.value: (ReadableBook, 25, "Content of The Lusty Argonian Maid"),
            RBkE.BRIEF_HISTORY_EMPIRE.value: (ReadableBook, 30, "Content of A Brief History of the Empire"),
            RBkE.NGASTA_KVATA_KVAKIS.value: (ReadableBook, 35, "Content of N'Gasta! Kvata! Kvakis!"),
            RBkE.RED_BOOK_RIDDLES.value: (ReadableBook, 20, "Content of The Red Book of Riddles"),
            RBkE.TRUE_NOBLES_CODE.value: (ReadableBook, 40, "Content of The True Noble's Code"),
            RBkE.DOORS_OF_SPIRIT.value: (ReadableBook, 15, "Content of The Doors of the Spirit"),
            RBkE.ANNOTATED_ANUAD.value: (ReadableBook, 50, "Content of The Annotated Anuad"),
            RBkE.DARKEST_DARKNESS.value: (ReadableBook, 45, "Content of Darkest Darkness"),
            RBkE.WILD_ELVES.value: (ReadableBook, 10, "Content of The Wild Elves"),
            RBkE.WOLF_QUEEN_VOL1.value: (ReadableBook, 55, "Content of The Wolf Queen, Vol 1"),
        }

    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given readable book.
        The method takes one parameter: the name of the readable book.
        The item_name parameter should be a string representing the name of the readable book.
        The method returns a dictionary with keys: item, base_price, content.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.book.ReadableBook'>,
            'base_price': 25,
            'content': 'Content of The Lusty Argonian Maid'
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Readable book name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}
