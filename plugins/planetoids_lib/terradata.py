########Terra########
from random import randint
# with anything in brackets, (3,4), for example, the former number needs to be smaller


trees = 10
terrachestcount = 400  #if over 500 with planetoids terraria will crash

chasms = randint(4, 5)  #means there are at least 4 and up to 5 chasms
#chasms = 4 # this is what you do if you want to force a number
chasmthickness = 0.045  #thickness in radians of the terra circle
chasmdeepness = (50, 75)  #in percent of radius

altar_count = 30  #amount for Terra
max_altar_planet = 50

caverns = 1.2  #multiplied with root of size
cavernsize = (5, 10)  #(minsize, maxsize) of cave "subplanetoids"

dirtcaverns = 0.2  #these are close to surface, the ones with dirt background
dirtcavernsize = (7, 30)  #(minsize, maxsize)

water = 0.1  #watercave
watersize = (10, 20)

lava = 0.05  #lavacave
lavasize = (5, 15)

#jungle
jcircle = 0.3
jcirclesize = (3, 10)

jrect = 0.07
jrectsize = (5, 20)

jdot = 1.0

jarc = 0.05  #junglegrassarcamount
jarcsize = (10, 150)

#             name,minradius,maxradius,amount,(minsize, maxsize)
#amount is multiplied with the root of the terra size
planetdata = [("Stone Block", 0.9999, 1.00, 0.01, (10, 15)),
              ("Clay Block", 0.9999, 1.00, 0.005, (3, 5)),
              ("Stone Block", 0.5, 0.98, 0.3, (5, 20)),
              ("Sand Block", 0.6, 0.98, 0.2, (10, 25)),
              ("Silt Block", 0.55, 0.97, 0.1, (1, 30)),
              ("Clay Block", 0.5, 0.9, 0.2, (10, 20)),
              ("Grass Block", 0.5, 0.99, 1.0, (1, 5)),
              ("Dirt Block", 0.25, 0.5, 0.1, (5, 25)),
              ("Cobweb", 0.25, 0.9, 0.1, (3, 5)),
              ("Iron Ore", 0.25, 0.7, 0.5, (3, 5)),
              ("Copper Ore", 0.25, 0.9, 0.8, (3, 5)),
              ("Silver Ore", 0.25, 0.5, 0.3, (2, 5)),
              ("Gold Ore", 0.25, 0.4, 0.2, (1, 4)),
              ("Demonite Ore", 0.2, 0.3, 0.1, (1, 3)),
              ("Wood", 0.9, 0.97, 0.2, (5, 10)),
              ("Mushroom Grass Block", 0.2, 0.5, 0.1, (5, 7)),
              ("Gem Sapphire", 0.2, 0.9, 2.0, (1, 1)),
              ("Gem Ruby", 0.2, 0.9, 2.0, (1, 1)),
              ("Gem Emerald", 0.2, 0.9, 2.0, (1, 1)),
              ("Gem Topaz", 0.2, 0.9, 2.0, (1, 1)),
              ("Gem Amethyst", 0.2, 0.9, 2.0, (1, 1)),
              ("Gem Diamond", 0.2, 0.9, 2.0, (1, 1)),
              ("Spike", 0.2, 0.9, 10.0, (1, 1))]


###chestdata###

potions = {'Swiftness Potion': 1,
           'Battle Potion': 1,
           'Shine Potion': 1,
           'Gills Potion': 1,
           'Gravitation Potion': 1,
           'Water Walking Potion': 1,
           'Invisibility Potion': 1,
           'Magic Power Potion': 1,
           'Healing Potion': 1,
           'Thorns Potion': 1,
           'Regeneration Potion': 1,
           'Night Owl Potion': 1,
           'Mana Regeneration Potion': 1,
           'Archery Potion': 1,
           'Hunter Potion': 1,
           'Restoration Potion': 1,
           'Lesser Healing Potion': 1,
           'Featherfall Potion': 1,
           'Spelunker Potion': 1,
           'Obsidian Skin Potion': 1,
           'Ironskin Potion': 1,
           }
accessoires = {
    "Anklet of the Wind": 1.0,
    #"Copper Watch":1,
    "Aglet": 1,
    #"Silver Watch":1,
    "Nature's Gift": 0.3,
    #"Depth Meter":1,
    "Hermes Boots": 0.5,
    #"Rocket Boots":1,
    "Cobalt Shield": 0.25,
    "Shiny Red Balloon": 1,
    #"Gold Watch":1,
    "Flipper": 1,
    "Band of Regeneration": 1,
    "Cloud in a Bottle": 1,
    #"Guide Voodoo Doll":1,
    "Band of Starpower": 1,
    "Lucky Horseshoe": 1,
    #"Obsidian Skull":1,
    #"Shackle":1,
    "Feral Claws": 0.7,
    'Magic Mirror': 1,
    'Breathing Reed': 1,
    "Angel Statue": 1  #yep, always good
}
weapons = {'Wooden Boomerang': 1,
           'Dynamite': 0.75,
           'Grenade': 0.9,
           'Bomb': 0.8,
           'Aqua Scepter': 0.2,
           'Trident': 0.3,
           'Enchanted Boomerang': 0.4,
           'Handgun': 0.25,
           'Blue Moon': 0.2,
           'Staff of Regrowth': 0.2,
           'Dark Lance': 0.15,
           'Muramasa': 0.25,
           "Flower of Fire": 0.2,
           "Sunfury": 1,
           "Angel Statue": 1}

