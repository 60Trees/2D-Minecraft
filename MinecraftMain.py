import pygame, time, random, math
from MinecraftWorldGen import grow
from MinecraftConstants import *

# ----------------------------------------------------------------------------------------- Main Program Loop ------------------------------------------------------------------------------


CONTROLS = []
scrolledYet = False

FPS_counter = 0
start_time = time.time()

##inCameraBoundsX = False
##inCameraBoundsY = False

main_window = MainWindow()

isErr = False

done = False

gamemodeSwitcherCooldown = 20
while not done:

    keys = pygame.key.get_pressed()

    TIME_SINCE_START = (time.time() - start_time)

    # ----------------------------------------------------------------------------------------- Handles the FPS --------------------------------------------------------------------------------

    FPS_counter += 1

    # ----------------------------------------------------------------------------------------- Handles the scroll -----------------------------------------------------------------------------

    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            if keys[pygame.K_c]:
                holding_scroll = True
                scroll = event.y
                if scroll == -1: scroll = 0.95
                if scroll == 1: scroll = 1.05
                
                BLOCK_size *= scroll
                BLOCK_size = abs(round(BLOCK_size))
                sur = main_window.tilemap.tilemap_draw()
            else:
                HOTBAR_selectedSlot += event.y * -1
                if HOTBAR_selectedSlot < 0:
                    HOTBAR_selectedSlot = 8
                elif HOTBAR_selectedSlot > 8:
                    HOTBAR_selectedSlot = 0

    # ----------------------------------------------------------------------------------------- Handles right and left click -------------------------------------------------------------------

    MOUSE_leftMiddleRight = pygame.mouse.get_pressed()
    MOUSE_left = MOUSE_leftMiddleRight[0]
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
    
    brush = main_window.hotbar.inventory.INVENTORY_current[HOTBAR_selectedSlot + 33]

    # ----------------------------------------------------------------------------------------- SETBLOCK ON CLICK --------------------------------------------------------------------------------------
    
    #if main_window.tilemap.GAMEMODE == "Creative":
    
    if True:    
        if not (main_window.hotbar.inventory.inInv or HOTBAR_TileSelected > -1):
            if MOUSE_right:
                sur = main_window.tilemap.setblock(MOUSE_coordinates_y, MOUSE_coordinates_x, brush)
            elif MOUSE_left:
                sur = main_window.tilemap.setblock(MOUSE_coordinates_y, MOUSE_coordinates_x, 0)

    # ----------------------------------------------------------------------------------------- UNFINISHED USELESS CRAP: ⇣ ---------------------------------------------------------------------

    if keys[pygame.K_r]:
        sur = main_window.tilemap.tilemap_draw()
        
    if keys[pygame.K_g]:
        grow(6, 4, 4, 6, main_window.tilemap.TILEMAP_width, main_window.tilemap.TILEMAP_main)

    gamemodeSwitcherCooldown -= 1
    if keys[pygame.K_F3]:
        if keys[pygame.K_F4] and gamemodeSwitcherCooldown < 1:
            gamemodeSwitcherCooldown = 20
            main_window.hotbar.inventory.F3_Cooldown = 20
            if main_window.tilemap.GAMEMODE == "Survival": main_window.tilemap.GAMEMODE = "Creative"
            else: main_window.tilemap.GAMEMODE = "Survival"
        elif main_window.hotbar.inventory.F3_Cooldown < 1:
            main_window.hotbar.inventory.F3_Cooldown = 20
            DEBUG[0] = not DEBUG[0]

    if length2 > 1:
        length2 -= 1
        main_window.draw_text(length2command, False)

    
    main_window.cameraBound(sizeX < BLOCK_size * main_window.tilemap.TILEMAP_width, sizeY < BLOCK_size * main_window.tilemap.TILEMAP_height)
    
    # ----------------------------------------------------------------------------------------- Close the window on escape ---------------------------------------------------------------------
    if keys[pygame.K_ESCAPE] and keys[pygame.K_F3]:
        done = True
        break
    if keys[pygame.K_e]:
        if main_window.hotbar.inventory.invCooldown < 1:
            main_window.hotbar.inventory.invCooldown = 20
            main_window.hotbar.inventory.inInv = not main_window.hotbar.inventory.inInv

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if main_window.hotbar.inventory.invCooldown > -1:
        main_window.hotbar.inventory.invCooldown = main_window.hotbar.inventory.invCooldown - 1

    if main_window.hotbar.inventory.F3_Cooldown > -1:
        main_window.hotbar.inventory.F3_Cooldown = main_window.hotbar.inventory.F3_Cooldown - 1

    # ----------------------------------------------------------------------------------------- DRAW TEXT 2 -------------------------------------------------------------------------------

    def drawTxt(renderedFont, posX, posY):
        WIN.blit(renderedFont, (posX, posY))

    # ----------------------------------------------------------------------------------------- F3 Text -----------------------------------------------------------------------------------------

    WIN.fill(COLOURS_skyBlue)
    WIN.blit(main_window.tilemap.sur, (main_window.SCROLL_X, main_window.SCROLL_Y))
    MOUSE_pos = pygame.mouse.get_pos()
    MOUSE_x, MOUSE_y = MOUSE_pos
    MOUSE_coordinates_x, MOUSE_coordinates_y = (((MOUSE_x - main_window.SCROLL_X) / BLOCK_size), ((MOUSE_y - main_window.SCROLL_Y) / BLOCK_size))

    
    try:
        if DEBUG[0]:
            
            drawTxt(FONT.render(f"Mouse pos X: {MOUSE_x}, mouse pos Y: {MOUSE_y} pos.", 1, (COLOURS_white)), F3_STARTPOS, F3_STARTPOS)
            drawTxt(FONT.render(f"Mouse coordinates X: {math.floor(MOUSE_coordinates_x)}, Mouse coordinates Y: {math.floor(MOUSE_coordinates_y)}", 1, (COLOURS_white)), F3_STARTPOS, F3_STARTPOS + 60)
            drawTxt(FONT.render(f"Selected tile: {main_window.tilemap.blockID_names[brush]}, {BLOCK_size} block size, {main_window.tilemap.GAMEMODE} Mode", 1, (COLOURS_white)), F3_STARTPOS, F3_STARTPOS + (60 * 2))
            drawTxt(FONT.render(f"In inventory is {main_window.hotbar.inventory.inInv}, Size is {size}, size X and Y halved is {sizeX / 2} x, {sizeY / 2} y", 1, (COLOURS_white)), F3_STARTPOS, F3_STARTPOS + (60 * 3))
            drawTxt(FONT.render(f"Your cursor is on hotbar slot {HOTBAR_TileSelected}", 1, (COLOURS_white)), F3_STARTPOS, F3_STARTPOS + (60 * 4))
            drawTxt(FONT.render(f"Time Since Start: {round(TIME_SINCE_START)}s", 1, (COLOURS_white)), F3_STARTPOS, F3_STARTPOS + (60 * 5))
            drawTxt(FONT.render(f"Scroll X: {main_window.SCROLL_X}, Scroll Y: {main_window.SCROLL_Y}, Size X: {sizeX}, Size Y: {sizeY}", 1, (COLOURS_white)), F3_STARTPOS, F3_STARTPOS + (60 * 6))
            
    except: pass
    
    # CHAT_txt = FONT.render(f"Time Since Start: {round(TIME_SINCE_START)}s", 1, (COLOURS_white))
    # WIN.blit(CHAT_txt, (F3_STARTPOS, main_window.tilemap.CHAT_STARTPos - (60 * 1)))

    # ----------------------------------------------------------------------------------------- This controls the camera scrolling -------------------------------------------------------------

    if keys[pygame.K_DOWN] or keys[pygame.K_s]: main_window.SCROLL_Y = main_window.SCROLL_Y - main_window.SCROLLScrollSpeed
    if keys[pygame.K_UP] or keys[pygame.K_w]: main_window.SCROLL_Y = main_window.SCROLL_Y + main_window.SCROLLScrollSpeed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: main_window.SCROLL_X = main_window.SCROLL_X + main_window.SCROLLScrollSpeed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: main_window.SCROLL_X = main_window.SCROLL_X - main_window.SCROLLScrollSpeed

    if main_window.tilemap.timeSinceRefresh < 30:
        main_window.tilemap.timeSinceRefresh += 1
        try: drawTxt(FONT.render(f"Refreshed screen!", 1, (main_window.tilemap.timeSinceRefresh * 5, main_window.tilemap.timeSinceRefresh * 5, main_window.tilemap.timeSinceRefresh * 5)), F3_STARTPOS, sizeY - F3_STARTPOS * 2.5)
        except: pass
    # ----------------------------------------------------------------------------------------- Go ahead and update the screen with what we've drawn. ------------------------------------------
    if main_window.hotbar.inventory.inInv: main_window.hotbar.inventory.inventory_setup(main_window.tilemap.GAMEMODE, 0, 0)
    main_window.hotbar.hotbarSetup(sizeX / 2 - (main_window.hotbar.inventory.ID[9].get_width() * main_window.hotbar.inventory.sze) / 2, sizeY - sizeY / 8, HOTBAR_selectedSlot)

    # ----------------------------------------------------------------------------------------- Limit to 60 frames per second ------------------------------------------------------------------
    pygame.display.flip()
    main_window.clock.tick(60)

# ----------------------------------------------------------------------------------------- Close the window and quit. ----------------------------------------------------------------------
pygame.quit()