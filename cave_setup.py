from cave import *

# Creating all mine caves
mine1 = Mine("Ore Refinery", 3)
mine2 = Mine("Miner's Forge", 7)
mine3 = Mine("Prospecting Site", 10)
mine4 = Mine("Damp Quarry", 12)

# Giving all mine caves descriptions
mine1.set_description("An abandoned ore refinery. You find yourself surrounded by furnaces and broken machinery.")
mine2.set_description("An abandoned miner's forge. Cracked crucibles lie on the floor next to toppled anvils.")
mine3.set_description("A prospecting site. It seems to have been abandoned before mining operations could begin.")
mine4.set_description("A damp quarry. The constant dripping of liquid from the stalactites overhead has covered all equipment here.")

# Creating all nature caves
nature1 = Nature("Abandoned Greenhouse", 2)
nature2 = Nature("Mossy Midsts", 6)
nature3 = Nature("Withered Wilds", 16)

# Giving all nature caves descriptions
nature1.set_description("The abandoned greenhouse. Rays of light shine from cracks in the ceiling, and roots cover the walls of the cave.")
nature2.set_description("The mossy midsts. The entire cave is lit with the eerie green glow of moss, which covers all surfaces in sight.")
nature3.set_description("The withered wilds. All that remains is the decayed plants that depressingly lay on the floor.")

# Creating all spider caves
library = Spider("Mineshaft Library", 9)
quarters = Spider("Miner's Quarters", 13)

# Giving all spider caves descriptions
library.set_description("The miners' library. Thick spiderwebs descent from the ceiling onto the hollow bookshelves.")
quarters.set_description("The miner's quarters. What once used to full of exhausted workers is now home to many cave-dwelling spiders.")

# Creating all ancient caves
whispering = Ancient("Statue Sanctuary", 5)
listening = Ancient("Ruins of Repetition", 19)

# Giving all ancient caves descriptions
whispering.set_description("The statue sanctuary. A room filled with ancient statues all staring at you.\nYou can't shake the feeling that you're being watched and that the statues are silently whispering something.")
listening.set_description("The ruins of repetition. You are forced to walk over the broken remains of ancient statues.\nYou think you can hear the only standing statue saying something.")

# Creating outside cave
exit = Outside("Windy Wakes", 18)

# Giving the outside cave a description
exit.set_description("You stumble into a cave flooded with light. There is an opening in the rocks, leading outside the caves.")

# Creating beach cave
beach = Beach("Grainy Grotto", 14)

# Giving the beach cave a description
beach.set_description("Soft sand cushions your foosteps as you walk through this obscure, almost beach-like cave.")

# Creating all battle caves
battle1 = Battle("Stalactite Theatre", 4)
battle2 = Battle("Daunting Dungeons", 17)
boss = Battle("Mystic Hollow", 8)

# Giving all the battle caves descriptions
battle1.set_description("This is where Ye resides. Prepare to fight!")
battle2.set_description("A wild Drizzy is storming about this cave. Your job is to hunt him down and subdue him.")
boss.set_description("You feel an eerie tingling sensation as gusts of wind emerge from the darkness ahead.\nCharge ahead and defeat the Wumpus!")

# Creating all shop caves
kanyeshop = Shop("Kanye's Shop", 1)
cliveshop = Shop("Clive's Camp", 11)
rookshop = Shop("Rook's Repository", 15)

# Giving all the shop caves descriptions
kanyeshop.set_description("You are at Kanye's Shop! The cave is covered with a dark cloth, with the occassional splash of colour.")
cliveshop.set_description("You are at Clive's Shop! You are inside a brightly lit tent filled with weapons, power ups and camping gear.")
rookshop.set_description("You are at Rook's Shop! The cave is dimly lit by a two lanterns, one above Rook and the other near the Shop.")

# Creating Oppenheimer's lair
oppenheimer = Cave("Oppenheimer's Lair", 20)

# Giving Oppenheimer's lair a description
oppenheimer.set_description("You have ventured into an ancient prison, one which contains the infamous scientist, OPPENHEIMER!")

# Using the text document to link all caves
with open("linked_caves.txt", 'r') as links:
    for line in links:
        line = line.strip()
        line = line.replace(" ", "")
        separate = line.split(",")
        for cave in Cave.cave_list:
            if cave.cave_id == int(separate[0]):
                cave.link_cave(separate[1], int(separate[2]))

# Linking oppenheimer's lair to the respective caves
oppenheimer.link_cave("north-west", 19)
oppenheimer.link_cave("south-east", 5)

# Placing chests
battle1.set_chestStat("yes")
battle2.set_chestStat("yes")
quarters.set_chestStat("yes")
