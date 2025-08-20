# Importing all the required classes and variables required for the program
from cave import *
from cave_setup import *
from character import *
from enemy import *
from items import *
from item_setup import *
from player import *
from character_setup import *

def welcome_sequence():
    # Welcome Screen
    print("===============================================================\n")
    print("Welcome to...\n")
    print("""
     .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
    / .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. |
    \ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
     \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
     / /\                                                            / /\ 
    / /\ \     ____                                                 / /\ |
    \ \/ /    / ___| __ _ __   __ ___                               \ \/ /
     \/ /    | |    / _` |\ \ / // _ \                               \/ / 
     / /\    | |___| (_| | \ V /|  __/                               / /\ 
    / /\ \    \____|\__,_|  \_/  \___|         _                    / /\ |
    \ \/ /    / ___| _ __  _   _  _ __    ___ | |__    ___  _ __    \ \/ /
     \/ /    | |    | '__|| | | || '_ \  / __|| '_ \  / _ \| '__|    \/ / 
     / /\    | |___ | |   | |_| || | | || (__ | | | ||  __/| |       / /\ 
    / /\ \    \____||_|    \__,_||_| |_| \___||_| |_| \___||_|      / /\ |
    \ \/ /                                                          \ \/ /
     \/ /                                                            \/ / 
     / /\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
    / /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ |
    \ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
     `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' 
    """)
    input("< Press Enter to Continue > ")
    print("\x1b[2J\x1b[H",end="")

    # Backstory

    # 1st text box 
    print("Welcome to CAVE CRUNCHER!\n")
    print("===============================================================================================\n")
    print("You were an extremely skilled bounty hunter who had been imprisoned for well over 5 years.\n")
    input("> Press Enter to Continue ")
    print("\x1b[2J\x1b[H",end="")

    # 2nd text box 
    print("Welcome to CAVE CRUNCHER!\n")
    print("===============================================================================================\n")
    print("You were an extremely skilled bounty hunter who had been imprisoned for well over 5 years.\n")
    print("You had nearly lost all hope that you could leave prison until—\n")
    input("> Press Enter to Continue ")
    print("\x1b[2J\x1b[H",end="")

    # 3rd text box 
    print("Welcome to CAVE CRUNCHER!\n")
    print("===============================================================================================\n")
    print("You were an extremely skilled bounty hunter who had been imprisoned for well over 5 years.\n")
    print("You had nearly lost all hope that you could leave prison until—\n")
    print("Government forces approached you with a way to earn your freedom, in return for a small favour—\n")
    input("> Press Enter to Continue ")
    print("\x1b[2J\x1b[H",end="")

    # 4th text box
    print("Welcome to CAVE CRUNCHER!\n")
    print("===============================================================================================\n")
    print("You were an extremely skilled bounty hunter who had been imprisoned for well over 5 years.\n")
    print("You had nearly lost all hope that you could leave prison until—\n")
    print("Government forces approached you with a way to earn your freedom, in return for a small favour—\n")
    print("===============================================================================================\n")
    print("Enemy creatures have infiltrated a top secret cave system guarded by the government's very best...\n")
    input("> Press Enter to Continue ")
    print("\x1b[2J\x1b[H",end="")

    # 5th text box
    print("Welcome to CAVE CRUNCHER!\n")
    print("===============================================================================================\n")
    print("You were an extremely skilled bounty hunter who had been imprisoned for well over 5 years.\n")
    print("You had nearly lost all hope that you could leave prison until—\n")
    print("Government forces approached you with a way to earn your freedom, in return for a small favour—\n")
    print("===============================================================================================\n")
    print("Enemy creatures have infiltrated a top secret cave system guarded by the government's very best...\n")
    print("Your task is to defeat the three monsters that have wreaked havoc inside the caves.\n")
    input("> Press Enter to Continue ")
    print("\x1b[2J\x1b[H",end="")

    # 6th text box
    print("Welcome to CAVE CRUNCHER!\n")
    print("===============================================================================================\n")
    print("You were an extremely skilled bounty hunter who had been imprisoned for well over 5 years.\n")
    print("You had nearly lost all hope that you could leave prison until—\n")
    print("Government forces approached you with a way to earn your freedom, in return for a small favour—\n")
    print("===============================================================================================\n")
    print("Enemy creatures have infiltrated a top secret cave system guarded by the government's very best...\n")
    print("Your task is to defeat the three monsters that have wreaked havoc inside the caves.\n")
    print("If you are successful in this mission, you will be released from prison and granted an unconditional pardon.\n")
    input("> Press Enter to Continue ")
    print("\x1b[2J\x1b[H",end="")

    # 7th text box
    print("Welcome to CAVE CRUNCHER!\n")
    print("===============================================================================================\n")
    print("You were an extremely skilled bounty hunter who had been imprisoned for well over 5 years.\n")
    print("You had nearly lost all hope that you could leave prison until—\n")
    print("Government forces approached you with a way to earn your freedom, in return for a small favour—\n")
    print("===============================================================================================\n")
    print("Enemy creatures have infiltrated a top secret cave system guarded by the government's very best...\n")
    print("Your task is to defeat the three monsters that have wreaked havoc inside the caves.\n")
    print("If you are successful in this mission, you will be released from prison and granted an unconditional pardon.\n")
    print("However, if you fail to do this, you shall immediately be sent back to prison.\n")
    input("> Press Enter to Continue ")
    print("\x1b[2J\x1b[H",end="")

    # 8th text box
    print("Welcome to CAVE CRUNCHER!\n")
    print("===============================================================================================\n")
    print("You were an extremely skilled bounty hunter who had been imprisoned for well over 5 years.\n")
    print("You had nearly lost all hope that you could leave prison until—\n")
    print("Government forces approached you with a way to earn your freedom, in return for a small favour—\n")
    print("===============================================================================================\n")
    print("Enemy creatures have infiltrated a top secret cave system guarded by the government's very best...\n")
    print("Your task is to defeat the three monsters that have wreaked havoc inside the caves.\n")
    print("If you are successful in this mission, you will be released from prison and granted an unconditional pardon.\n")
    print("However, if you fail to do this, you shall immediately be sent back to prison.\n")
    print("===============================================================\n")
    print("Do not ask any more questions. You may begin your journey...\n")
    input("> Press Enter to Continue ")
    print("\x1b[2J\x1b[H",end="")

    # 9th text box
    print("Welcome to CAVE CRUNCHER!\n")
    print("===============================================================================================\n")
    print("You were an extremely skilled bounty hunter who had been imprisoned for well over 5 years.\n")
    print("You had nearly lost all hope that you could leave prison until—\n")
    print("Government forces approached you with a way to earn your freedom, in return for a small favour—\n")
    print("===============================================================================================\n")
    print("Enemy creatures have infiltrated a top secret cave system guarded by the government's very best...\n")
    print("Your task is to defeat the three monsters that have wreaked havoc inside the caves.\n")
    print("If you are successful in this mission, you will be released from prison and granted an unconditional pardon.\n")
    print("However, if you fail to do this, you shall immediately be sent back to prison.\n")
    print("===============================================================\n")
    print("Do not ask any more questions. You may begin your journey...\n")
    print("...\n")
    input("< Press Enter to Continue > ")
    print("\x1b[2J\x1b[H",end="")

