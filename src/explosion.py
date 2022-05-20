import pygame

#inheritance from sprite
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.img_list = []
		#list image file from 1 to 5
		for i in range(1, 6):
			img = pygame.image.load(f"assets/exp{i}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.img_list.append(img)
		self.index = 0
		self.image = self.img_list[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.count_delay = 0 
	
	#print the image
	def update(self):
		explosion_speed = 4
		self.count_delay +=1
		if self.count_delay >= self.count_delay >= explosion_speed and self.index < len(self.img_list) -1:
			self.count_delay = 0
			self.index += 1
			self.image = self.img_list[self.index]

		#remove image after print
		if self.index >= len(self.img_list) - 1 and self.count_delay >= explosion_speed:
			self.kill()
explosion_group = pygame.sprite.Group()