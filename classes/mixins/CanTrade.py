from classes.creatures.Creature import Creature


class CanTrade(Creature):
    def set_trading_inventory(self, trading_inventory):
        self.trading_inventory = trading_inventory
        
    def get_trading_inventory(self):
        return self.trading_inventory
    