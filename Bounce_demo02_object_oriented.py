import pygame
import random
import math

from pygame.locals import *

pygame.init()

win_wide = 800
win_high = 600
win_surf = pygame.display.set_mode((win_wide, win_high))
	
backgd_colour = (0, 0, 0)
circle_radius = 20

class Circle:

	def __init__(self):
		self.x = win_wide // 2
		self.y = win_high // 2
		a = random.randint(0, 359)
		self.dx = math.cos(math.radians(a))
		self.dy = math.sin(math.radians(a))
		self.r = random.randint(0, 191)
		self.g = random.randint(0, 191)
		self.b = random.randint(0, 191)

	def draw(self):
		pygame.draw.circle(win_surf, (self.r, self.g, self.b), (int(self.x), int(self.y)), circle_radius)
		
	
	def move(self):

		bounced = False

		if self.x + self.dx < 0:
			self.x = 0
			self.dx = -self.dx
			bounced = True
		elif self.x + self.dx > win_wide:
			self.x = win_wide
			self.dx = -self.dx
			bounced = True
		else:
			self.x = self.x + self.dx

		if self.y + self.dy < 0:
			self.y = 0
			self.dy = -self.dy
			bounced = True
		elif self.y + self.dy > win_high:
			self.y = win_high
			self.dy = -self.dy
			bounced = True
		else:
			self.y = self.y + self.dy

		if bounced:
			self.r = random.randint(0, 191)
			self.g = random.randint(0, 191)
			self.b = random.randint(0, 191)
		
	def fade(self):
		if self.r < 255:
			self.r += 1
		if self.g < 255:
			self.g += 1
		if self.b < 255:
			self.b += 1			
	
def main():

	circles = []

	for i in range(10):
		circles.append(Circle())
	
	closed_flag = False
	while not closed_flag:

		for event in pygame.event.get():
			if event.type == QUIT:
				closed_flag = True
		
		win_surf.fill(backgd_colour)

		for circle in circles:
			circle.move()
			circle.draw()
			circle.fade()
	
		pygame.display.update()
		pygame.time.wait(5)
				
main()