other = {"Jester's Arrow": 0.7,
         'Hellfire Arrow': 0.8,
         'Bottle': 1,
         'Silver Bullet': 1,
         "Suspicious Looking Eye": 0.7,
         "Worm Food": 0.6,

         "Cobweb": 1,
         "Bone": 0.7,
         "Musket Ball": 1}

healthperchest = (0, 1)  #(min, max)
starsperchest = (0, 2)
###chestdata end###


#####planetoids#####

#chestdata for planetoids
itemdata = {'Swiftness Potion': 100, 'Cloud in a Bottle': 25, 'Sandstorm in a Bottle' : 25,
            'Flying Carpet' : 10, "Pharaoh's Robe" : 10, "Pharaoh's Mask" : 10,
            'Ice Boomerang' : 10, 'Ice Blade': 10, 'Ice Skates' : 10, 'Snowball Cannon' : 10,
            'Blizzard in a Bottle' : 25, 'Flurry Boots' : 10, 'Fish' : 2,
            'Lucky Horseshoe': 10, 'Gold Bar': 250, 'Shiny Red Balloon': 10,
            'Wooden Arrow': 500, 'Throwing Knife': 500,
            'Wooden Boomerang': 20, 'Flipper': 10, 'Blowpipe': 5, 'Dynamite': 300,
            'Band of Regeneration': 50, 'Flaming Arrow': 500, 'Starfury': 3,
            'Battle Potion': 50, 'Hellfire Arrow': 500, 'Umbrella' : 5,
            'Shine Potion': 100, 'Trident': 7, 'Gills Potion': 100,
            'Silver Bar': 250, 'Gravitation Potion': 300, "Water Walking Boots" : 10,
            'Regeneration Potion': 50, 'Water Walking Potion': 50,
            'Invisibility Potion': 50, 'Magic Mirror': 30, "Beach Ball" : 50,
            'Magic Power Potion': 100, 'Glowstick': 750, 'Healing Potion': 500,
            'Enchanted Boomerang': 50, "Shoe Spikes" : 10, "Climbing Claws" : 10,
            'Flare Gun' : 5, 'Flare' : 500, 'Lava Charm' : 10,
            'Staff of Regrowth': 3, 'Night Owl Potion': 100,
            'Thorns Potion': 100, 'Mana Regeneration Potion': 100,
            'Archery Potion': 100, 'Feral Claws': 10, 'Gold Coin': 300,
            'Hunter Potion': 100, 'Bottle': 300, 'Silver Bullet': 750,
            'Iron Bar': 250, 'Breathing Reed': 10,
            'Grenade': 100, 'Aglet': 20, 'Restoration Potion': 300,
            'Hermes Boots': 30, "Extractinator" : 5,
            'Bomb': 500, 'Spear': 10, 'Lesser Healing Potion': 200,
            'Silver Coin': 5000, 'Torch': 3000, 'Anklet of the Wind': 10,
            'Featherfall Potion': 100, "Jester's Arrow": 1000,
            'Shuriken': 1000, 'Copper Bar': 250, 'Obsidian Skin Potion': 100,
            'Spelunker Potion': 100, 'Lesser Restoration Potion': 100,
            'Ironskin Potion': 100, "Life Crystal": 150, "Fallen Star": 250,
            "Suspicious Looking Eye": 100, "Worm Food": 100,
            "Book": 1000, "Wood": 2000,
            "Cobweb": 3000, "Bone": 300, "Musket Ball": 1000, "Meteorite": 500,
            "Flesh Cloning Vat" : 2, "Glass Kiln" : 2, "Honey Dispenser" : 2,
            "Ice Machine" : 2, "Lihzahrd Furnace" : 2, "Living Loom" : 2,
            "Sky Mill" : 2, "Living Wood Wand" : 2, "Leaf Wand" : 2,
            "Web Slinger" : 10, "Jungle Key Mold" : 2, "Corruption Key Mold" : 2,
            "Crimson Key Mold" : 2, "Hallowed Key Mold" : 2, "Frozen Key Mold" : 2,
            "Abeemination" : 10, "Wooden Crate" : 100, "Compass" : 10, "Ruler" : 10,
            "Slime Crown" : 10, "Music Box" : 10, "Lens" : 50, "Bezoar" : 2, "Nazar" : 2,
            "Water Bolt" : 5, "Water Candle" : 10,
            }

