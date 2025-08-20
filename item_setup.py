from items import *

# Creating instances for all Crafting Items
rusty_iron = Crafting_Items("Rusty Iron")
shiny_iron = Crafting_Items("Shiny Iron")
stick = Crafting_Items("Stick")
string = Crafting_Items("String")

# Setting the sell prices of all Crafting Items
rusty_iron.set_sell_price(5)
shiny_iron.set_sell_price(20)
stick.set_sell_price(10)
string.set_sell_price(30)

# Setting the descriptions of all Crafting Items
rusty_iron.set_description("Rusted iron found in abandoned mines. A useful material for crafting, with a little left to give.")
shiny_iron.set_description("Strong, durable, and sharp! Forged from rusty iron, and perfect for your crafting needs.")
stick.set_description("A small but rare material, a wooden stick! These sticks are needed to craft any weapon.")
string.set_description("A strong, elastic thread perfect for crafting a mighty bow! Also quite rare.")

# Creating instances for all Weapons
rusty_shovel = Weapons("Rusty Shovel", 5, 4)
shovel = Weapons("Shiny Shovel", 5, 10)
rusty_sword = Weapons("Rusty Sword", 15, 2)
sword = Weapons("Shiny Sword", 20, 6)
rusty_arrow = Weapons("Rusty Arrow", 15, 1)
arrow = Weapons("Shiny Arrow", 30, 1)
bow = Weapons("Bow", 0, 10)

# Setting the buy prices of all shiny Weapons
shovel.set_buy_price(50)
sword.set_buy_price(100)
arrow.set_buy_price(40)
bow.set_buy_price(150)

# Setting the sell prices of all Weapons
rusty_shovel.set_sell_price(15)
shovel.set_sell_price(30)
rusty_sword.set_sell_price(30)
sword.set_sell_price(60)
rusty_arrow.set_sell_price(15)
arrow.set_sell_price(30)
bow.set_sell_price(80)

# Setting the descriptions of all Weapons
rusty_shovel.set_description("Useful for digging around to find useful items! Doesn't look like it'll last though...")
shovel.set_description("Useful for digging around to find useful items! Won't do you much good in combat however.")
rusty_sword.set_description("The blade may be falling apart, but it will serve you well in combat.")
sword.set_description("A mighty steel blade that is sure to deal strong blows in any fight.")
rusty_arrow.set_description("A weak arrow to use with your deadly bow. Perhaps you can strengthen it?")
arrow.set_description("A sharp and shiny arrow to strike down your enemies with force!")
bow.set_description("Needed to shoot arrows. This deadly tool can deal a great deal of damage, but there's a chance you miss.")

# Creating instances for all Armour items
rusty_helmet = Armour("Rusty Helmet", 5, 3)
helmet = Armour("Shiny Helmet", 5, 8)
rusty_chestplate = Armour("Rusty Chestplate", 5, 3)
chestplate = Armour("Shiny Chestplate", 5, 8)
rusty_leggings = Armour("Rusty Leggings", 5, 3)
leggings = Armour("Shiny Leggings", 5, 8)
rusty_boots = Armour("Rusty Boots", 5, 3)
boots = Armour("Shiny Boots", 5, 8)

# Setting the buy prices for all Shiny Armour items
helmet.set_buy_price(90)
chestplate.set_buy_price(90)
leggings.set_buy_price(90)
boots.set_buy_price(90)

# Setting the sell prices for all Armour items
rusty_helmet.set_sell_price(20)
helmet.set_sell_price(50)
rusty_chestplate.set_sell_price(20)
chestplate.set_sell_price(50)
rusty_leggings.set_sell_price(20)
leggings.set_sell_price(50)
rusty_boots.set_sell_price(20)
boots.set_sell_price(50)

# Setting the sell prices for all Armour items
rusty_helmet.set_description("Head protection (-5 Damage). However, it's not very sturdy and confidence inspiring...")
helmet.set_description("Strong, sturdy head protection (-5 Damage). Better protect your logic circuits!")
rusty_chestplate.set_description("Upper body protection (-5 Damage). However, it's not very sturdy and confidence inspiring...")
chestplate.set_description("Upper body protection (-5 Damage). You know you want this right?")
rusty_leggings.set_description("Lower body protection (-5 Damage). However, it's not very sturdy and confidence inspiring...")
leggings.set_description("Lower body protection (-5 Damage). It's nice to be able to move around.")
rusty_boots.set_description("Feet protection (-5 Damage). However, it's not very sturdy and confidence inspiring...")
boots.set_description("Feet protection (-5 Damage). It's more useful than you'd think.")

# Creating instances for all Power Ups
attack_shroom = Powerups("Attack Shroom")
defence_shroom = Powerups("Defence Shroom")
speed_shroom = Powerups("Speed Shroom")
heal_shroom = Powerups("Heal Shroom")

# Setting the buy prices for all Power Ups
attack_shroom.set_buy_price(40)
defence_shroom.set_buy_price(40)
speed_shroom.set_buy_price(30)
heal_shroom.set_buy_price(30)

# Setting the sell prices for all Power Ups
attack_shroom.set_sell_price(30)
defence_shroom.set_sell_price(30)
speed_shroom.set_sell_price(20)
heal_shroom.set_sell_price(20)

# Setting the descriptions for all Power Ups
attack_shroom.set_description("Found by digging. When consumed, attacks do 50% more damage for the next two turns.")
defence_shroom.set_description("Found by digging. When consumed, damage from enemies in the next two turns is reduced by 50%.")
speed_shroom.set_description("Found by digging. When consumed, you are guaranteed to be able to escape any fight.")
heal_shroom.set_description("Found by digging. When consumed, you recover 20 HP.")

# Creating instances for all miscellaneous items
vegemite = Item("Vegemite")
atomic_bomb = Item("Atomic Bomb")

# Setting the buy price of vegemite
vegemite.set_buy_price(500)

# setting the descriptions of all miscellaneous items
vegemite.set_description("An outlandish, thick, salty paste that you bought from a talking kangaroo. What could this do?")
atomic_bomb.set_description("A prototype of the world's deadliest weapon. Will instantly defeat any normal enemy.")