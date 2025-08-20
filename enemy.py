from cave_setup import *

class Enemy:
    # Creating a variable to track number of enemies left in the game
    enemies_left = 0

    # Constructor method
    def __init__(self, name, description, hp):
        Enemy.enemies_left += 1
        self.spl_atkCounter = 0
        self.name = name
        self.description = description
        self.health = hp
        self.atk = None
        self.spl_atk = None
        self.atk_dmg = 0
        self.spl_atk_dmg = 0
        self.spl_atk_freq = 0
    
    # Method to get enemy name
    def get_name(self):
        return self.name
    
    # Method to get enemy description
    def get_description(self):
        return self.description
    
    # Method to set attack
    def set_attack(self, atk_name, damage):
        self.atk = atk_name
        self.atk_dmg = damage

    # Method to set special attack
    def set_spl_attack(self, atk_name, damage, frequency):
        self.spl_atk = atk_name
        self.spl_atk_dmg = damage
        self.spl_atk_freq = frequency

    # Method to attack the player
    def attack(self):
        if self.spl_atkCounter < self.spl_atk_freq:
            print(">", self.name, "uses", self.atk, "on you, dealing", self.atk_dmg, "to you!")
            self.spl_atkCounter += 1
            return self.atk_dmg
        else:
            print(">", "SPECIAL ATTACK!", self.name, "USES", self.spl_atk, "ON YOU, DEALING", self.spl_atk_dmg, "TO YOU!")
            self.spl_atkCounter = 0
            return self.spl_atk_dmg
        
    # Method to defend against the player's attacks
    def defend(self, damage):
        self.health -= damage
        if self.health > 0:
            print(self.name, "is now at", self.health, "HP!")
        else:
            print(self.name, "is now at 0 HP!")
            print("Congratulations! You have defeated", self.name + "!")
            Enemy.enemies_left -= 1
            print("There are", Enemy.enemies_left, "enemies left to defeat.")
            if self.name == "Ye":
                battle1.character = None
            elif self.name == "Drizzy":
                battle2.character = None
            elif self.name == "Wumpus":
                boss.character = None

    # Method to signal the end of the game
    def endgame(self):
        if Enemy.enemies_left > 0:
            return False
        else:
            return True
