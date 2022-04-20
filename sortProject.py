# -*- coding: utf-8 -*-
import pygame, sys, time
import random
import math
from algorithms_sort import *

pygame.init()

global startTime 

startTime = time.time()

class DrawInfo:

	BLACK 	=   0,   0,   0
	WHITE 	= 255, 255, 255
	GREEN 	=   0, 255,   0
	RED 	= 255,   0,   0
	BLUE 	=   0,   0, 255
	YELLOW  = 255, 255, 0
	BACKGROUND_COLOR = WHITE

	GRADIENTS = [
		(143,188,143),
		(46,139,87),
		(47,79,79)
	]

	SIDE_PAD = 100
	TOP_PAD = 150

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.DISPLAYSURE = pygame.display.set_mode((width, height))
		pygame.display.set_caption('Sort')
		self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst
		self.min_val = 0
		self.max_val = max(lst)

		self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
		self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
		self.start_x = self.SIDE_PAD // 2

def generate_starting_list(n, min_val, max_val):
	lst = []
	with open('data.txt') as f:
		lines = f.readlines()

		for line in lines:
			lst.append(int(line))
	if not lst:
		for _ in range(n):
			val = random.randint(min_val, max_val)
			lst.append(val)

	return lst
# def refill():
# 	screen.fill((255, 255, 255))
# 	draw(draw_info, algorithms, speed)
# 	pygame.display.update()
# 	pygame.time.delay(10)

# def refill(draw_info):

# 	draw_info.DISPLAYSURE.fill((255, 255, 255))
# 	draw(draw_info, algorithms, speed)
# 	pygame.display.update()

def draw(draw_info, algorithms=None, speed=None):
	
	fnt = pygame.font.SysFont("comicsans", 30)
	fnt1 = pygame.font.SysFont("comicsans", 25)
	draw_info.DISPLAYSURE.fill(draw_info.BACKGROUND_COLOR)
	txt = fnt.render("Algorithms: {}".format(algorithms), 1, (0, 0, 0))
	# Position where text is placed
	draw_info.DISPLAYSURE.blit(txt, (10, 20))

	txt2 = fnt.render("Speed: {}".format(speed), 1,  (0, 0, 0))
	draw_info.DISPLAYSURE.blit(txt2, (10, 50))
	current = time.time()
	text3 = fnt1.render("Running Time(sec): " + str(int(current - startTime)), 1, (0, 0, 0))
	draw_info.DISPLAYSURE.blit(text3, (700, 20))

	# button
	draw_button(draw_info)

	draw_list(draw_info)
	pygame.draw.line(draw_info.DISPLAYSURE, (0, 0, 0), (0, 145), (900, 145), 4)

	pygame.display.update()

def main():
	clock = pygame.time.Clock()
	n = 100
	min_val = 1
	max_val = 101

	lst = generate_starting_list(n, min_val, max_val)
	draw_info = DrawInfo(900, 600, lst)
	# button
	bubble_button, insert_button, select_button, heap_button, quick_button, sync_button, slow_button, fast_button = draw_button(draw_info)

	print(lst)
	run = True
	sorting = False
	sorting_algorithm_generator = None
	algorithms = None
	set_speed = None
	speed = 0.2
	global startTime
	while run:
		clock.tick(50)
		if sorting:
			try:
				next(sorting_algorithm_generator)
			except StopIteration:
				sorting = False
		# draw(draw_info,algorithms, set_speed)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					# run = False
					quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					pos = pygame.mouse.get_pos()
					print(pos)
					print(slow_button.rect)
					if slow_button.rect.collidepoint(pos):
						print('ok')
						speed = 0.15
						set_speed = 'Slow'
						print(speed)

					if fast_button.rect.collidepoint(pos):
						speed = 0.01
						print(speed)
						set_speed = 'Fast'

					if bubble_button.rect.collidepoint(pos):
						algorithms = 'Bubble Sort'
						sorting = True
						sorting_algorithm_generator = bubble_sort(draw_info, speed)
						print('bubble_sort')

					if insert_button.rect.collidepoint(pos):
						algorithms = 'Insert Sort'
						sorting = True
						sorting_algorithm_generator = insertion_sort(draw_info, speed)
						print('insert_sort')

					if select_button.rect.collidepoint(pos):
						algorithms = 'Selection Sort'
						sorting = True
						sorting_algorithm_generator = selector_sort(draw_info, speed)
						print('selcet_sort')

					if heap_button.rect.collidepoint(pos):
						algorithms = 'Heap Sort'
						print('heap_sort')
						sorting = True
						sorting_algorithm_generator = heap_sort(draw_info, speed)

					if quick_button.rect.collidepoint(pos):
						algorithms = 'Quick Sort'
						sorting = True
						sorting_algorithm_generator = quick_sort(draw_info, speed)
						print('quick_sort')

					if sync_button.rect.collidepoint(pos):
						lst = generate_starting_list(n, min_val, max_val)
						draw_info.set_list(lst)
						print('Sync data')
						startTime = time.time()
			# elif event.key == pygame.K_SPACE and sorting == False:
			# 	pass
				# sorting = True
				# sorting_algorithm_generator = bubble_sort(draw_info)
		draw(draw_info, algorithms, set_speed)
	pygame.quit()

if __name__ == "__main__":
	main()