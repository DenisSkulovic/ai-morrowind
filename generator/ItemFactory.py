class ItemFactory:
    
    def create_item_instance(self, item_config):
        cls = item_config["class"]
        params = item_config["params"]
        instance = cls(**params)
        return instance
