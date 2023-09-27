import pygame
import time
import random
from MinecraftWorldGen import generate_map
import math
from MinecraftConstants import *
pygame.font.init()
WIN = pygame.display.set_mode()
size = WIN.get_size()
sizeX, sizeY = size
FONT = pygame.font.Font(pack + "/Font.ttf", 30)




# ----------------------------------------------------------------------------------------- DRAW TEXT --------------------------------------------------------------------------------------

def draw_text(text, colour, x, y, updateScreen, Length):
    WIN.blit(FONT.render(text, 1, (colour)), (x, y))
    length2 = Length
    length2command = text, colour, x, y
    if updateScreen:
        pygame.display.flip()

TILEMAP_startingPoint_X = 0
TILEMAP_startingPoint_Y = 0
TILEMAP_startingPointScrollSpeed = 10
random.seed(12)
draw_text("Loading...", COLOURS_white, sizeX / 2, sizeY / 2, True, 1)

pygame.init()
pygame.display.set_caption("2D Minecraft")
clock = pygame.time.Clock()

# ----------------------------------------------------------------------------------------- TILEMAP GENERATE ------------------------------------------------------------------------------

TILEMAP_height = 100
TILEMAP_width = 50

SEED = 2567

TILEMAP_main = generate_map(TILEMAP_width, TILEMAP_height, SEED)
BLOCK_brush = 1

# ----------------------------------------------------------------------------------------- SETBLOCK --------------------------------------------------------------------------------------

def setblock(x, y, ID):
    try:
        _2 = TILEMAP_main
        _ = TILEMAP_main[math.floor(y)]
        _[math.floor(x)] = ID
        return tilemap_draw()
    except:
        return sur

# ----------------------------------------------------------------------------------------- TILEMAP DRAW ------------------------------------------------------------------------------------

def tilemap_draw():

    #    This tilemap is being done by rows, top down
    #    The "for VAR in NUM:" starts at 1
    #    The "LIST[num]" input starts at 0

    s = pygame.Surface((TILEMAP_height * BLOCK_size, TILEMAP_width * BLOCK_size))
    s.set_colorkey((0, 0, 0))
    global TILEMAP_startingPoint_Y, TILEMAP_startingPoint_X
    for INDEX_x in range(TILEMAP_height):
        for INDEX_y in range(TILEMAP_width):
            if not TILEMAP_main[INDEX_x][INDEX_y] == 0:
                if TILEMAP_main[INDEX_x][INDEX_y] < 999:

                    draw(pygame.transform.scale(TILEMAP_blockID[TILEMAP_main[INDEX_x][INDEX_y]], (BLOCK_size, BLOCK_size)),
                        int(INDEX_x * BLOCK_size),
                        int((INDEX_y) * BLOCK_size), s,
                        BLOCK_size, BLOCK_size, 0)
    return s

# ----------------------------------------------------------------------------------------- DRAW FUNCTION -----------------------------------------------------------------------------------

def draw(filename, x, y, s, resizeX, resizeY, rotation):

    # This code rotates the transformed image. It does NOT transform the rotated image. There IS a difference.
    if resizeX > 0 and resizeY > 0:
        s.blit(pygame.transform.rotate((pygame.transform.scale(filename, (resizeX, resizeY))), rotation), (x, y))
    else:
        s.blit(pygame.transform.rotate(filename, rotation), (x, y))

GAMEMODE = "Creative"

sur = tilemap_draw()

invCooldown = 0
invCooldownState = False
F3_Cooldown = 0
# ----------------------------------------------------------------------------------------- PIXELS FUNCTION ---------------------------------------------------------------------------------

def pixels_setup(pixelSZE):
    global PIXEL_sze
    PIXEL_sze = pixelSZE
    
    
# ----------------------------------------------------------------------------------------- INVENTORY SETUP ---------------------------------------------------------------------------------

sze = 5

pixels_setup(sze)
drawPos = 0
drawPosX, drawPosY = drawPos, drawPos

