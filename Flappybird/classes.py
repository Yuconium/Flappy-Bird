import pygame
from pygame.locals import (K_SPACE, K_UP, K_DOWN)
import mainwindow
import main
import random
import sys

class Bird:
	def __init__(self, x, y, surface, pipes):
		self.screen = surface
		self.posx = x
		self.posy = y
		self.startpos = (x,y)
		self.width = 30
		self.height = 30
		self.color = (50, 50, 50)

		self.down_velo = 2

		self.counter = 0
		self.dead = False

		self.gravity = True

		self.pipes = pipes

		self.image = pygame.image.load("bird.png").convert()

		self.image.set_colorkey((255, 255, 255))


	def draw(self):

							
		self.screen.blit(self.image, (self.posx, self.posy))


		self.rect = self.image.get_rect(center = (self.posx + 15, self.posy + 15))







	def fly(self, Taste):
		if Taste[K_UP] or Taste[K_SPACE]:
			self.gravity = False
			self.posy -= 5
		else:
			self.gravity = True

		if Taste[K_DOWN]:
			self.down_velo = 5
		else:
			self.down_velo = 2


		if self.gravity == True:
			self.posy += self.down_velo
	

	
	def collide(self):

		if self.rect.top <= 0:
			self.dead = True	
		elif self.rect.bottom >= 500:
			self.dead = True



		for pipe in self.pipes:
			if self.rect.colliderect(pipe.uprect):
				self.dead = True
			elif self.rect.colliderect(pipe.downrect):
				self.dead = True
			if 102 == pipe.downrect.x:

				self.counter += 1
				

	def begin(self):
		for pipe in self.pipes:
			pipe.posx = pipe.startx

		self.posx = self.startpos[0]
		self.posy = self.startpos[1]
		self.counter = 0

class Pipe:
	def __init__(self, posx, posy, screen):
		self.screen = screen
		
		self.startx = posx
		self.width = 50
		self.height = 500
		self.posx =  posx
		self.posy =  -random.randint(100, 500)
		self.color = (100, 100, 100)
			
		self.uppipeimage = pygame.image.load("uppipe.png").convert()

		self.downpipeimage = pygame.image.load("downpipe.png").convert()


		self.uppipeimage.set_colorkey((255, 255, 255))
		self.downpipeimage.set_colorkey((255, 255, 255))
		

	def draw(self):


		self.screen.blit(self.uppipeimage, (self.posx, self.posy))

		self.screen.blit(self.downpipeimage, (self.posx, self.posy + self.height + 100))



		self.uprect = self.uppipeimage.get_rect(center = (self.posx + 25, self.posy + 250))
		self.downrect =  self.downpipeimage.get_rect(center = (self.posx + 25, self.posy + self.height + 350))



	def move(self):
		self.posx -= 2

		if self.posx <= (0 - self.width):
			self.posx = 700 + self.width
			self.posy = -random.randint(100, 500)