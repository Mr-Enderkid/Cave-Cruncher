from character import *
from cave_setup import *
from cave import *
from enemy import *

kanye = Shopkeeper("Kanye", "You're looking at Kanye, a visionary shopkeeper inside his outlandish shop.")
kanyeshop.set_character(kanye)
kanye.set_dialogue("Hmm things don't seem right in the caves these days...\nWait who are you?\n...\nOh you're here to buy things? Don't overstay your visit.")
kanye.set_leaving_dialogue("Leaving so soon? Just remember, I am the best shopkeeper in the world. No controversy.")
kanye.set_inventory(2, 1, 5, 1, 1, 1, 1, 1, 2, 2, 2, 2)

rook = Shopkeeper("Rook", "Here resides Rook, a hooded figure who reveals nothing but his smile - and his vast shop inventory!")
rookshop.set_character(rook)
rook.set_dialogue("Oh, hello traveller.\nIt's strange that you come to these parts, especially with the recent activity in the area...\nTake a look around while you're here.")
rook.set_leaving_dialogue("It's a pity you're leaving so soon. Stay safe out there traveller!")
rook.set_inventory(2, 2, 10, 2, 2, 2, 2, 2, 4, 4, 4, 5)

clive = Shopkeeper("Clive", "Here's Clive, a man who loves his camping! He also runs a shop to afford the hobby!")
cliveshop.set_character(clive)
clive.set_dialogue("Oh? OH. OH MY GOD!\nDo my eyes deceive me or do I see one who enjoys the thrill of adventure and travel?\nMake yourself welcome here, take a look around at all the goods!")
clive.set_leaving_dialogue("Make sure to enjoy these beautiful caves, but also stay cautious. A violent creature passed through here only a while back...")
clive.set_inventory(2, 1, 5, 1, 1, 1, 1, 1, 3, 3, 3, 5)

ye = Enemy("Ye", "An egotistical beast who produced deadly screeching sounds.", 30)
ye.set_attack("Modern Screech", 10)
ye.set_spl_attack("Nostalgic Bars", 25, 3)
battle1.set_character(ye)

drizzy = Enemy("Drizzy", "A very popular monster until you're face to face with him.", 50)
drizzy.set_attack("Beefy Revenge", 15)
drizzy.set_spl_attack("Crowd Rush", 35, 3)
battle2.set_character(drizzy)

wumpus = Enemy("Wumpus", "A gigantic beast with razor sharp teeth. This is the boss enemy.", 100)
wumpus.set_attack("Claw Swipe", 20)
wumpus.set_spl_attack("Mega Chomp", 40, 3)
boss.set_character(wumpus)