def pixels(AmountOfPixels):
    return AmountOfPixels * PIXEL_sze

INVENTORY_index = 0

def inventory_setup(CreativeOrSurvival, x, y):
    if CreativeOrSurvival == "Creative":
        pic = INVENTORY_ID[2]
        global SlotPos_CURRENT
        SlotPos_CURRENT = INVENTORY_ID_creative_Inventory_SlotPos

    else: pic = INVENTORY_ID[0] 

    drawPos = round((sizeX / 2) - ((pixels(pic.get_width())) / 2)), sizeY / 6 
    drawPosX, drawPosY = drawPos    

    WIN.blit(pygame.transform.scale(pic, (pixels(pic.get_width()), pixels(pic.get_height()))), drawPos)     

    for INVENTORY_index in range(len(INVENTORY_current) - 1):
        pic2 = TILEMAP_blockID[INVENTORY_current[INVENTORY_index + 1]]
        tposX, tposY = SlotPos_CURRENT[INVENTORY_index + 1]
        posX = (pixels(tposX) + drawPosX) - pixels(1)
        posY = (pixels(tposY) + drawPosY) - pixels(1)
        pic2 = pygame.transform.scale(pic2,
                (pixels(pic2.get_width()),
                    pixels(pic2.get_height())))
        if INVENTORY_current[INVENTORY_index + 1] != 0:
            WIN.blit(pic2, (posX, posY))
        if MOUSE_x > posX - sze and MOUSE_y > posY - sze and MOUSE_x < posX + pic2.get_width() + sze and MOUSE_y < posY + pic2.get_height() + sze:
            pic2 = INVENTORY_ID[12]
            WIN.blit(
                pygame.transform.scale(pic2,
                (pixels(pic2.get_width()),
                    pixels(pic2.get_height()))),
                (posX, posY))      
            
        

# ----------------------------------------------------------------------------------------- HOTBAR SETUP ------------------------------------------------------------------------------------

HOTBAR_pos = []
HOTBAR_posEnd = []
def inventory_hotbarSetup(x, y):

    pic = INVENTORY_ID[9]
    pic = pygame.transform.scale(pic, (pixels(pic.get_width()), pixels(pic.get_height())))
    WIN.blit(pic, (x, y))

    HOTBAR_pos = []
    HOTBAR_posEnd = []

    for INVENTORY_index in range(9):

        pic2 = TILEMAP_blockID[INVENTORY_current[33 + INVENTORY_index]]
        posX = x + 15 + (pic.get_width() / 9) * INVENTORY_index - INVENTORY_index
        posY = y + 15

        if pic2 != TILEMAP_blockID[0]:
            WIN.blit(
                pygame.transform.scale(pic2,                # resized image
                    (pixels(pic2.get_width()),                # resized image width
                    pixels(pic2.get_height()))),              # resized image height
                    (posX, posY))                           # blit X, blit Y
        if MOUSE_x > posX and MOUSE_y > posY and MOUSE_x < posX + pixels(pic2.get_width()) and MOUSE_y < posY + pixels(pic2.get_height()): # -------- WHERE IT CHANGES TILE SELECTED -----------
            pic2 = INVENTORY_ID[12]
            global HOTBAR_TileSelected
            HOTBAR_TileSelected = INVENTORY_index
            WIN.blit(
                pygame.transform.scale(pic2,
                (pixels(pic2.get_width()),
                    pixels(pic2.get_height()))),
                (posX, posY))
        else:
            HOTBAR_TileSelected = -1
            
        HOTBAR_pos.append((posX, posY))
        HOTBAR_posEnd.append((pic2.get_width() * sze, pic2.get_height() * sze))
        pic2 = INVENTORY_ID[11]

        if INVENTORY_index == HOTBAR_selectedSlot:
            WIN.blit(
                pygame.transform.scale(pic2,
                    (pic2.get_width() * sze,
                    pic2.get_height() * sze)),
                    (posX - 4 * sze, posY - 4 * sze))

