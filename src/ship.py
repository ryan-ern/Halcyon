from src.utility import *
from src.explosion import *

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) !=None

class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self,window):
        window.blit(self.img, (self.x, self.y))

    def move(self,vel):
        self.x -= vel

    def off_screen(self, WIDTH):
        return not(self.x <= WIDTH and self.x >=0)

    def collision(self, obj):
        return collide(self, obj)

#parent class
class Ship:
    COOLDOWN=30
    def __init__(self, x, y, health=100, score=0):
        self.x = x
        self.y = y
        self.health = health
        self.score = score
        self.ship_img = None
        self.bullet_img = None
        self.bullet = []
        self.cooldown_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for bulet in self.bullet:
            bulet.draw(window)
    
    def cooldown(self):
        if self.cooldown_counter >= self.COOLDOWN:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter +=1
    
    def move_bullets(self, vel, obj):
        self.cooldown()
        for bulet in self.bullet:
            bulet.move(vel)
            if bulet.off_screen(WIDTH):
                self.bullet.remove(bulet)
            elif bulet.collision(obj):
                ESHOOT_SOUND.play()
                obj.health -= 10
                self.bullet.remove(bulet)

    def shoot(self):
        if self.cooldown_counter == 0:
            bullet = Bullet(self.x, self.y, self.bullet_img)
            self.bullet.append(bullet)
            self.cooldown_counter = 1
            SHOOT_SOUND.play()
    
    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

#inheritance class
class Player(Ship):
    def __init__(self, x, y, health=100, score=0):
        super().__init__(x, y, health, score)
        self.ship_img = PLAYER
        self.bullet_img = PLAYER_BULLET
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_bullets(self, vel, objs):
        self.cooldown()
        for bulet in self.bullet:
            bulet.move(vel)
            if bulet.off_screen(WIDTH):
                self.bullet.remove(bulet)
            for obj in objs:
                if bulet.collision(obj):
                    objs.remove(obj)
                    self.score +=1
                    EXPLOSION_SOUND.play()
                    explosion = Explosion(obj.x + obj.get_width()/2, obj.y + obj.get_height()/2)
                    explosion_group.add(explosion)
                    if bulet in self.bullet:
                        self.bullet.remove(bulet)
    
    def hp_player_bar(self, window, width_hp=80, height_hp=8):
        self.width_hp = width_hp
        self.height_hp = height_hp
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height(), self.width_hp, self.height_hp))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height(), self.width_hp * (self.health/self.max_health), self.height_hp))

    def draw(self, window):
        super().draw(window)
        self.hp_player_bar(window)

    def get_high_score():
        with open("src/highscore.txt", "r") as f:
            return f.read()
            
#inheritance class
class Enemy(Ship):
    ENEMY_TYPE= {
                "enemy1" : (ENEMY1, ENEMY_BULLET1),
                "enemy2" : (ENEMY2, ENEMY_BULLET2),
                "enemy3" : (ENEMY3, ENEMY_BULLET3)
    }

    def __init__(self, x, y, type_enemy,health=100):
        super().__init__(x, y, health)
        self.ship_img, self.bullet_img = self.ENEMY_TYPE[type_enemy]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.x -= vel

    def shoot(self):
        if self.cooldown_counter == 0:
            bulet = Bullet(self.x, self.y, self.bullet_img)
            self.bullet.append(bulet)
            self.cooldown_counter = 1  
