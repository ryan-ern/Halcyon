import pygame
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
ENEMY1 = pygame.image.load('assets/enemy1.png')
ENEMY2 = pygame.image.load('assets/enemy2.png')
ENEMY3 = pygame.image.load('assets/enemy3.png')
PLAYER = pygame.image.load('assets/player.png')

#Window
WIDTH, HEIGHT = 900, 600
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Halcyon")
ICON = pygame.transform.scale(PLAYER, (50, 50))
pygame.display.set_icon(ICON)

#image bullet
PLAYER_BULLET = pygame.image.load('assets/pbullet.png')
ENEMY_BULLET1 = pygame.image.load('assets/ebullet1.png')
ENEMY_BULLET2 = pygame.image.load('assets/ebullet2.png')
ENEMY_BULLET3 = pygame.image.load('assets/ebullet3.png')

#how to play
HOWTOPLAY = pygame.image.load('assets/howtoplay.png')

#background
BACKGROUND = pygame.transform.scale(pygame.image.load('assets/BG.png'), (WIDTH, HEIGHT)) #scale background menyesuaikan WIDTH dan HEIGHT window
BG_WIDTH = BACKGROUND.get_width() #mengambil lebar background
BG_RECT = BACKGROUND.get_rect() #mengambil rectangle background
SCROLL = 0
TILES = math.ceil(WIDTH  / BG_WIDTH) + 1 # perhitungan besar background dan hasil perhitungan dibulatkan ke angka terdekat