inv = False

CONTROLS = []
scrolledYet = False

FPS_counter = 0
start_time = time.time()
# ----------------------------------------------------------------------------------------- Main Program Loop ------------------------------------------------------------------------------

done = False
while not done:

    keys = pygame.key.get_pressed()

    TIME_SINCE_START = (time.time() - start_time)

    # ----------------------------------------------------------------------------------------- Handles the FPS --------------------------------------------------------------------------------

    FPS_counter += 1

    # ----------------------------------------------------------------------------------------- Handles the scroll -----------------------------------------------------------------------------

    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            holding_scroll = True
            scroll = event.y
            if scroll == -1: scroll = 0.95
            if scroll == 1: scroll = 1.05

            BLOCK_size *= scroll
            BLOCK_size = abs(round(BLOCK_size))
            sur = tilemap_draw()

    # ----------------------------------------------------------------------------------------- Handles right and left click -------------------------------------------------------------------

    MOUSE_leftMiddleRight = pygame.mouse.get_pressed()
    MOUSE_left = MOUSE_leftMiddleRight[0]
    MOUSE_middle = MOUSE_leftMiddleRight[1]
    MOUSE_right = MOUSE_leftMiddleRight[2]

    # ----------------------------------------------------------------------------------------- Handles hotbar slot switching ------------------------------------------------------------------

    if keys[pygame.K_1]: HOTBAR_selectedSlot = 0
    elif keys[pygame.K_2]: HOTBAR_selectedSlot = 1
    elif keys[pygame.K_3]: HOTBAR_selectedSlot = 2
    elif keys[pygame.K_4]: HOTBAR_selectedSlot = 3
    elif keys[pygame.K_5]: HOTBAR_selectedSlot = 4
    elif keys[pygame.K_6]: HOTBAR_selectedSlot = 5
    elif keys[pygame.K_7]: HOTBAR_selectedSlot = 6
    elif keys[pygame.K_8]: HOTBAR_selectedSlot = 7
    elif keys[pygame.K_9]: HOTBAR_selectedSlot = 8

    if HOTBAR_TileSelected > -1: HOTBAR_selectedSlot = HOTBAR_TileSelected
    
    BLOCK_brush = INVENTORY_current[HOTBAR_selectedSlot + 33]

    # ----------------------------------------------------------------------------------------- SETBLOCK ON CLICK --------------------------------------------------------------------------------------
    
    if GAMEMODE == "Creative":
        if not (inv or HOTBAR_TileSelected > -1):
            if MOUSE_right:
                sur = setblock(MOUSE_coordinates_y, MOUSE_coordinates_x, BLOCK_brush)
            elif MOUSE_left:
                sur = setblock(MOUSE_coordinates_y, MOUSE_coordinates_x, 0)

    # ----------------------------------------------------------------------------------------- UNFINISHED USELESS CRAP: ⇣ ---------------------------------------------------------------------

    if keys[pygame.K_r]:
        sur = tilemap_draw()

    if keys[pygame.K_F3]:
        if F3_Cooldown < 1:
            F3_Cooldown = 20
            DEBUG[0] = not DEBUG[0]

    if length2 > 1:
        length2 -= 1
        draw_text(length2command, False)

    # ----------------------------------------------------------------------------------------- Close the window on escape ---------------------------------------------------------------------
    if keys[pygame.K_ESCAPE] and keys[pygame.K_F3]:
        done = True
        break
    if keys[pygame.K_e]:
        if invCooldown < 1:
            invCooldown = 20
            inv = not inv

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if invCooldown > -1:
        invCooldown = invCooldown - 1

    if F3_Cooldown > -1:
        F3_Cooldown = F3_Cooldown - 1

    # ----------------------------------------------------------------------------------------- F3 Text -----------------------------------------------------------------------------------------

    WIN.fill(COLOURS_skyBlue)
    WIN.blit(sur, (TILEMAP_startingPoint_X, TILEMAP_startingPoint_Y))
    MOUSE_pos = pygame.mouse.get_pos()
    MOUSE_x, MOUSE_y = MOUSE_pos
    MOUSE_coordinates_x, MOUSE_coordinates_y = (((MOUSE_x - TILEMAP_startingPoint_X) / BLOCK_size), ((MOUSE_y - TILEMAP_startingPoint_Y) / BLOCK_size))


    if DEBUG[0]:

        MOUSE_text = FONT.render(f"Mouse pos X: {MOUSE_x}, mouse pos Y: {MOUSE_y} pos.", 1, (255, 255, 255))
        WIN.blit(MOUSE_text, (F3_STARTPOS, F3_STARTPOS))

        MOUSE_text2 = FONT.render(f"Mouse coordinates X: {math.floor(MOUSE_coordinates_x)}, Mouse coordinates Y: {math.floor(MOUSE_coordinates_y)}", 1, (255, 255, 255))
        WIN.blit(MOUSE_text2, (F3_STARTPOS, F3_STARTPOS + 60))

        MOUSE_text3 = FONT.render(f"Selected tile: {TILEMAP_blockID_NAMES[BLOCK_brush]}, {BLOCK_size} block size, {GAMEMODE} Mode", 1, (255, 255, 255))
        WIN.blit(MOUSE_text3, (F3_STARTPOS, F3_STARTPOS + (60 * 2)))

        MOUSE_text4 = FONT.render(f"In inventory is {inv}, Size is {size}, size X and Y halved is {sizeX / 2} x, {sizeY / 2} y", 1, (255, 255, 255))
        WIN.blit(MOUSE_text4, (F3_STARTPOS, F3_STARTPOS + (60 * 3)))        

        MOUSE_text5 = FONT.render(f"Your cursor is on hotbar slot {HOTBAR_TileSelected}", 1, (255, 255, 255))
        WIN.blit(MOUSE_text5, (F3_STARTPOS, F3_STARTPOS + (60 * 4)))

        MOUSE_text6 = FONT.render(f"Time Since Start: {round(TIME_SINCE_START)}s", 1, (255, 255, 255))
        WIN.blit(MOUSE_text6, (F3_STARTPOS, F3_STARTPOS + (60 * 5)))

    # ----------------------------------------------------------------------------------------- This controls the camera scrolling -------------------------------------------------------------

    if keys[pygame.K_DOWN] or keys[pygame.K_s]: TILEMAP_startingPoint_Y = TILEMAP_startingPoint_Y - TILEMAP_startingPointScrollSpeed
    if keys[pygame.K_UP] or keys[pygame.K_w]: TILEMAP_startingPoint_Y = TILEMAP_startingPoint_Y + TILEMAP_startingPointScrollSpeed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: TILEMAP_startingPoint_X = TILEMAP_startingPoint_X + TILEMAP_startingPointScrollSpeed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: TILEMAP_startingPoint_X = TILEMAP_startingPoint_X - TILEMAP_startingPointScrollSpeed

    #WIN.blit(pygame.transform.scale(BLOCK_outline, (BLOCK_size, BLOCK_size)),
    #         MOUSE_coordinates_x * BLOCK_size - TILEMAP_startingPoint_X,
    #          MOUSE_coordinates_y * BLOCK_size - TILEMAP_startingPoint_Y)

    # ----------------------------------------------------------------------------------------- Go ahead and update the screen with what we've drawn. ------------------------------------------
    if inv: inventory_setup(GAMEMODE, 0, 0)
    else: inventory_hotbarSetup(sizeX / 2 - (INVENTORY_ID[9].get_width() * sze) / 2, sizeY - sizeY / 8)

    # ----------------------------------------------------------------------------------------- Limit to 60 frames per second ------------------------------------------------------------------
    pygame.display.flip()

    clock.tick(60)

# ----------------------------------------------------------------------------------------- Close the window and quit. ----------------------------------------------------------------------
pygame.quit()