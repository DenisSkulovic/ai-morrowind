class Location:
    def __init__(self, name, description, type, size_and_density):
        self.name = name
        self.description = description
        self.type = type
        self.size_and_density = size_and_density
        self.npcs = {}  # Dictionary to hold Character instances

    def add_npc(self, npc):
        """ Add an NPC (Character instance) to the location. """
        self.npcs[npc.name] = npc

    def remove_npc(self, npc_name):
        """ Remove an NPC from the location by name. """
        if npc_name in self.npcs:
            del self.npcs[npc_name]

    def find_relevant_routes(self):
        """
        Find all routes relevant to the given location.

        :return: Dictionary of relevant routes for the given location.
        """
        relevant_routes = {}
        for route, details in vvardenfell_connections.items():
            if self.name in route.split(" <-> "):
                relevant_routes[route] = details
        return relevant_routes
    
    def __str__(self):
        """ Display information about the location. """
        print(f"Location: {self.name}")
        print(f"Description: {self.description}")
        print(f"Type: {self.type}")
        print(f"Size and Density: {self.size_and_density}")
        print("NPCs present:")
        for npc in self.npcs.values():
            print(f" - {npc.name}")