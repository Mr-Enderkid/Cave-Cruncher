# Creating a dictionary containing the opposite direction to each of the 8 possible directions
opposite_directions = {
    "north": "south",
    "east": "west",
    "south": "north",
    "west": "east",
    "north-east": "south-west",
    "north-west": "south-east",
    "south-east": "north-west",
    "south-west": "north-east"
}

class Cave:
    # Creating a list to store the names of instances in this class for future use
    cave_list = []
    ordered_dictionary = {}

    # Constructor method
    def __init__(self, cave_name, cave_id):
        Cave.cave_list.append(self)
        self.name = cave_name
        self.cave_id = cave_id
        self.description = None
        self.character = None
        self.chestStatus = "no"
        self.linked_caves = {}
        self.dug = False

    # Method to get the name of a cave
    def get_name(self):
        return self.name
    
    # Method to get the id of a cave
    def get_id(self):
        return self.cave_id
    
    # Method to set the description of a cave
    def set_description(self, description):
        self.description = description

    # Method to get the description of a cave
    def get_description(self):
        return self.description
    
    # Method to set the character currently in the cave
    def set_character(self, character):
        self.character = character
    
    # Method to get the character currently in the cave
    def get_character(self):
        return self.character
    
    # Method to place/remove a money chest in the cave
    def set_chestStat(self, status):
        self.chestStatus = status
    
    # Method to get chestStatus of a cave
    def get_chestStat(self):
        return self.chestStatus
    
    # Method to set the cave to dug
    def set_dug(self):
        self.dug = True
    
    # Method to link caves
    def link_cave(self, direction, id):
        # Linking linked cave to current cave
        self.linked_caves[direction] = id
        # Finding the direction of the current cave from the linked cave
        opp_direction = opposite_directions[direction]
        # Finding the instance name of the linked cave
        for cave in Cave.cave_list:
            if cave.cave_id == id:
                # Linking the current cave to the linked cave
                cave.linked_caves[opp_direction] = self.cave_id

    # Method to print a list of linked caves
    def move_menu(self):
        Cave.ordered_dictionary = {}
        print("List of surrounding caves:\n")
        # Swapping key and value of linked_caves dictionary for ordering
        swapped_dictionary = dict((id, direction) for direction, id in self.linked_caves.items())
        # Ordering dictionary in ascending order of cave_id
        for i in range(0, 20):
            if i in swapped_dictionary:
                Cave.ordered_dictionary[swapped_dictionary[i]] = i
        # Looping through all the caves linked to the current cave from ordered dictionary
        for direction in Cave.ordered_dictionary:
            # Finding the id of the linked cave for each direction
            surr_caveID = Cave.ordered_dictionary[direction]
            # Finding the instance name of the linked cave using the linked id
            for cave in Cave.cave_list:
                if cave.cave_id == surr_caveID:
                    surr_caveName = cave.name
                    # Printing a message with the id, name and direction
                    print(str(surr_caveID) + ".", surr_caveName, "(" + direction + ")")
    
    # Method to return the name of the cave the player wants to move to
    def move(self, menu_num):
        for direction in Cave.ordered_dictionary:
            if Cave.ordered_dictionary[direction] == menu_num:
                caveid = self.linked_caves[direction]
                for cave in Cave.cave_list:
                    if cave.cave_id == caveid:
                        return cave

class Mine(Cave):
    # Constructor method
    def __init__(self, cave_name, cave_id):
        super().__init__(cave_name, cave_id)
        self.reset_search = 0

class Nature(Cave):
    # Constructor method
    def __init__(self, cave_name, cave_id):
        super().__init__(cave_name, cave_id)

class Spider(Cave):
    # Constructor method
    def __init__(self, cave_name, cave_id):
        super().__init__(cave_name, cave_id)

class Shop(Cave):
    # Constructor method
    def __init__(self, cave_name, cave_id):
        super().__init__(cave_name, cave_id)

class Ancient(Cave):
    # Constructor method
    def __init__(self, cave_name, cave_id):
        super().__init__(cave_name, cave_id)

class Outside(Cave):
    # Constructor method
    def __init__(self, cave_name, cave_id):
        super().__init__(cave_name, cave_id)

class Beach(Cave):
    # Constructor method
    def __init__(self, cave_name, cave_id):
        super().__init__(cave_name, cave_id)

class Battle(Cave):
    # Constructor method
    def __init__(self, cave_name, cave_id):
        super().__init__(cave_name, cave_id)
