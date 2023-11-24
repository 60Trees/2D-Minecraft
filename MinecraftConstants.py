import pygame, time, random, math
from MinecraftWorldGen import generate_map
keys = []

pack = "Assets"


#blockID = AssetID
#
#TILEMAP_blockID = blockID
#showID = TILEMAP_blockID

TILEMAP_blockID_itemStart = 32


MOUSE_breakCursor = [
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s0.png"),                      # ID 00 = Block cursor
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s1.png"),                      # ID 01 = Block destroy stage 1
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s2.png"),                      # ID 02 = Block destroy stage 2
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s3.png"),                      # ID 03 = Block destroy stage 3
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s4.png"),                      # ID 04 = Block destroy stage 4
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s5.png"),                      # ID 05 = Block destroy stage 5
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s6.png"),                      # ID 06 = Block destroy stage 6
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s7.png"),                      # ID 07 = Block destroy stage 7
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s8.png"),                      # ID 08 = Block destroy stage 8
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s9.png"),                      # ID 09 = Block destroy stage 9
    pygame.image.load(pack + "/Tiles/Block destroy stages/DESTROY_s10.png"),                     # ID 10 = Block destroy stage 10
]
F3_STARTPOS = 20
scrollOriginal = 0

pygame.display.set_icon(pygame.image.load(pack + "/Tiles/Tables/TABLE_crafting.png"))

DEBUG = [True, False, False]

COLOURS_black = (0, 0, 0)
COLOURS_white = (255, 255, 255)
COLOURS_grey = (100, 100, 100)
COLOURS_green = (0, 255, 0)
COLOURS_red = (255, 0, 0)
COLOURS_skyBlue = (28, 141, 227)

PLAYER_x = 10
PLAYER_y = 10

BLOCK_size = 64
BLOCK_sizeOriginal = 16

length2 = 0
length2command = "", COLOURS_white, 0, 0

HOTBAR_selectedSlot = 0
HOTBAR_TileSelected = -1

between = lambda val1, val2, valmain : valmain > val1 and valmain < val2
orbetween = lambda val1, val2, valmain : valmain > val1 or valmain < val2

pygame.font.init()
WIN = pygame.display.set_mode()
size = WIN.get_size()
sizeX, sizeY = size
FONT = pygame.font.Font(pack + "/Font.ttf", 30)

c_logo = pygame.image.load("Assets/Tiles/Tables/TABLE_crafting.png").convert()

MOUSE_x = 0
MOUSE_y = 0

