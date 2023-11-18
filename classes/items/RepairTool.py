from classes.items.Tool import Tool


class RepairTool(Tool):
    def __init__(self, name, base_price):
        super().__init__(name, "RepairTool", base_price)
