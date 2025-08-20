class Item:
    items_list = []
    craftable_items = []
    # Constructor method
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.buy_price = None
        self.sell_price = None
        Item.items_list.append(self)
        self.crafting = {}

    # Method to set the crafting recipe of an item
    def set_crafting(self, recipe):
        self.crafting = recipe
        Item.craftable_items.append(self.name)

    # Method to get the crafting recipe of an item
    def get_crafting(self):
        return self.crafting

    # Method to get the name of the item
    def get_name(self):
        return self.name
    
    # Method to set the description of the item
    def set_description(self, description):
        self.description = description

    # Method to get the description of the item
    def get_description(self):
        return self.description
    
    # Method to set the buy cost of the item
    def set_buy_price(self, cost):
        self.buy_price = cost

    # Method to get the buy cost of the item
    def get_buy_price(self):
        return self.buy_price
    
    # Method to set the sell cost of the item
    def set_sell_price(self, cost):
        self.sell_price = cost

    # Method to get the sell cost of the item
    def get_sell_price(self):
        return self.sell_price
    
class Crafting_Items(Item):
    # Constructor method
    def __init__(self, item_name):
        super().__init__(item_name)

class Weapons(Item):
    # Constructor method
    def __init__(self, item_name, dp, durability):
        super().__init__(item_name)
        self.damage_points = dp
        self.max_durability = durability
        self.durability = durability

    # Method to get damage points
    def get_damage(self):
        return self.damage_points
    
    # Method to set durability
    def set_durability(self, durability):
        self.durability = durability

    # Method to lower item durability by 1
    def use_weapon(self):
        self.durability -= 1

    # Method to get the durability of the weapon
    def get_durability(self):
        return self.durability

class Armour(Item):
    # Constructor method
    def __init__(self, item_name, dp, durability):
        super().__init__(item_name)
        self.defence_points = dp
        self.max_durability = durability
        self.durability = durability

    # Method to get defence points
    def get_defence(self):
        return self.defence_points
    
    # Method to set durability
    def set_durability(self, durability):
        self.durability = durability

    # Method to lower item durability by 1
    def use_armour(self):
        self.durability -= 1

    # Method to get the durability of the weapon
    def get_durability(self):
        return self.durability
    
class Powerups(Item):
    # Constructor method
    def __init__(self, item_name):
        super().__init__(item_name)
