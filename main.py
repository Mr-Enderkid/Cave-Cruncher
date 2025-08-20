# Importing all the required classes and variables required for the program
from cave import *
from cave_setup import *
from character import *
from enemy import *
from items import *
from item_setup import *
from player import *
from character_setup import *
from game_functions import *
from crafting import *
import random

# Create the player instance and set the current location
player = Player(100, 20)
player.set_cave(kanyeshop)
dead = False
upuse = False
player.add_inventory("Shiny Sword", 1)

# Welcome Screen
welcome_sequence()

# Previous cave storage
cave_1 = None
cave_2 = None
alr_searched = False
vegemite_sold = False
damage_boost = 1
defence_boost = 1
speed_boost = 1
poweruptimer = 0

while dead == False:
    current_cave = player.get_cave()
    room_info(player.get_cave())
    print("")
    print("===============================================================================================\n")
    if isinstance(current_cave.character, Enemy):
        fight = True
        enemy = current_cave.get_character()
        print("You are fighting...", str(enemy.name) + "!")
        while fight == True:
            player.check_inventory()
            weapon = input("Which weapon/item are you going to use? ")
            for item in Item.items_list:
                if (item.get_name()).lower() == weapon.lower():
                    damage = item.get_damage()
                    enemy.defend(damage)
                    item.use_weapon()
            enemy_damage = enemy.attack()
            player.attacked(enemy_damage)
            if player.health <= 0:
                print("game over")
                fight = True
                dead = True
    else:
        action_list(player.get_cave())
        action = input("\nWhich action would you like to perform (enter name)? ")
        print("\n===============================================================================================\n")
        # Move command
        if action.lower() == "move":
            current_cave.move_menu()
            print("")
            move_to = int(input("Which cave would you like to move to (enter position in menu): "))
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
            cave_2 = cave_1
            cave_1 = current_cave
            alr_searched = False
            player.set_cave(current_cave.move(move_to))
        # Inventory command
        elif action.lower() == "inventory":
            player.check_inventory()
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Check command
        elif action.lower() == "check":
            which = input("Which item would you like to check? ")
            print("")
            has = player.is_item(which)
            if has == False:
                print("You do not have the specified item.")
            else:
                for item in Item.items_list:
                    if (item.name).lower() == which.lower():
                        print(item.get_description())
                        if isinstance(item, Weapons) or isinstance(item, Armour):
                            print("The durability of the item is:", str(item.durability) + "/" + str(item.max_durability))
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Dig command
        elif action.lower() == "dig":
            if current_cave.dug == False:
                if player.is_item("Rusty Shovel") or player.is_item("Shiny Shovel") == True:
                    chance = random.randint(1, 5)
                    if chance == 4:
                        whichone = random.randint(1,4)
                        item = ""
                        match whichone:
                            case 1: item = "Attack Shroom"
                            case 2: item = "Defence Shroom"
                            case 3: item = "Speed Shroom"
                            case 4: item = "Heal Shroom"
                        print("WOW! You found a", item, "while digging!")
                    else:
                        print("Unlucky. You didn't find anything while digging.")
                    current_cave.set_dug()
                    if player.is_item("Rusty Shovel") == True:
                        rusty_shovel.use_weapon()
                    elif player.is_item("Shiny Shovel") == True:
                        shovel.use_weapon()
                else:
                    print("You do not have a shovel.")
            else:
                print("You cannot dig here again!")
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Balance command
        elif action.lower() == "balance":
            print("Your coins balance is:", player.get_coins(), "coins.\n")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Search command
        elif action.lower() == "search":
            if isinstance(current_cave, Mine):
                if current_cave == cave_1 or current_cave == cave_2 or alr_searched == True:
                    print("You have already searched here in the past two turns!")
                else:
                    num_iron = random.randint(1, 5)
                    print("You searched the mine and found", num_iron, "pieces of Rusty Iron!")
                    player.add_inventory("Rusty Iron", num_iron)
                    alr_searched = True
            else: 
                print("You are not in a mine! You cannot search here!")
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Forage command
        elif action.lower() == "forage":
            if isinstance(current_cave, Nature):
                if current_cave == cave_1 or current_cave == cave_2 or alr_searched == True:
                    print("You have already foraged here in the past two turns!")
                else:
                    chance = random.randint(1,2)
                    if chance == 2:
                        num_sticks = random.randint(1, 2)
                        print("You foraged the cave and found", num_sticks, "sticks!")
                        player.add_inventory("Stick", num_sticks)
                    else:
                        print("Unlucky. You didn't manage to find any sticks.")
                    alr_searched = True
            else: 
                print("You are not in a nature cave! You cannot forage here!")
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Grab command
        elif action.lower() == "grab":
            if isinstance(current_cave, Spider):
                if current_cave == cave_1 or current_cave == cave_2 or alr_searched == True:
                    print("You have already looked around here in the past two turns!")
                else:
                    chance = random.randint(1,10)
                    if chance == 6:
                        num_string = random.randint(1, 2)
                        print("You searched the cave and grabbed", num_string, "string!")
                        player.add_inventory("String", num_string)
                    else:
                        print("Unlucky. You didn't manage to find any sticks.")
                    alr_searched = True
            else: 
                print("You are not in a spider cave! You cannot grab here!")
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Shop command
        elif action.lower() == "shop":
            if isinstance(current_cave, Shop):
                shop_action = "buy"
                shopkeeper = current_cave.get_character()
                print(">", str(shopkeeper.name) + ":", str(shopkeeper.speak()))
                while shop_action.lower() == "buy":
                    print("")
                    shopkeeper.shopping_list()
                    print("")
                    shop_action = input("Choose action: Buy or Leave? ")
                    print("")
                    if shop_action.lower() == "leave":
                        print(shopkeeper.end_speak())
                    else:
                        print("Quick note: You cannot own multiple sets of armour, and only one of each weapon type.\nIf a new set is bought, the old one will disappear.")
                        buying_item = input("What will you be buying (enter name)? ")
                        if shopkeeper.check_stock(buying_item) == False:
                            print("Sorry. That item's not in stock anymore.")
                        else:
                            price = int(shopkeeper.item_price(buying_item))
                            balance = player.get_coins()
                            if balance >= price:
                                shopkeeper.sold_item(buying_item)
                                item_name = shopkeeper.item_name(buying_item)
                                weapon_replacer(item_name, player)
                                shop_armour_replacer(item_name, player)
                                player.add_inventory(item_name, 1)
                                player.take_coins(price)
                                print("You bought a", item_name, "from the shop!") 
                            else:
                                print("You cannot afford that item.")
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Listen command
        elif action.lower() == "listen":
            if isinstance(current_cave, Ancient):
                if current_cave == whispering:
                    print("")
                    print("The statue seems to be saying:\ncan You you free, but should me?")
                    print("Nothing else seems to be happening.")
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Whisper command
        elif action.lower() == "whisper":
            if isinstance(current_cave, Ancient):
                if current_cave == listening:
                    want = True
                    while want == True:
                        guess = input("You can hear the statue mumbling 'I need you to tell me something...' ")
                        if guess.lower() == "you can free me, but should you?":
                            player.set_cave(current_cave.move(oppenheimer))
                            want = False
                        else:
                            want = input("Nothing happened. Do you wish to continue or stop ('continue' or 'stop')? ")
                            if want.lower() == "stop":
                                want = False
                            else:
                                want = True
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Escape command
        elif action.lower() == "escape":
            if isinstance(current_cave, Outside):
                sure = input("Are you sure you want to try and escape (Y/N)? ")
                if sure.lower() == "n":
                    print("Okay then.")
                else:
                    print("You crawl out of the cave system, only to be immediately captured by government agents.")
                    print("You have been imprisoned once again.")
                    print("Game Over.")
                    dead = True
            else:
                print("You cannot use this command here!")
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Talk command
        elif action.lower() == "talk":
            if isinstance(current_cave, Beach):
                print("G'day mate. How are ya?")
                lol = input("> ")
                print("Nice. I'm Joey the kangaroo, the lone surfer of these caves. I must say, this one really resonates with me.")
                if vegemite_sold == False:
                    buy_vegemite = input("Anyway. Would you like to buy this jar of Vegemite for 500 coins (Y/N)? ")
                    if buy_vegemite.lower == "y":
                        balance = player.get_coins()
                        if balance < 500:
                            print("Mate, I'm sorry to disappoint you, but you don't have enough coins to get this one off me.\nCome back some other time won't you?")
                        else:
                            print("Pleasure doing business with you mate! The taste is truly quite acquired. I'll see you around then!")
                            print("You acquired a jar of Vegemite!")
                            player.add_inventory("Vegemite", 1)
                            player.take_coins(500)
                            vegemite_sold = True
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Sell command
        elif action.lower() == "sell":
            if isinstance(current_cave, Shop):
                selling = True
                while selling == True:
                    player.check_inventory()
                    sell_input = input("What do you have for me, traveller? ")
                    for item in Item.items_list:
                        if (item.name).lower() == sell_input.lower():
                            selling_price = item.get_sell_price()
                            item_name = item.get_name()
                            if isinstance(item, Armour) or isinstance(item, Weapons):
                                durability = item.durability
                                max_dura = item.max_durability
                                dura_frac = durability / max_dura
                                selling_price = int(selling_price * dura_frac)
                    if player.is_item(item_name) == True:
                        print("Value of", item_name, "=", str(selling_price), "coins.")
                        confirm = input("Are you sure you want to sell the item (Y/N)? ")
                        if confirm.lower() == "y":
                            print("Pleasure doing business with you.")
                            player.add_coins(selling_price)
                            player.use_inventory(item_name, 1)
                        else:
                            print("Changed your mind? Fine with me.")
                    else:
                        print("You do not have that item.")
                    selling = input("Do you want to sell another item (Y/N)? ")
                    if selling.lower() == "y":
                        selling = True
                    else:
                        selling = False
            else:
                print("There is no one to sell to.")
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        # Craft Command
        elif action.lower() == "craft":
            print("CRAFTING COST = 20 COINS")
            print("List of craftable items:\n")
            count = 1
            crafted = True
            for item in Item.craftable_items:
                print(str(count) + ".", item)
                count += 1
            print("")
            choose = input("Choose:\n1. Find Recipe\n2. Craft Items\nEnter number: ")
            if choose == "1":
                which_craft = input("Which item do you want to view the recipe for? ")
                for item in Item.items_list:
                    if (item.name).lower() == which_craft.lower():
                        print("To craft,", item.name, "you need:")
                        for ing in item.crafting:
                            print(str(item.crafting[ing]) + "x", ing)
            else:
                balance = player.get_coins()
                if balance >= 20:
                    which_tocraft = input("Which item do you want to craft? ")
                    for item in Item.items_list:
                        if (item.name).lower() == which_tocraft.lower():
                            tocraft = item.name
                            itemd = item
                    for ing in itemd.crafting:
                        if player.use_inventory_bool(ing, itemd.crafting[ing]) == False:
                            crafted = False
                        else:
                            player.use_inventory(ing, itemd.crafting[ing])
                    if crafted == False:
                        print("Crafting failed.")
                    else:
                        print("Crafting successful! You crafted a", tocraft, "!")
                        player.add_inventory(tocraft, 1)
                else:
                    print("You do not have enough coins.")
            print("")
            input("> Press Enter to Continue ")
            print("\n===============================================================================================\n")
            print("\x1b[2J\x1b[H",end="")
        elif Enemy.enemies_left == 0:
            print("Congrats! You beat the game!")
            dead = True


                            


                            
                