def room_info(current_cave):
    print(current_cave.get_name())
    print("===============================================================================================\n")
    print(current_cave.get_description() + "\n")
    character = current_cave.get_character()
    if character is not None:
        print(character.get_description() + "\n")
    input("> Press Enter to Continue ")

def action_list(current_cave):
    action_counter = 1
    print("Here's a list of actions you can perform in this cave:\n")
    if isinstance(current_cave, Mine):
        print(str(action_counter) + ". 'Search': Look for pieces of rusty iron to use for crafting.")
        action_counter += 1
        print(str(action_counter) + ". 'Smelt': Use the furnace to convert rusty items to shiny items for a cost.")
        action_counter += 1
    elif isinstance(current_cave, Nature):
        print(str(action_counter) + ". 'Forage': Try to find sticks to use for crafting.")
        action_counter += 1
    elif isinstance(current_cave, Spider):
        print(str(action_counter) + ". 'Grab': Reach for the spider webs and potentially receive string for crafting.")
        action_counter += 1
    elif isinstance(current_cave, Shop):
        print(str(action_counter) + ". 'Shop': Speak to the shopkeeper and purchase items using coins.")
        action_counter += 1
        print(str(action_counter) + ". 'Sell': Trade your items in exchange for coins from the shopkeeper.")
        action_counter += 1
    elif isinstance(current_cave, Ancient):
        if current_cave.name == "Statue Sanctuary":
            print(str(action_counter) + ". 'Listen': Try to make out what the statues might be whispering.")
            action_counter += 1
        else:
            print(str(action_counter) + ". 'Whisper': Talk to an inanimate statue... Nice one.")
            action_counter += 1
    elif isinstance(current_cave, Outside):
        print(str(action_counter) + ". 'Escape': Try to escape the caves through the opening.")
        action_counter += 1
    elif isinstance(current_cave, Beach):
        print(str(action_counter) + ". 'Talk': Talk to the kangaroo standing in the cave.")
        action_counter += 1

    print(str(action_counter) + ". 'Move': Move to one of the surrounding caves.")
    action_counter += 1
    print(str(action_counter) + ". 'Inventory': Check the contents of your inventory.")
    action_counter += 1
    print(str(action_counter) + ". 'Check': Get the description and durability of items in your inventory.")
    action_counter += 1
    print(str(action_counter) + ". 'Craft': Open the item crafting menu.")
    action_counter += 1
    print(str(action_counter) + ". 'Dig': If you have a shovel, try your luck at finding power-ups!")
    action_counter += 1
    print(str(action_counter) + ". 'Balance': Check how many coins you currently have.")
    action_counter += 1