class Inventory:  
    def __init__(self, tilemap):
            # these are some variables that are like globals to the class
            
        self.tilemap = tilemap
        
        self.ID = [
            pygame.image.load(pack + "/GUIs/INVENTORY_survival.png"),                                             # ID 00 = Survival inventory
            pygame.image.load(pack + "/GUIs/INVENTORY_yesno.png"),                                                # ID 01 = Yes / No option
            pygame.image.load(pack + "/GUIs/Creative/CREATIVE_inventory.png"),                                    # ID 02 = Creative inventory
            pygame.image.load(pack + "/GUIs/Creative/CREATIVE_invSearch.png"),                                    # ID 03 = Creative search
            pygame.image.load(pack + "/GUIs/Creative/CREATIVE_invTabs.png"),                                      # ID 04 = Creative tab menu 
            pygame.image.load(pack + "/GUIs/Creative/CREATIVE_tabsUP_SEL.png"),                                   # ID 05 = Tabs - Up Selected
            pygame.image.load(pack + "/GUIs/Creative/CREATIVE_tabsUP_DESEL.png"),                                 # ID 06 = Tabs - Up Deselected
            pygame.image.load(pack + "/GUIs/Creative/CREATIVE_tabsDOWN_SEL.png"),                                 # ID 07 = Tabs - Down Selected
            pygame.image.load(pack + "/GUIs/Creative/CREATIVE_tabsDOWN_DESEL.png"),                               # ID 08 = Tabs - Down Deselected
            pygame.image.load(pack + "/GUIs/INVENTORY_hotbar.png"),                                               # ID 09 = Hotbar
            pygame.image.load(pack + "/GUIs/INVENTORY_hotbarOffHand.png"),                                        # ID 10 = Hotbar offhand
            pygame.image.load(pack + "/GUIs/INVENTORY_hotbarSelected.png"),                                       # ID 11 = Hotbar selected
            pygame.image.load(pack + "/GUIs/INVENTORY_tileSelected.png"),                                         # ID 12 = Invenory tile selected
        ]
        self.ID_creative_Inventory_SlotPos = [
            (74,    7),                                                                                        # ID 00 = Player
            (55,    7),                                                                                        # ID 01 = Helmet
            (55,   34),                                                                                        # ID 02 = Chestplate
            (109,   7),                                                                                        # ID 03 = Leggings
            (109,  34),                                                                                        # ID 04 = Boots
            (36,   21),                                                                                        # ID 05 = Offhand
            (10,   55),                                                                                        # ID 06 = Slot num 1, 1
            (28,   55),                                                                                        # ID 07 = Slot num 1, 2
            (46,   55),                                                                                        # ID 08 = Slot num 1, 3
            (64,   55),                                                                                        # ID 09 = Slot num 1, 4
            (82,   55),                                                                                        # ID 10 = Slot num 1, 5
            (100,  55),                                                                                        # ID 11 = Slot num 1, 6
            (118,  55),                                                                                        # ID 12 = Slot num 1, 7
            (136,  55),                                                                                        # ID 13 = Slot num 1, 8
            (154,  55),                                                                                        # ID 14 = Slot num 1, 9
            (10,   73),                                                                                        # ID 15 = Slot num 2, 1
            (28,   73),                                                                                        # ID 16 = Slot num 2, 2
            (46,   73),                                                                                        # ID 17 = Slot num 2, 3
            (64,   73),                                                                                        # ID 18 = Slot num 2, 4
            (82,   73),                                                                                        # ID 19 = Slot num 2, 5
            (100,  73),                                                                                        # ID 20 = Slot num 2, 6
            (118,  73),                                                                                        # ID 21 = Slot num 2, 7
            (136,  73),                                                                                        # ID 22 = Slot num 2, 8
            (154,  73),                                                                                        # ID 23 = Slot num 2, 9
            (10,   91),                                                                                        # ID 24 = Slot num 3, 1
            (28,   91),                                                                                        # ID 25 = Slot num 3, 2
            (46,   91),                                                                                        # ID 26 = Slot num 3, 3
            (64,   91),                                                                                        # ID 27 = Slot num 3, 4
            (82,   91),                                                                                        # ID 28 = Slot num 3, 5
            (100,  91),                                                                                        # ID 29 = Slot num 3, 6
            (118,  91),                                                                                        # ID 30 = Slot num 3, 7
            (136,  91),                                                                                        # ID 31 = Slot num 3, 8
            (154,  91),                                                                                        # ID 32 = Slot num 3, 9
            (10,  113),                                                                                        # ID 33 = Hotbar slot num 1
            (28,  113),                                                                                        # ID 34 = Hotbar slot num 2
            (46,  113),                                                                                        # ID 35 = Hotbar slot num 3
            (64,  113),                                                                                        # ID 36 = Hotbar slot num 4
            (82,  113),                                                                                        # ID 37 = Hotbar slot num 5
            (100, 113),                                                                                        # ID 38 = Hotbar slot num 6
            (118, 113),                                                                                        # ID 39 = Hotbar slot num 7
            (136, 113),                                                                                        # ID 40 = Hotbar slot num 8
            (154, 113),                                                                                        # ID 41 = Hotbar slot num 9
        ]
        self.ID_survival_Inventory_SlotPos = [
            (27,    9),                                 # ID 00 = Player
            (9,     9),                                 # ID 01 = Helmet
            (9,    27),                                 # ID 02 = Chestplate
            (9,    45),                                 # ID 03 = Leggings
            (9,    63),                                 # ID 04 = Boots
            (78,   63),                                 # ID 05 = Offhand
            (9,    85),                                 # ID 06 = Slot num 1, 1
            (27,   85),                                 # ID 07 = Slot num 1, 2
            (45,   85),                                 # ID 08 = Slot num 1, 3
            (63,   85),                                 # ID 09 = Slot num 1, 4
            (81,   85),                                 # ID 10 = Slot num 1, 5
            (99,   85),                                 # ID 11 = Slot num 1, 6
            (117,  85),                                 # ID 12 = Slot num 1, 7
            (135,  85),                                 # ID 13 = Slot num 1, 8
            (153,  85),                                 # ID 14 = Slot num 1, 9
            (9,   103),                                 # ID 15 = Slot num 2, 1
            (27,  103),                                 # ID 16 = Slot num 2, 2
            (45,  103),                                 # ID 17 = Slot num 2, 3
            (63,  103),                                 # ID 18 = Slot num 2, 4
            (81,  103),                                 # ID 19 = Slot num 2, 5
            (99,  103),                                 # ID 20 = Slot num 2, 6
            (117, 103),                                 # ID 21 = Slot num 2, 7
            (135, 103),                                 # ID 22 = Slot num 2, 8
            (153, 103),                                 # ID 23 = Slot num 2, 9
            (9,   121),                                 # ID 24 = Slot num 3, 1
            (27,  121),                                 # ID 25 = Slot num 3, 2
            (45,  121),                                 # ID 26 = Slot num 3, 3
            (63,  121),                                 # ID 27 = Slot num 3, 4
            (81,  121),                                 # ID 28 = Slot num 3, 5
            (99,  121),                                 # ID 29 = Slot num 3, 6
            (117, 121),                                 # ID 30 = Slot num 3, 7
            (135, 121),                                 # ID 31 = Slot num 3, 8
            (153, 121),                                 # ID 32 = Slot num 3, 9
            (9,   143),                                 # ID 33 = Hotbar slot num 1
            (27,  143),                                 # ID 34 = Hotbar slot num 2
            (45,  143),                                 # ID 35 = Hotbar slot num 3
            (63,  143),                                 # ID 36 = Hotbar slot num 4
            (81,  143),                                 # ID 37 = Hotbar slot num 5
            (99,  143),                                 # ID 38 = Hotbar slot num 6
            (117, 143),                                 # ID 39 = Hotbar slot num 7
            (135, 143),                                 # ID 40 = Hotbar slot num 8
            (153, 143),                                 # ID 41 = Hotbar slot num 9
            ]
        self.INVENTORY_current = [
            00,                                                                                                # ID 00 = Player
            44,                                                                                                # ID 01 = Helmet
            45,                                                                                                # ID 02 = Chestplate
            46,                                                                                                # ID 03 = Leggings
            47,                                                                                                # ID 04 = Boots
            00,                                                                                                # ID 05 = Offhand
            1,                                                                                                # ID 06 = Slot num 1, 1
            00,                                                                                                # ID 07 = Slot num 1, 2
            00,                                                                                                # ID 08 = Slot num 1, 3
            00,                                                                                                # ID 09 = Slot num 1, 4
            00,                                                                                                # ID 10 = Slot num 1, 5
            00,                                                                                                # ID 11 = Slot num 1, 6
            00,                                                                                                # ID 12 = Slot num 1, 7
            00,                                                                                                # ID 13 = Slot num 1, 8
            00,                                                                                                # ID 14 = Slot num 1, 9
            00,                                                                                                # ID 15 = Slot num 2, 1
            1,                                                                                                # ID 16 = Slot num 2, 2
            00,                                                                                                # ID 17 = Slot num 2, 3
            00,                                                                                                # ID 18 = Slot num 2, 4
            00,                                                                                                # ID 19 = Slot num 2, 5
            00,                                                                                                # ID 20 = Slot num 2, 6
            00,                                                                                                # ID 21 = Slot num 2, 7
            00,                                                                                                # ID 22 = Slot num 2, 8
            00,                                                                                                # ID 23 = Slot num 2, 9
            00,                                                                                                # ID 24 = Slot num 3, 1
            00,                                                                                                # ID 25 = Slot num 3, 2
            1,                                                                                                # ID 26 = Slot num 3, 3
            00,                                                                                                # ID 27 = Slot num 3, 4
            00,                                                                                                # ID 28 = Slot num 3, 5
            00,                                                                                                # ID 29 = Slot num 3, 6
            00,                                                                                                # ID 30 = Slot num 3, 7
            00,                                                                                                # ID 31 = Slot num 3, 8
            00,                                                                                                # ID 32 = Slot num 3, 9
            1,                                                                                                # ID 33 = Hotbar slot num 1
            2,                                                                                                # ID 34 = Hotbar slot num 2
            3,                                                                                                # ID 35 = Hotbar slot num 3
            4,                                                                                                # ID 36 = Hotbar slot num 4
            00,                                                                                                # ID 37 = Hotbar slot num 5
            20,                                                                                                # ID 38 = Hotbar slot num 6
            21,                                                                                                # ID 39 = Hotbar slot num 7
            22,                                                                                                # ID 40 = Hotbar slot num 8
            26,                                                                                                # ID 41 = Hotbar slot num 9
        ]

        
        # ----------------------------------------------------------------------------------------- INVENTORY SETUP ---------------------------------------------------------------------------------
        self.inInv = False
        self.invCooldown = 0
        self.F3_Cooldown = 0
        self.sze = 5

        self.drawPos = 0
        self.drawPosX, self.drawPosY = self.drawPos, self.drawPos


        self.INVENTORY_index = 0

    def inventory_setup(self, CreativeOrSurvival, x, y):
        if CreativeOrSurvival == "Creative":
            self.pic = self.ID[2]
            self.SlotPos_CURRENT = self.ID_creative_Inventory_SlotPos
        else:
            self.pic = self.ID[0]
            self.SlotPos_CURRENT = self.ID_survival_Inventory_SlotPos
        
        self.drawPos = round((sizeX / 2) - ((self.pic.get_width() * self.sze) / 2)), sizeY / 6
        self.drawPosX, self.drawPosY = self.drawPos    

        WIN.blit(pygame.transform.scale(self.pic,
                                        (self.pic.get_width() * self.sze,
                                        self.pic.get_height() * self.sze)),
                self.drawPos)

        for INVENTORY_index in range(len(self.INVENTORY_current) - 1):
            pic2 = self.tilemap.blockID[self.INVENTORY_current[INVENTORY_index + 1]]
            if pic2 != self.tilemap.blockID[0]:             # If it's NOT air
                tposX, tposY = self.SlotPos_CURRENT[INVENTORY_index + 1]
                posX = tposX * self.sze + self.drawPosX - self.sze
                posY = tposY * self.sze + self.drawPosY - self.sze
                pic2 = pygame.transform.scale(pic2,
                        (pic2.get_width() * self.sze,
                            pic2.get_height() * self.sze))
                if self.INVENTORY_current[self.INVENTORY_index + 1] != 0:
                    WIN.blit(pic2, (posX, posY))
                if MOUSE_x > posX - self.sze and MOUSE_y > posY - self.sze and MOUSE_x < posX + pic2.get_width() + self.sze and MOUSE_y < posY + pic2.get_height() + self.sze:
                    pic2 = self.ID[12]
                    WIN.blit(
                        pygame.transform.scale(pic2,
                        (pic2.get_width() * self.sze,
                            pic2.get_height() * self.sze)),
                        (posX, posY))
