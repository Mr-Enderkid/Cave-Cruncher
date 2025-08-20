from items import *


class Shopkeeper:
    # Constructor method
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.dialogue = None
        self.leaving_dialogue = None
        self.shop_inventory = {
            "Shiny Shovel": 0,
            "Shiny Sword": 0,
            "Shiny Arrow": 0,
            "Bow": 0,
            "Shiny Helmet": 0, 
            "Shiny Chestplate": 0,
            "Shiny Leggings": 0,
            "Shiny Boots": 0,
            "Attack Shroom": 0,
            "Defence Shroom": 0,
            "Speed Shroom": 0,
            "Heal Shroom": 0
        }

    # Method to get shopekeeper's name
    def get_name(self):
        return self.name
    
    # Method to get shopkeeper's description
    def get_description(self):
        return self.description
    
    # Method to set shopkeeper's dialogue
    def set_dialogue(self, dialogue):
        self.dialogue = dialogue

    # Method to get the shopkeeper's dialogue 
    def speak(self):
        return self.dialogue
    
     # Method to set shopkeeper's dialogue as you leave the shop
    def set_leaving_dialogue(self, dialogue):
        self.leaving_dialogue = dialogue

    # Method to get the shopkeeper's dialogue as you leave the shop
    def end_speak(self):
        return self.leaving_dialogue
    
    # Method to set the shopkeeper's inventory
    def set_inventory(self, shovel, sword, arrows, bow, helmet, chestplate, leggings, boots, attack, defence, speed, heal):
        self.shop_inventory["Shiny Shovel"] = shovel
        self.shop_inventory["Shiny Sword"] = sword
        self.shop_inventory["Shiny Arrow"] = arrows
        self.shop_inventory["Bow"] = bow
        self.shop_inventory["Shiny Helmet"] = helmet
        self.shop_inventory["Shiny Chestplate"] = chestplate
        self.shop_inventory["Shiny Leggings"] = leggings
        self.shop_inventory["Shiny Boots"] = boots
        self.shop_inventory["Attack Shroom"] = attack
        self.shop_inventory["Defence Shroom"] = defence
        self.shop_inventory["Speed Shroom"] = speed
        self.shop_inventory["Heal Shroom"] = heal

    # Method to check if item is in stock
    def check_stock(self, item):
        for items in self.shop_inventory:
            if items.lower() == item.lower():
                if self.shop_inventory[items] == 0:
                    return False
                else:
                    return True
            else:
                return False
                
    # Method to check if player has enough money
    def item_price(self, item):
        for good in Item.items_list:
            if (good.name).lower() == item.lower():
                price = good.get_buy_price()
                return price
        
    # Method to adjust stock of item if sold
    def sold_item(self, item):
        for items in self.shop_inventory:
            if items.lower() == item.lower():
                if self.shop_inventory[items] >= 1:
                    self.shop_inventory[items] -= 1
                else:
                    return False
                
    def item_name(self, item):
        for items in self.shop_inventory:
            if items.lower() == item.lower():
                return items

    # Method to provide a list of all items
    def shopping_list(self):
        list_no = 1
        for item in self.shop_inventory:
            goods = item
            quant = self.shop_inventory[item]
            for thing in Item.items_list:
                if thing.name == goods:
                    price = thing.get_buy_price()
            lengthgoods = len(goods)
            if quant < 10:
                spaces_required = 20 - lengthgoods
            else:
                spaces_required = 19 - lengthgoods
            spaces = "-" * spaces_required
            if list_no > 9:
                print(str(list_no) + ".", str(quant) + "x", goods, spaces, "Price: $" + str(price))
            else:
                print(str(list_no) + ". ", str(quant) + "x", goods, spaces, "Price: $" + str(price))
            list_no += 1
            



        