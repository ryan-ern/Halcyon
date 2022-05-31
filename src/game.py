import pygame, random #import library
import sys #import library
from pygame.locals import * 
from src.utility import * #import file
from src.ship import *
from src.explosion import *
def ingame(): 
    BACKSOUND.play(-1) #backsound diputar tidak ada batas (unlimited)
    global SCROLL #variabel global untuk mencegah unbound local error
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
        highscore = int(player._get_high_score())  # mencoba mendapatkan nilai int pada class
    except:
        highscore = 0 #jika tidak ada maka nilai variabel diisi 0

    try:
        highlevel = int(player._get_high_level())
    except:
        highlevel = 0

    clock = pygame.time.Clock() #variabel berisi class Clock

    def redraw_window():
        #draw text
        level_label = main_font.render(f"Level:{level}", 1, (255,0,0))
        score_label = main_font.render(f"Score: {player.score}", 1, (255,0,0))
        enemy_label = main_font.render(f"Enemy Live: {len(enemies[:])}", 1, (255,0,0))

        WINDOW.blit(score_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        WINDOW.blit(enemy_label, (WIDTH/2 - level_label.get_width(), 10))
        
        #draw enemy dengan bentuk perulangan yang disimpan ke dalam list enemies
        for enemy in enemies:
            enemy.draw(WINDOW)

        player.draw(WINDOW) # draw player

        explosion_group.draw(WINDOW) #draw explosion

        #condition lost
        if lost:
            BACKSOUND.stop()
            DIE_SOUND.play()
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WINDOW.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 - lost_label.get_height()/2))
        
        explosion_group.update()
        pygame.display.update()
        
    while run:
        clock.tick(fps)
        redraw_window()

        #highscore
        if highscore < player.score:
            highscore = player.score
        with open("src/highscore.txt", "w") as f:
            f.write(str(highscore))
        #highlevel
        if highlevel < level:
            highlevel = level
        with open("src/highlevel.txt", "w") as f:
            f.write(str(highlevel))

        #lost
        if player.health <= 0:
            lost = True
            lost_count += 1
        
        if lost:
            if lost_count > fps * 6: #kondisi jika lost_count > fps *6 fungsi ingame ini dihentikan dan kembali ke persiapan sebelum game dimulai
                run = False
            else:
                continue #jika tidak maka berlanjut terus
        
        #enemies
        if len(enemies) == 0: #kondisi jika panjang list enemies = 0
            level +=1
            wave_length = level * 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(910, 4000), random.randrange(80, HEIGHT-80), random.choice(["enemy1", "enemy2", "enemy3"]))
                enemies.append(enemy) # spawn enemy dengan random x,y dan memilih 3 enemy secara random
        
        #kondisi cooldown player shoot
        if level >= 5 and level < 10:
            player.COOLDOWN = 25
        if level >= 10 and level < 15:
            player.COOLDOWN = 15
        if level >= 15 and level < 20:
            player.COOLDOWN = 10 
        if level >= 20:
            player.COOLDOWN = 5

        #draw background bergerak
        for i in range(0, TILES):
            WINDOW.blit(BACKGROUND, (i * BG_WIDTH + SCROLL, 0))
            BG_RECT.x = i * BG_WIDTH + SCROLL
            pygame.draw.rect(WINDOW, (255, 255, 255), BG_RECT, -1)
        #scroll background
        SCROLL -= 2
        #reset scroll
        if abs(SCROLL) > BG_WIDTH:
            SCROLL = 0

        for user in pygame.event.get():
            if user.type == pygame.QUIT:
                run = False
                sys.exit()
        
        #key input
        key = pygame.key.get_pressed()
        keys=100
        if key[pygame.K_a] and player.x - player_vel > 0: #kiri
            player.x -= player_vel
        if key[pygame.K_d] and player.x + player_vel + keys < WIDTH:#kanan
            player.x += player_vel
        if key[pygame.K_w] and player.y - player_vel > keys/2: #atas
            player.y -= player_vel
        if key[pygame.K_s] and player.y + player_vel + keys < HEIGHT: #bawah
            player.y += player_vel
        if key[pygame.K_UP] or key[pygame.K_SPACE]:
            player.shoot()
        
        #cheat input
        cheat = pygame.key.get_pressed()
        if cheat[pygame.K_s] and cheat[pygame.K_p]: #skor bertanbah 50
            player.score +=10
        if cheat[pygame.K_h] and cheat[pygame.K_p]: #health max
            player.health =+100
        if cheat[pygame.K_u] and cheat[pygame.K_p]: #level bertambah
            level +=1
        if cheat[pygame.K_DELETE]:#kill all enemy
            player.score +=len(enemies[:])
            EXPLOSION_SOUND.play()
            enemies.clear()
        if cheat[pygame.K_s] and cheat[pygame.K_t]: # cooldown shoot
            player.COOLDOWN=5
        if cheat[pygame.K_d] and cheat[pygame.K_i]: # die
            player.health=0
        
        #enemy
        for enemy in enemies[:]:
            enemy.move(enemy_vel) #kecepatan enemy bergerak
            enemy.move_bullets(bullet_vel-3, player) #kecepatan gerak bullet enemy dan player sebagai objek tabrakan
            if random.randrange(0, 5*fps) == 1: #enemy menembak secara random, semakin kecil fps maka semakin banyak
                enemy.shoot()
            if collide(enemy, player): #kondisi enemy menbrak player
                player.health -= 15
                enemies.remove(enemy)
                EXPLOSION_SOUND.play()
                explosion = Explosion(enemy.x + enemy.get_width()/2, enemy.y + enemy.get_height()/2)
                explosion_group.add(explosion)
                player.score+=1
            if enemy.x + enemy.get_width() < 0: # kondisi enemy keluar dari layar
                enemies.remove(enemy)
                if player.score <=0:
                    player.health-=5
                elif player.score <=100:
                    player.score -=1
                else:
                    player.score -=2
                    player.health -=2.5
        
        #bullet player
        player.move_bullets(-bullet_vel, enemies) # -bullet vel digunakan agar koordinat x bernilai positif, objeknya list enemies