class HotBar:
    def __init__(self, current_selection, tilemap):
        # these are some variables that are like globals to the class
        self.pos = []
        self.posEnd = []
        self.tilemap = tilemap
        self.inventory = Inventory(self.tilemap)
        
        self.invCooldown = 0
        self.invCooldownState = False
        self.F3_Cooldown = 0
    # ----------------------------------------------------------------------------------------- HOTBAR SETUP ------------------------------------------------------------------------------------
    def hotbarSetup(self, x, y, tileSel):
        
        pic = self.inventory.ID[9]
        pic = pygame.transform.scale(pic, (pic.get_width() * self.inventory.sze, pic.get_height() * self.inventory.sze))
        WIN.blit(pic, (x, y))
        
        self.posEnd = []
        blockID = self.tilemap.blockID

        for self.INVENTORY_index in range(9):
            
            pic2 = self.tilemap.blockID[self.inventory.INVENTORY_current[33 + self.INVENTORY_index]]
            posX = x + 15 + (pic.get_width() / 9) * self.INVENTORY_index - self.INVENTORY_index
            posY = y + 15

            if pic2 != blockID[0]: # If it's NOT air
                WIN.blit(
                    pygame.transform.scale(pic2,                    # resized image
                        (pic2.get_width() * self.inventory.sze,     # resized image width
                        pic2.get_height() * self.inventory.sze)),   # resized image height
                        (posX, posY))                               # blit X, blit Y

            if MOUSE_x > posX and MOUSE_y > posY and MOUSE_x < posX + pic2.get_width() * self.inventory.sze and MOUSE_y < posY + pic2.get_height() * self.inventory.sze: # -------- WHERE IT CHANGES TILE SELECTED -----------
                pic2 = self.ID[12]
                tileSel = self.INVENTORY_index
                print(tileSel)

                WIN.blit(
                    pygame.transform.scale(pic2,
                    (pic2.get_width() * self.inventory.sze,
                        pic2.get_height() * self.inventory.sze)),
                    (posX, posY))
            else:
                tileSel = -1
                
            self.pos.append((posX, posY))
            self.posEnd.append((pic2.get_width() * self.inventory.sze, pic2.get_height() * self.inventory.sze))
            pic2 = self.inventory.ID[11]
            if self.INVENTORY_index == tileSel:
                tileSel = self.INVENTORY_index
                WIN.blit(
                    pygame.transform.scale(pic2,
                        (pic2.get_width() * self.inventory.sze,
                        pic2.get_height() * self.inventory.sze)),
                        (posX - 4 * self.inventory.sze, posY - 4 * self.inventory.sze))
