from asyncio.windows_events import NULL
import pygame, random, sys
from pygame.locals import *
from src.utility import *
from src.ship import *
from src.explosion import *
def ingame(): 
    BACKSOUND.play(-1)
    global SCROLL
    run = True
    fps = 60
    level = 0
    
    #lost
    lost = False
    lost_count = 0

    #font
    main_font = pygame.font.SysFont("comicsans", 30)
    lost_font = pygame.font.SysFont("comicsans", 60)

    #enemy
    enemies = []
    enemy_vel = 3
    
    #player spwan
    player_vel = 8
    player = Player(20, 280)
    bullet_vel = 9

    #conditional highscore
    try:
        highscore = int(player.get_high_score())
    except:
        highscore = 0

    clock = pygame.time.Clock()

    def redraw_window():
        #draw text
        level_label = main_font.render(f"Level:{level}", 1, (255,0,0))
        score_label = main_font.render(f"Score: {player.score}", 1, (255,0,0))
        enemy_label = main_font.render(f"Enemy Live: {len(enemies[:])}", 1, (255,0,0))

        WINDOW.blit(score_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        WINDOW.blit(enemy_label, (WIDTH/2 - level_label.get_width(), 10))
        
        #ship
        for enemy in enemies:
            enemy.draw(WINDOW)

        player.draw(WINDOW)

        explosion_group.draw(WINDOW)

        #condition lost
        if lost:
            BACKSOUND.stop()
            DIE_SOUND.play()
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WINDOW.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 - lost_label.get_height()/2))

        pygame.display.update() 