def weapon_replacer(item_name, player):
    if item_name in ["Rusty Shovel", "Shiny Shovel", "Rusty Sword", "Shiny Sword", "Rusty Arrow", "Shiny Arrow", "Bow"]:
        if player.is_item(item_name) == True:
            player.weapons[item_name] = 0
            for thing in Item.items_list:
                if thing.name == item_name:
                     thing.durability = thing.max_durability

def shop_armour_replacer(item_name, player):
    if item_name == "Shiny Helmet":
        if player.is_item("Rusty Helmet") == True:
            player.armour["Rusty Helmet"] = 0
            for thing in Item.items_list:
                if thing.name == "Rusty Helmet":
                    thing.durability = thing.max_durability
        elif player.is_item("Shiny Helmet") == True:
            player.armour["Shiny Helmet"] = 0
            for thing in Item.items_list:
                if thing.name == "Shiny Helmet":
                    thing.durability = thing.max_durability
    elif item_name == "Shiny Chestplate":
        if player.is_item("Rusty Chestplate") == True:
            player.armour["Rusty Chestplate"] = 0
            for thing in Item.items_list:
                if thing.name == "Rusty Chestplate":
                    thing.durability = thing.max_durability
        elif player.is_item("Shiny Chestplate") == True:
            player.armour["Shiny Chestplate"] = 0
            for thing in Item.items_list:
                if thing.name == "Shiny Chestplate":
                    thing.durability = thing.max_durability
    elif item_name == "Shiny Leggings":
        if player.is_item("Rusty Leggings") == True:
            player.armour["Rusty Leggings"] = 0
            for thing in Item.items_list:
                if thing.name == "Rusty Leggings":
                    thing.durability = thing.max_durability
        elif player.is_item("Shiny Leggings") == True:
            player.armour["Shiny Leggings"] = 0
            for thing in Item.items_list:
                if thing.name == "Shiny Leggings":
                    thing.durability = thing.max_durability
    elif item_name == "Shiny Boots":
        if player.is_item("Rusty Boots") == True:
            player.armour["Rusty Boots"] = 0
            for thing in Item.items_list:
                if thing.name == "Rusty Boots":
                    thing.durability = thing.max_durability
        elif player.is_item("Shiny Boots") == True:
            player.armour["Shiny Boots"] = 0
            for thing in Item.items_list:
                if thing.name == "Shiny Boots":
                    thing.durability = thing.max_durability
        


                