class TileMap:
    def __init__(self):
        
        self.blockID_names = [
            "Air",                                                                                             # ID 00 = Air
            "Grass block",                                                                                     # ID 01 = Grass block
            "Dirt block",                                                                                      # ID 02 = Dirt block
            "Stone block",                                                                                     # ID 03 = Stone block
            "Coal ore",                                                                                        # ID 04 = Coal ore
            "Copper ore",                                                                                      # ID 05 = Copper ore
            "Iron ore",                                                                                        # ID 06 = Iron ore
            "Gold ore",                                                                                        # ID 07 = Gold ore
            "Redstone ore",                                                                                    # ID 08 = Redstone ore 
            "Lapis ore",                                                                                       # ID 09 = Lapis ore
            "Diamond ore",                                                                                     # ID 10 = Diamond ore
            "Emerald ore",                                                                                     # ID 11 = Emerald ore
            "Deepslate",                                                                                       # ID 12 = Deepslate
            "Deepslate Coal ore",                                                                              # ID 13 = Deepslate Coal ore
            "Deepslate Copper ore",                                                                            # ID 14 = Deepslate Copper ore
            "Deepslate Iron ore",                                                                              # ID 15 = Deepslate Iron ore
            "Deepslate Gold ore",                                                                              # ID 16 = Deepslate Gold ore
            "Deepslate Lapis ore",                                                                             # ID 17 = Deepslate Lapis ore
            "Deepslate Diamond ore",                                                                           # ID 18 = Deepslate Diamond ore
            "Deepslate Emerald ore",                                                                           # ID 19 = Deepslate Emerald ore
            "Double tall grass bottom",                                                                        # ID 20 = Double tall grass bottom
            "Double tall grass top",                                                                           # ID 21 = Double tall grass top
            "Single tall grass",                                                                               # ID 22 = Single tall grass
            "Oak leaves",                                                                                      # ID 23 = Oak leaves
            "Oak log vertical",                                                                                # ID 24 = Oak log vertical
            "Oak log side",                                                                                    # ID 25 = Oak log side
            "Oak Sapling",                                                                                     # ID 26 = Oak Sapling
            "Dark oak Sapling",                                                                                # ID 27 = Dark oak Sapling
            "Spruce Sapling",                                                                                  # ID 28 = Spruce Sapling
            "Acacia Sapling",                                                                                  # ID 29 = Acacia Sapling
            "Birch Sapling",                                                                                   # ID 30 = Birch Sapling
            "Jungle Sapling",                                                                                  # ID 31 = Jungle Sapling
            "Coal",                                                                                            # ID 32 = Coal
            "Copper Ingot",                                                                                    # ID 33 = Copper Ingot
            "Iron ingot",                                                                                      # ID 34 = Iron ingot
            "Gold ingot",                                                                                      # ID 35 = Gold ingot
            "Redstone dust",                                                                                   # ID 36 = Redstone dust
            "Lapis lazuli",                                                                                    # ID 37 = Lapis lazuli
            "Diamond",                                                                                         # ID 38 = Diamond
            "Netherite ingot",                                                                                 # ID 39 = Netherite ingot
            "Raw copper",                                                                                      # ID 40 = Raw copper
            "Raw iron",                                                                                        # ID 41 = Raw iron
            "Raw gold",                                                                                        # ID 42 = Raw gold
            "Netherite scrap",                                                                                 # ID 43 = Netherite scrap
            "Leather helmet",                                                                                  # ID 44 = Leather helmet
            "Leather chesplate",                                                                               # ID 45 = Leather chesplate
            "Leather leggings",                                                                                # ID 46 = Leather leggings
            "Leather boots",                                                                                   # ID 47 = Leather boots
        ]
        self.blockID = [
            pygame.image.load(pack + "/Tiles/Air.png"),                                                        # ID 00 = Air
            pygame.image.load(pack + "/Tiles/grass_block.png"),                                                # ID 01 = Grass block
            pygame.image.load(pack + "/Tiles/dirt_block.png"),                                                 # ID 02 = Dirt block
            pygame.image.load(pack + "/Tiles/stone_block.png"),                                                # ID 03 = Stone block
            pygame.image.load(pack + "/Tiles/Ores/Stone/ORE_STONE_coal.png"),                                  # ID 04 = Coal ore
            pygame.image.load(pack + "/Tiles/Ores/Stone/ORE_STONE_copper.png"),                                # ID 05 = Copper ore
            pygame.image.load(pack + "/Tiles/Ores/Stone/ORE_STONE_iron.png"),                                  # ID 06 = Iron ore
            pygame.image.load(pack + "/Tiles/Ores/Stone/ORE_STONE_gold.png"),                                  # ID 07 = Gold ore
            pygame.image.load(pack + "/Tiles/Ores/Stone/ORE_STONE_redstone.png"),                              # ID 08 = Redstone ore
            pygame.image.load(pack + "/Tiles/Ores/Stone/ORE_STONE_lapis.png"),                                 # ID 09 = Lapis ore
            pygame.image.load(pack + "/Tiles/Ores/Stone/ORE_STONE_diamond.png"),                               # ID 10 = Diamond ore
            pygame.image.load(pack + "/Tiles/Ores/Stone/ORE_STONE_emerald.png"),                               # ID 11 = Emerald ore
            pygame.image.load(pack + "/Tiles/deepslate.png"),                                                  # ID 12 = Deepslate
            pygame.image.load(pack + "/Tiles/Ores/Deepslate/ORE_DEEPSLATE_coal.png"),                          # ID 13 = Deepslate Coal ore
            pygame.image.load(pack + "/Tiles/Ores/Deepslate/ORE_DEEPSLATE_copper.png"),                        # ID 14 = Deepslate Copper ore
            pygame.image.load(pack + "/Tiles/Ores/Deepslate/ORE_DEEPSLATE_iron.png"),                          # ID 15 = Deepslate Iron ore
            pygame.image.load(pack + "/Tiles/Ores/Deepslate/ORE_DEEPSLATE_gold.png"),                          # ID 16 = Deepslate Gold ore
            pygame.image.load(pack + "/Tiles/Ores/Deepslate/ORE_DEEPSLATE_lapis.png"),                         # ID 17 = Deepslate Lapis ore
            pygame.image.load(pack + "/Tiles/Ores/Deepslate/ORE_DEEPSLATE_diamond.png"),                       # ID 18 = Deepslate Diamond ore
            pygame.image.load(pack + "/Tiles/Ores/Deepslate/ORE_DEEPSLATE_emerald.png"),                       # ID 19 = Deepslate Emerald ore
            pygame.image.load(pack + "/Tiles/Decor/DECOR_tallGrassDouble_BOTTOM.png"),                         # ID 20 = Double tall grass bottom
            pygame.image.load(pack + "/Tiles/Decor/DECOR_tallGrassDouble_TOP.png"),                            # ID 21 = Double tall grass top
            pygame.image.load(pack + "/Tiles/Decor/DECOR_tallGrassSingle.png"),                                # ID 22 = Single tall grass
            pygame.image.load(pack + "/Tiles/Decor/Trees/Leaves/LEAVES_oak.png"),                              # ID 23 = Oak leaves
            pygame.image.load(pack + "/Tiles/Decor/Trees/Logs/Not stripped/LOG_oakVERTICAL.png"),              # ID 24 = Oak log vertical
            pygame.image.load(pack + "/Tiles/Decor/Trees/Logs/Not stripped/LOG_oakSIDE.png"),                  # ID 25 = Oak log side
            pygame.image.load(pack + "/Tiles/Decor/Trees/Saplings/SAPLINGS_oak.png"),                          # ID 26 = Oak Sapling
            pygame.image.load(pack + "/Tiles/Decor/Trees/Saplings/SAPLINGS_oakDark.png"),                      # ID 27 = Dark oak Sapling
            pygame.image.load(pack + "/Tiles/Decor/Trees/Saplings/SAPLINGS_spruce.png"),                       # ID 28 = Spruce Sapling
            pygame.image.load(pack + "/Tiles/Decor/Trees/Saplings/SAPLINGS_acacia.png"),                       # ID 29 = Acacia Sapling
            pygame.image.load(pack + "/Tiles/Decor/Trees/Saplings/SAPLINGS_birch.png"),                        # ID 30 = Birch Sapling
            pygame.image.load(pack + "/Tiles/Decor/Trees/Saplings/SAPLINGS_jungle.png"),                       # ID 31 = Jungle Sapling
            # ------------------------------------------------------------------------------------------------------------------------------------- ITEM START: 32 ----------------
            pygame.image.load(pack + "/Items/coal.png"),                                                       # ID 32 = Coal
            pygame.image.load(pack + "/Items/copper_ingot.png"),                                               # ID 33 = Copper Ingot
            pygame.image.load(pack + "/Items/iron_ingot.png"),                                                 # ID 34 = Iron ingot
            pygame.image.load(pack + "/Items/gold_ingot.png"),                                                 # ID 35 = Gold ingot
            pygame.image.load(pack + "/Items/redstone.png"),                                                   # ID 36 = Redstone dust
            pygame.image.load(pack + "/Items/lapis_lazuli.png"),                                               # ID 37 = Lapis lazuli
            pygame.image.load(pack + "/Items/diamond.png"),                                                    # ID 38 = Diamond
            pygame.image.load(pack + "/Items/netherite_ingot.png"),                                            # ID 39 = Netherite ingot
            pygame.image.load(pack + "/Items/raw_copper.png"),                                                 # ID 40 = Raw copper
            pygame.image.load(pack + "/Items/raw_iron.png"),                                                   # ID 41 = Raw iron
            pygame.image.load(pack + "/Items/raw_gold.png"),                                                   # ID 42 = Raw gold
            pygame.image.load(pack + "/Items/netherite_scrap.png"),                                            # ID 43 = Netherite scrap
            pygame.image.load(pack + "/Items/leather_helmet.png"),                                             # ID 44 = Leather helmet
            pygame.image.load(pack + "/Items/leather_chestplate.png"),                                         # ID 45 = Leather chesplate
            pygame.image.load(pack + "/Items/leather_leggings.png"),                                           # ID 46 = Leather leggings
            pygame.image.load(pack + "/Items/leather_boots.png"),                                              # ID 47 = Leather boots
            pygame.image.load(pack + "/Items/shield.png"),                                                     # ID 48 = Shield
        ]
        
        self.TILEMAP_height = 100
        self.TILEMAP_width = 50
        
        self.timeSinceRefresh = 1001
        
        self.SEED = 5555
        
        self.MAKE_MAP()

        self.brush = 1

        self.CHAT_STARTPos = self.TILEMAP_width - round(self.TILEMAP_width / 4)
        
        self.GAMEMODE = "Survival"

        self.sur = self.tilemap_draw()
    def MAKE_MAP(self):
        #global TILEMAP_main
        self.TILEMAP_main = generate_map(self.TILEMAP_width, self.TILEMAP_height, self.SEED)
        errorCount = self.TILEMAP_main


    # ----------------------------------------------------------------------------------------- SETBLOCK --------------------------------------------------------------------------------------
    def setblock(self, x, y, ID):
        try:
            _2 = self.TILEMAP_main
            _ = self.TILEMAP_main[math.floor(y)]
            _[math.floor(x)] = ID
            return self.tilemap_draw()
        except:
            return self.sur

    # ----------------------------------------------------------------------------------------- TILEMAP DRAW ------------------------------------------------------------------------------------

    def tilemap_draw(self):

        #    This tilemap is being done by rows, top down
        #    The "for VAR in NUM:" starts at 1
        #    The "LIST[num]" input starts at 0

        s = pygame.Surface((self.TILEMAP_height * BLOCK_size, self.TILEMAP_width * BLOCK_size))
        s.set_colorkey((0, 0, 0))
        global SCROLL_Y, SCROLL_X
        for INDEX_x in range(self.TILEMAP_height):
            for INDEX_y in range(self.TILEMAP_width):
                if not self.TILEMAP_main[INDEX_x][INDEX_y] == 0:
                    if self.TILEMAP_main[INDEX_x][INDEX_y] < 999:

                        self.draw(pygame.transform.scale(self.blockID[self.TILEMAP_main[INDEX_x][INDEX_y]], (BLOCK_size, BLOCK_size)),
                            int(INDEX_x * BLOCK_size),
                            int((INDEX_y) * BLOCK_size), s,
                            BLOCK_size, BLOCK_size, 0)
        
        self.timeSinceRefresh = 1
        
        return s


    # ----------------------------------------------------------------------------------------- DRAW FUNCTION -----------------------------------------------------------------------------------

    def draw(self, filename, x, y, s, resizeX, resizeY, rotation):

        # This code rotates the transformed image. It does NOT transform the rotated image. There IS a difference.
        if resizeX > 0 and resizeY > 0:
            s.blit(pygame.transform.rotate((pygame.transform.scale(filename, (resizeX, resizeY))), rotation), (x, y))
        else:
            s.blit(pygame.transform.rotate(filename, rotation), (x, y))
