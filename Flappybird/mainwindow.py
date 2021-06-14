import pygame
from pygame.locals import (K_SPACE, K_UP)
import classes
import random

class Screen:
	def __init__(self, width, height):


		self.screen_width = width
		self.screen_height = height
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
		self.state = "main"
		self.instance_all()

		


		self.font = pygame.font.SysFont("comicsansms", 30)


		self.clock = pygame.time.Clock()


		self.run = True


	def mainloop(self):
		while self.run == True:
			if self.state == "main":
				self.mainstate()
			if self.state == "dead":
				self.deadstate()
			self.clock.tick(60)

		pygame.quit()



	def instance_all(self):
		
		self.pipe = classes.Pipe(self.screen_width + 200, 100, self.screen)
		self.pipe2 = classes.Pipe(self.screen_width + 400, 100, self.screen)
		self.pipe3 = classes.Pipe(self.screen_width + 600, 100, self.screen)
		self.pipe4 = classes.Pipe(self.screen_width + 800, 100, self.screen)

		self.all_pipes = [ self.pipe, self.pipe2, self.pipe3, self.pipe4]
		

		self.bird = classes.Bird((self.screen_width/6) - 15, (self.screen_height/2) - 15, self.screen, self.all_pipes)
		self.all_sprites = [self.bird, self.pipe, self.pipe2, self.pipe3, self.pipe4]
		

		



	def handle_sprites(self):
		for sprite in self.all_sprites:
			sprite.draw()

		for pipe in self.all_pipes:
			pipe.move()
		self.bird.fly(self.Input)
		self.bird.collide()


		if self.bird.dead == True:
			self.state = "dead"

		self.text = self.font.render(str(self.bird.counter), True, (0, 0, 0))
		self.screen.blit(self.text, (self.bird.posx - 50, self.bird.posy - 10))
        



		

	def mainstate(self):
		
		self.events = pygame.event.get()
		for event in self.events:
			if event.type == pygame.QUIT:
				self.run = False

		self.screen.fill((10, 150, 100))
		self.Input = pygame.key.get_pressed()


		self.handle_sprites()

		
		pygame.display.flip()

	def deadstate(self):

		self.events = pygame.event.get()
		for event in self.events:
			if event.type == pygame.QUIT:
				self.run = False

		self.screen.fill((0, 150, 150))
		self.Input = pygame.key.get_pressed()
		if self.Input[K_SPACE]:
			self.state = "main"

			self.bird.dead = False
			self.bird.begin()

		self.text = self.font.render(str(self.bird.counter), True, (0, 0, 0))
		self.screen.blit(self.text, (self.screen_width / 2 - self.text.get_width()/ 2, self.screen_height / 2 - self.text.get_height()/ 2))
		
		pygame.display.flip()