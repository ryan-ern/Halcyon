import pygame, os
import math

#font
pygame.font.init()

#Backsound
pygame.mixer.init()
BACKSOUND = pygame.mixer.Sound('assets/sound/BS.mp3')
SHOOT_SOUND = pygame.mixer.Sound('assets/sound/BS-shoot.mp3')
EXPLOSION_SOUND = pygame.mixer.Sound('assets/sound/BS-explo.mp3')
MENU_SOUND = pygame.mixer.Sound('assets/sound/BS-menu.mp3')
BUTTON_SOUND = pygame.mixer.Sound('assets/sound/BS-tombol.mp3')
DIE_SOUND = pygame.mixer.Sound('assets/sound/BS-die.mp3')
ESHOOT_SOUND = pygame.mixer.Sound('assets/sound/BS-eshoot.mp3')

#Image ship
ENEMY1 = pygame.image.load(os.path.join("assets", "enemy1.png"))
ENEMY2 = pygame.image.load(os.path.join("assets", "enemy2.png"))
ENEMY3 = pygame.image.load(os.path.join("assets", "enemy3.png"))
PLAYER = pygame.image.load(os.path.join("assets", "player.png"))

#Window
WIDTH, HEIGHT = 900, 600
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Halcyon")
ICON = pygame.transform.scale(PLAYER, (50, 50))
pygame.display.set_icon(ICON)