class MainWindow:
    
    # this happens when you make the class  
    def __init__(self):
        # these are some variables that are like globals to the class
        self.SCROLL_X = 0
        self.SCROLL_Y = 0
        self.SCROLLScrollSpeed = 10
        random.seed(12)
        self.draw_text("Loading...", COLOURS_white, sizeX / 2, sizeY / 2, True, 1)

        pygame.init()
        pygame.display.set_caption("2D Minecraft")
        self.clock = pygame.time.Clock()
        
        self.tilemap = TileMap()
        
        self.hotbar = HotBar(0, self.tilemap)

    # ----------------------------------------------------------------------------------------- DRAW TEXT --------------------------------------------------------------------------------------
    def draw_text(self, text, colour, x, y, updateScreen, Length):
        WIN.blit(FONT.render(text, 1, (colour)), (x, y))
        length2 = Length
        length2command = text, colour, x, y
        if updateScreen:
            pygame.display.flip()

    # ----------------------------------------------------------------------------------------- CAMERA BOUNDARIES ------------------------------------------------------------------------------

    def cameraBound(self, boundsX, boundsY):
        """ Camera bounds:
        global sizeX
        global inCameraBoundsX
        global inCameraBoundsY
        global sizeY
        global SCROLL_X
        global SCROLL_Y
        global BLOCK_size
        global TILEMAP_width
        global TILEMAP_height
        
        if SCROLL_X > 0:
            inCameraBoundsX = True
            if not keys[pygame.K_m]:
                SCROLL_X = 0
        elif TILEMAP_width * BLOCK_size < SCROLL_X:
            if not keys[pygame.K_m]:
                SCROLL_X = 0
            inCameraBoundsX = True
        else:
            inCameraBoundsX = False
        
        if SCROLL_Y > 0:
            if not keys[pygame.K_m]:
                SCROLL_Y = 0
            inCameraBoundsY = False
        else:
            inCameraBoundsY = True
        
        if boundsY:
            pass 
        
        
        if not keys[pygame.K_m]:
            # Assuming that map_width and map_height are the width and height of your tilemap
            MAP_width = BLOCK_size * self.tilemap.TILEMAP_width
            MAP_height = BLOCK_size * self.tilemap.TILEMAP_height

            # Left boundary
            if self.SCROLL_X > 0:
                self.SCROLL_X = 0

            # Right boundary
            if self.SCROLL_X < -1 * (MAP_width + sizeX / BLOCK_size):
                self.SCROLL_X = -1 * (MAP_width + sizeX / BLOCK_size)
                
            # Top boundary
            #if SCROLL_Y > 0:
            #    SCROLL_Y = 0

            # Bottom boundary
            #if SCROLL_Y > -1 * (MAP_height + sizeY):
            #    SCROLL_Y = -1 * (MAP_height + sizeY)"""