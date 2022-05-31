import pygame

#inheritance from sprite
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.img_list = []
		#perulangan load gambar dengan scale yang sama
		for i in range(1, 6): 
			img = pygame.image.load(f"assets/exp{i}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.img_list.append(img) # image ditambah pada urutan akhir
		self.index = 0
		self.image = self.img_list[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.count_delay = 0 
	
	#update gambar
	def update(self):
		explosion_speed = 4 #durasi explosion
		self.count_delay +=1 #delay gambar
		if self.count_delay >= self.count_delay >= explosion_speed and self.index < len(self.img_list) -1: #kondisi  count_delay >= explosion_speed dan index< panjang img_list -1
			self.count_delay = 0 #reset count_delay
			self.index += 1 #index bertambah 1
			self.image = self.img_list[self.index]  #membuat list sesuai urutan index

		#kondisi index >= panjang img_list -1  dan count_delay >= explosion speed maka image dihapus sesuai urutan pertama
		if self.index >= len(self.img_list) - 1 and self.count_delay >= explosion_speed:
			self.kill()
explosion_group = pygame.sprite.Group()
