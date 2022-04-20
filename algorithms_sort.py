import pygame, sys
import time 
import button

def draw_button(draw_info):
	bubble_img = pygame.image.load('bubble.png')
	bubble_button = button.Button(300, 40, bubble_img, 1)

	insert_img = pygame.image.load('insert.png')
	insert_button = button.Button(370, 40, insert_img, 1)

	select_img = pygame.image.load('selection.png')
	select_button = button.Button(440, 40, select_img, 1)

	heap_img = pygame.image.load('heap.png')
	heap_button = button.Button(510, 40, heap_img, 1)

	quick_img = pygame.image.load('quick.png')
	quick_button = button.Button(580, 40, quick_img, 1)

	sync_img = pygame.image.load('icons8-synchronize-48.png')
	sync_button = button.Button(440, 100, sync_img, 0.8)

	slow_img = pygame.image.load('icons8-left-48.png')
	slow_button = button.Button(370, 100, slow_img, 0.8)

	fast_img = pygame.image.load('icons8-right-48.png')
	fast_button = button.Button(510, 98, fast_img, 0.8)

	bubble_button.draw(draw_info.DISPLAYSURE)
	insert_button.draw(draw_info.DISPLAYSURE)
	select_button.draw(draw_info.DISPLAYSURE)
	heap_button.draw(draw_info.DISPLAYSURE)
	quick_button.draw(draw_info.DISPLAYSURE)
	sync_button.draw(draw_info.DISPLAYSURE)
	slow_button.draw(draw_info.DISPLAYSURE)
	fast_button.draw(draw_info.DISPLAYSURE)

	return bubble_button, insert_button, select_button, heap_button, quick_button, sync_button, slow_button, fast_button

def draw_list(draw_info, color_positions={}, clear_bg=False):
	lst = draw_info.lst

	if clear_bg:
		clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, 
						draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
		pygame.draw.rect(draw_info.DISPLAYSURE, draw_info.BACKGROUND_COLOR, clear_rect)

	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width
		y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height + 1

		color = draw_info.GRADIENTS[i % 3]

		if i in color_positions:
			color = color_positions[i] 

		pygame.draw.rect(draw_info.DISPLAYSURE, color, (x, y, draw_info.block_width, draw_info.height))

	if clear_bg:
		pygame.display.update()


def bubble_sort(draw_info, speed=None):
	lst = draw_info.lst

	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j]
			num2 = lst[j + 1]

			if (num1 > num2):
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
		time.sleep(speed)
		yield True

	return lst

def insertion_sort(draw_info, speed=None):
	lst = draw_info.lst

	for i in range(1, len(lst)):
		current = lst[i]

		while i > 0 and lst[i - 1] > current:
			lst[i] = lst[i - 1]
			i = i - 1
			lst[i] = current
			draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
		time.sleep(speed)
		yield True
	return lst

def selector_sort(draw_info, speed=None):
	lst = draw_info.lst

	for i in range(1, len(lst)):
		min_idx = i-1
		for j in range(i, len(lst)):
			if lst[min_idx] > lst[j]:
				min_idx = j 
			draw_list(draw_info,{min_idx: draw_info.GREEN, j: draw_info.RED}, True)
		time.sleep(speed)
		yield True
		lst[i-1], lst[min_idx] = lst[min_idx], lst[i-1]
		# draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
		
	return lst

def heapify(arr, n, i, draw_info):
	draw_list(draw_info,{i: draw_info.RED, n: draw_info.GREEN}, True)
	largest = i  # Initialize largest as root
	l = 2 * i + 1     # left = 2*i + 1
	r = 2 * i + 2     # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and arr[largest] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]  # swap
		# refill(draw_info)
		pygame.display.update()
	# Heapify the root.
		heapify(arr, n, largest, draw_info)
		# refill(draw_info)
		pygame.display.update()

def heap_sort(draw_info, speed=None):
	lst = draw_info.lst

	n = len(lst)
    # Build a maxheap.
	for i in range(n//2 - 1, -1, -1):
		heapify(lst, n, i, draw_info)
		time.sleep(speed)
    # One by one extract elements
	for i in range(n-1, 0, -1):
		lst[i], lst[0] = lst[0], lst[i]  # swap
		# refill(draw_info)
		pygame.display.update()
		heapify(lst, i, 0, draw_info)
		time.sleep(speed)
	yield True
	return lst

def partition(start, end, array, draw_info):

	# Initializing pivot's index to start
	pivot_index = start
	pivot = array[pivot_index]

	# This loop runs till start pointer crosses
	# end pointer, and when it does we swap the
	# pivot with element on end pointer
	# draw_list(draw_info,{pivot: draw_info.RED, end: draw_info.GREEN}, True)
	while start < end:
	 
		# Increment the start pointer till it finds an
		# element greater than  pivot
		while start < len(array) and array[start] <= pivot:
			start += 1
		     
		# Decrement the end pointer till it finds an
		# element less than pivot
		while array[end] > pivot:
			end -= 1
		 
		# If start and end have not crossed each other,
		# swap the numbers on start and end
		if(start < end):
			array[start], array[end] = array[end], array[start]

		# Swap pivot element with element on end pointer.
		# This puts pivot on its correct sorted place.
		draw_list(draw_info,{pivot: draw_info.RED, end: draw_info.GREEN}, True)
		time.sleep(0.01)
	array[end], array[pivot_index] = array[pivot_index], array[end]
	draw_list(draw_info,{start: draw_info.RED, end: draw_info.GREEN}, True)
	# Returning end pointer to divide the array into 2
	return end

def temp_quick_sort(start, end, array, draw_info,speed=None):

	if (start < end):

		# p is partitioning index, array[p]
		# is at right place
		p = partition(start, end, array, draw_info)
		draw_list(draw_info,{start: draw_info.RED, end: draw_info.GREEN}, True)
		time.sleep(speed)
		# Sort elements before partition
		# and after partition
		temp_quick_sort(start, p - 1, array, draw_info, speed)
		temp_quick_sort(p + 1, end, array, draw_info, speed)

def quick_sort(draw_info, speed=None):
	lst = draw_info.lst
	temp_quick_sort(0, len(lst) - 1, lst, draw_info, speed)
	yield True 
	return lst
