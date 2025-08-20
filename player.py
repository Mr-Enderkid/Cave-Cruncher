from items import *
from item_setup import *

crafting_items = ["Rusty Iron", "Shiny Iron", "Stick", "String"]
weapons = ["Rusty Shovel", "Shiny Shovel", "Rusty Sword", "Shiny Sword", "Rusty Arrow", "Shiny Arrow", "Bow"]
armour = ["Rusty Helmet", "Rusty Chestplate", "Rusty Leggings", "Rusty Boots", "Shiny Helmet", "Shiny Chestplate", "Shiny Leggings", "Shiny Boots"]
powerups = ["Attack Shroom", "Defence Shroom", "Speed Shroom", "Heal Shroom"]
misc_items = ["Vegemite", "Atomic Bomb"]

class Player:
    # Constructor method
    def __init__(self, hp, coins):
        self.health = hp
        self.coins = coins
        self.crafting_items = {}
        self.weapons = {}
        self.armour = {}
        self.powerups = {}
        self.misc_items = {}
        self.current_cave = None
    
    # Method to set current cave
    def set_cave(self, cave):
        self.current_cave = cave

    # Method to get current cave
    def get_cave(self):
        return self.current_cave
    
    # Method to set health 
    def set_health(self, health):
        self.health = health

    # Method to get health
    def get_health(self):
        return self.health
    
    # Method to set coins
    def set_coins(self, coins):
        self.coins = coins

    # Method to get the user's coin balance
    def get_coins(self):
        return self.coins
    
    # Method to add coins to the user's balance
    def add_coins(self, morecoins):
        self.coins += morecoins

    # Method to take away coins from user's balance
    def take_coins(self, lesscoins):
        self.coins -= lesscoins

    # Method to remove health from player
    def attacked(self, health):
        for armour in self.armour:
            health -= 5
            for item in Item.items_list:
                if item.name == armour:
                    item.use_armour()
        self.health -= health
        print(f"You now have {self.health} hp remaining!")

    # Method to add health to player
    def healed(self, health):
        self.health += health

    # Method to add item to inventory
    def add_inventory(self, name, quantity):
        if name in crafting_items:
            if name in self.crafting_items:
                self.crafting_items[name] += quantity
            else:
                self.crafting_items[name] = quantity
        elif name in weapons:
            if name in self.weapons:
                self.weapons[name] += quantity
            else:
                self.weapons[name] = quantity
        elif name in armour:
            if name in self.armour:
                self.armour[name] += quantity
            else:
                self.armour[name] = quantity
        elif name in powerups:
            if name in self.powerups:
                self.powerups[name] += quantity
            else:
                self.powerups[name] = quantity
        elif name in misc_items:
            if name in self.misc_items:
                self.misc_items[name] += quantity
            else:
                self.misc_items[name] = quantity
        # Else shouldn't occur as this does not involve user input and is a system process

    # Method to use items in inventory
    def use_inventory(self, name, quantity):
        if name in crafting_items:
            if name in self.crafting_items:
                if self.crafting_items[name] >= quantity:
                    self.crafting_items[name] -= quantity
                    return True
                else: 
                    print("You do not have enough", name, "in your inventory! (You have", self.crafting_items[name] + ")")
                    return False
            else:
                print("You do not have any", name, "in your inventory!")
                return False
        elif name in weapons:
            if name in self.weapons:
                if self.weapons[name] >= quantity:
                    self.weapons[name] -= quantity
                    return True
                else: 
                    print("You do not have enough", name, "in your inventory! (You have", self.weapons[name] + ")")
                    return False
            else:
                print("You do not have any", name, "in your inventory!")
                return False
        elif name in armour:
            if name in self.armour:
                if self.armour[name] >= quantity:
                    self.armour[name] -= quantity
                    return True
                else: 
                    print("You do not have enough", name, "in your inventory! (You have", self.armour[name] + ")")
                    return False
            else:
                print("You do not have any", name, "in your inventory!")
                return False
        elif name in powerups:
            if name in self.powerups:
                if self.powerups[name] >= quantity:
                    self.powerups[name] -= quantity
                    return True
                else: 
                    print("You do not have enough", name, "in your inventory! (You have", self.powerups[name] + ")")
                    return False
            else:
                print("You do not have any", name, "in your inventory!")
                return False
        if name in misc_items:
            if name in self.misc_items:
                if self.misc_items[name] >= quantity:
                    self.misc_items[name] -= quantity
                    return True
                else: 
                    print("You do not have enough", name, "in your inventory! (You have", self.misc_items[name] + ")")
                    return False
            else:
                print("You do not have any", name, "in your inventory!")
                return False
        # Else shouldn't occur as this does not involve user input and is a system process

    # Method to use items in inventory
    def use_inventory_bool(self, name, quantity):
        if name in crafting_items:
            if name in self.crafting_items:
                if self.crafting_items[name] >= quantity:
                    return True
                else: 
                    return False
            else:
                print("You do not have any", name, "in your inventory!")
                return False

    # Method to check inventory
    def check_inventory(self):
        print("Your inventory:\n")
        for item in self.crafting_items:
            quant = self.crafting_items[item]
            if quant > 0:
                print(str(quant) + "x", item)
        for item in self.weapons:
            quant = self.weapons[item]
            if quant > 0:
                print(str(quant) + "x", item)
        for item in self.armour:
            quant = self.armour[item]
            if quant > 0:
                print(str(quant) + "x", item)
        for item in self.powerups:
            quant = self.powerups[item]
            if quant > 0:
                print(str(quant) + "x", item)
        for item in self.misc_items:
            quant = self.misc_items[item]
            if quant > 0:
                print(str(quant) + "x", item)
        if bool(self.crafting_items) == False:
            if bool(self.weapons) == False:
                if bool(self.armour) == False:
                    if bool(self.powerups) == False:
                        if bool(self.misc_items) == False:
                            print("You do not have any items.")

    def is_item(self, item):
        there = False
        for thing in self.crafting_items:
            if thing.lower() == item.lower():
                if self.crafting_items[thing] > 0:
                    there = True
            else:
                there = False
        for thing in self.weapons:
            if thing.lower() == item.lower():
                if self.weapons[thing] > 0:
                    there = True
            else:
                there = False
        for thing in self.armour:
            if thing.lower() == item.lower():
                if self.armour[thing] > 0:
                    there = True
            else:
                there = False
        for thing in self.powerups:
            if thing.lower() == item.lower():
                if self.powerups[thing] > 0:
                    there = True
            else:
                there = False
        for thing in self.misc_items:
            if thing.lower() == item.lower():
                if self.misc_items[thing] > 0:
                    there = True
            else:
                there = False
        return there





        