goldlockitemdata = {'Muramasa': 4, 'Handgun': 4, 'Blue Moon': 4, 'Magic Missile': 4, 'Cobalt Shield': 4,
                    'Aqua Scepter': 4, 'Shadow Key' : 4}
#extra format: (itemname, amount)
goldlockextra = (("Life Crystal", 1), ("Bone", 10), ("Golden Key", 1), ("Iron Crate", 1), ("Present", 1))
itemspergoldchest = 2

shadowlockitemdata = {"Demon Wings" : 1, "Angel Wings" : 1, "Bee Wings" : 1, "Butterfly Wings" : 1, "Fairy Wings" : 1,
                      'Dark Lance': 2, "Flamelash" : 2, "Flower of Fire": 2, "Sunfury" : 2, "Lihzahrd Altar" : 4,
                      "Moon Charm" : 1, "Neptune's Shell" : 1,
                      }
shadowlockextra = (("Lihzahrd Power Cell", 3), ("Golden Crate", 1), ("Goodie Bag", 1))
itemspershadowchest = 2
statues = ['Angel Statue', 'Anvil Statue', 'Armor Statue', 'Axe Statue', 'Bat Statue', 'Bird Statue', 'Bomb Statue',
           'Boomerang Statue', 'Boot Statue', 'Bow Statue', 'Bunny Statue', 'Chest Statue', 'Corrupt Statue',
           'Crab Statue', 'Cross Statue', 'Eyeball Statue', 'Fish Statue', 'Gargoyle Statue', 'Gloom Statue',
           'Goblin Statue', 'Hammer Statue', 'Heart Statue', 'Hornet Statue', 'Imp Statue', 'Jellyfish Statue',
           'King Statue', 'Mushroom Statue', 'Pickaxe Statue', 'Pillar Statue', 'Piranha Statue', 'Pot Statue',
           'Potion Statue', 'Queen Statue', 'Reaper Statue', 'Shield Statue', 'Skeleton Statue', 'Slime Statue',
           'Spear Statue', 'Star Statue', 'Sunflower Statue', 'Sword Statue', 'Tree Statue', 'Woman Statue',
           'Shark Statue']
for stat in statues:
    itemdata[stat] = 4

#data format: tile_id, minradius, maxradius, [tile_id for shell]
#shell is optional
#tile ids can be found in database.txt
#NEVER use a tile listed in "multitiles", bad stuff will happen

#"large planetoids"
data1 = [(23, 50, 150, 32),  #corgrass with vines
         (25, 20, 40, 23),#ebonstone
         (30, 50, 150),
         (40, 50, 150),
         (48, 5, 150),
         (51, 30, 50, 1),#cobweb planet
         (53, 50, 150),
         (54, 10, 50),
         (57, 50, 150),
         (59, 50, 150),
         (145, 30, 50, 147),
         (146, 30, 50, 147),
         (148, 30, 50, 147),
         (229, 30, 50, 225),#honey surrounded by hive
         (189, 30, 50, 196),#cloud surrounded by raincloud
         ]
#"small planetoids"
data2 = [(22, 2, 4, 1),
         (48, 5, 20, 1),
         (58, 10, 25, 56),  #hellstone with obsidian
         (63, 2, 3, 1),
         (64, 2, 3, 1),
         (65, 2, 3, 1),
         (66, 2, 3, 1),
         (67, 2, 3, 1),
         (68, 2, 3, 1),
         (70, 3, 10, 1),

         ]

#list of valuables for cave planetoids
#the more often an entry the higher its chance
valuable = [(1, 1, 1),
            (6, 6, 6),
            (6, 6, 6),
            (6, 6, 6),
            (6, 6, 6),
            (6, 6, 6),
            (7, 7, 7),
            (7, 7, 7),
            (7, 7, 7),
            (7, 7, 7),
            (7, 7, 7),
            (7, 7, 7),
            (7, 7, 7),
            (8, 8, 8),
            (9, 9, 9),
            (9, 9, 9),
            (30, 30, 30),
            (40, 40, 40),
            (40, 40, 40),
            (48, 48, 48),
            (48, 48, 48),
            (48, 48, 48),
            (51, 51, 51),
            (53, 53, 53),
            (56, 56, 56),
            (59, 59, 59),
            (253, 0, 255),  #water
            (253, 1, 255),  #lava
            (253, 0, 255),  #water
            (253, 1, 255),  #lava
            (253, 0, 255),  #water
            (253, 1, 255)  #lava
            ]

##mixing of dungeon walls with dungeon tiles
walls = [41, 43, 44]
center = [[-1, 20, 100], [-1, 20, 100], [-1, 20, 100]]
data3 = []  #dungeon
for tile in center:
    for wall in walls:
        #center[0], center[1], center[2], walls[0]
        #tile_Id, rmin, rmax, surround
        data3.append((tile + [wall]))
dungeon_map = {41 : 7,
               43 : 8,
               44 : 9}
