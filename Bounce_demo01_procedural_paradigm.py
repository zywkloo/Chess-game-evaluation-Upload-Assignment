import pygame
import random
import math

from pygame.locals import *

pygame.init()

win_wide = 800
win_high = 600
win_surf = pygame.display.set_mode((win_wide, win_high))
	
backgd_colour = (0, 0, 0)
circle_colour = (255, 255, 255)

circle_radius = 20

def main():

	circles = []

	for i in range(4):
	
		x = 400
		y = 300
		a = random.randint(0, 359)
		dx = math.cos(math.radians(a))
		dy = math.sin(math.radians(a))
		
		circles.append([x, y, dx, dy])
	
	closed_flag = False
	while not closed_flag:

		for event in pygame.event.get():
			if event.type == QUIT:
				closed_flag = True

		for i in range(len(circles)):
			
			if circles[i][0] + circles[i][2] < 0:
				circles[i][0] = 0
				circles[i][2] = -circles[i][2]
			elif circles[i][0] + circles[i][2] > win_wide:
				circles[i][0] = win_wide
				circles[i][2] = -circles[i][2]
			else:
				circles[i][0] = circles[i][0] + circles[i][2]

			if circles[i][1] + circles[i][3] < 0:
				circles[i][1] = 0
				circles[i][3] = -circles[i][3]
			elif circles[i][1] + circles[i][3] > win_high:
				circles[i][1] = win_high
				circles[i][3] = -circles[i][3]
			else:
				circles[i][1] = circles[i][1] + circles[i][3]

		
		win_surf.fill(backgd_colour)

		for i in range(len(circles)):
		
			pygame.draw.circle(win_surf, circle_colour, (int(circles[i][0]), int(circles[i][1])), circle_radius) 
	
		pygame.display.update()
		pygame.time.wait(5)
	
				
main()