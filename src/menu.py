import pygame,sys
from src.utility import *
from src.game import *
from src.ship import *

def main_menu():
    MENU_SOUND.play(-1)
    global SCROLL
    run = True
    click = False
    #conditional highscore
    try:
        highscore = int(Player.get_high_score())
    except:
        highscore = 0

    while run:
        #draw scrolling background
        for i in range(0, TILES):
            WINDOW.blit(BACKGROUND, (i * BG_WIDTH + SCROLL, 0))
            BG_RECT.x = i * BG_WIDTH + SCROLL
            pygame.draw.rect(WINDOW, (255, 255, 255), BG_RECT, -1)
        #scroll background
        SCROLL -= 4
        #reset scroll
        if abs(SCROLL) > BG_WIDTH:
            SCROLL = 0
        #Returns the X and Y position mouse cursor
        mx, my = pygame.mouse.get_pos()
        title_font = pygame.font.SysFont("comicsans", 35)
        #rectangle
        button_1 = pygame.Rect(350, 300, 200, 50)
        button_2 = pygame.Rect(350, 360, 200, 50)
        button_3 = pygame.Rect(350, 420, 200, 50)
        #draw
        pygame.draw.rect(WINDOW, (255, 0, 0), button_1)
        pygame.draw.rect(WINDOW, (255, 0, 0), button_2)
        pygame.draw.rect(WINDOW, (255, 0, 0), button_3)
        #collide position mouse to the button
        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(WINDOW, (0, 0, 0), button_1)
            if click:
                MENU_SOUND.stop()
                BUTTON_SOUND.play()
                menu_play()

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(WINDOW, (0, 0, 0), button_2)
            if click:
                BUTTON_SOUND.play()
                menu_how()
        
        if button_3.collidepoint((mx, my)):
            pygame.draw.rect(WINDOW, (0, 0, 0), button_3)
            if click:
                BUTTON_SOUND.play()
                highscore = 0
                with open("src/highscore.txt", "w") as f:
                    f.write(str(highscore))
        #render font
        title_game = title_font.render("HALCYON", 1, (255,0,0))
        WINDOW.blit(title_game, (WIDTH/2 - title_game.get_width()/2, HEIGHT/2 - title_game.get_height()*2))

        title_highscore = title_font.render(f"HIGHSCORE : {highscore}", 1, (255,0,0))
        WINDOW.blit(title_highscore, (WIDTH/2 - title_highscore.get_width()/2, HEIGHT/3.2 + title_highscore.get_height()))

        title_button1 = title_font.render("Lets Begin!", 1, (255,255,255))
        WINDOW.blit(title_button1, (WIDTH/2 - title_button1.get_width()/2, HEIGHT/2))

        title_button2 = title_font.render("How To Play", 1, (255,255,255))
        WINDOW.blit(title_button2, (WIDTH/2 - title_button2.get_width()/2, HEIGHT/2 + title_button2.get_height()*1.2))

        title_button3 = title_font.render("Reset Score", 1, (255,255,255))
        WINDOW.blit(title_button3, (WIDTH/2 - title_button3.get_width()/2, HEIGHT/2 + title_button3.get_height()*2.5))
        #quit window and condition if button click 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()