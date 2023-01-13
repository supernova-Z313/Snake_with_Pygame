import pygame
import time
from collections import deque

# ======================================================
# Initialising pygame
# pygame.init()

# ======================================================
# init Constant

FPS = 30
WITHE = (255, 255, 255)
WIDTH, HEIGHT = 500, 600

# ======================================================
# Load base value

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("hello")
top_1 = pygame.image.load("./Assets/top_line1.png")
top_2 = pygame.image.load("./Assets/top_line2.png")
horizontal_line = pygame.image.load("./Assets/line.jpg")
vertical_line = pygame.transform.rotate(horizontal_line, 90)
snake_body = pygame.image.load("./Assets/body.png")
snake_head = pygame.image.load("./Assets/head.png")
apple_5 = pygame.image.load("./Assets/5.png")
apple_10 = pygame.image.load("./Assets/10.png")
apple_15 = pygame.image.load("./Assets/15.png")

# ======================================================
# blit base image


# ======================================================
# game control func

def play_again():
	pass

# ======================================================
# handleing movment

def handel_movment(keys_pressed, last_direction):
	# also can add big char
	if keys_pressed[pygame.K_d] and last_direction != 3:
		last_direction = 1
	elif keys_pressed[pygame.K_s] and last_direction != 4:
		last_direction = 2
	elif keys_pressed[pygame.K_a] and last_direction != 1:
		last_direction = 3
	elif keys_pressed[pygame.K_w] and last_direction != 2:
		last_direction = 4

	return last_direction

# ======================================================
# update window func

def draw_game_win(head, body):
	win.fill(WITHE)
	win.blit(top_1, (0, 0))
	win.blit(top_2, (0, 93))
	for i in range(11):
		win.blit(horizontal_line, (0, 100+(50*i)-1))
	for i in range(11):
		win.blit(vertical_line, ((50*i)-1, 100))

	for i in body:
		win.blit(snake_body, (i[0]-23, i[1]-23))  # (2, 102)
	win.blit(snake_head, (head[0]-23, head[1]-23))  # (52, 102)

	pygame.display.update()


# ======================================================
# new place of apple
def new_apple(walls, body, head):
	pass


# ======================================================
# main func

def main():
	clock = pygame.time.Clock()
	game = True
	while game:
		run = True
		
		walls = []
		for x in range(12):
		    for y in range(12):
		        if 0 < 50*x-25 < 500 and 100 < 50*y+75 < 600:
		            continue
		        walls.append([50*x-25, 50*y+75])

		head = [75, 125]
		body = [[25, 125]]
		head_c = head.copy()
		# body_c = body.copy()
		real_direction = 1
		user_direction = 1
		movment_direction = deque([1])
		fps_level = 0
		move = False
		move_counter = 0
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					break

			keys_pressed = pygame.key.get_pressed()
			user_direction = handel_movment(keys_pressed, user_direction)

			fps_level += 1
			if fps_level == 20:
				real_direction = user_direction
				move = True
				fps_level = 0
				# body_c = body.copy()
				head_c = head.copy()
				if real_direction == 1:
					head_c[0] += 50
				elif real_direction == 2:
					head_c[1] += 50
				elif real_direction == 3:
					head_c[0] -= 50
				else:
					head_c[1] -= 50

				if head_c in walls or head_c in body:
					run = False
					break

			# move body
			if move:
				for ind, i in enumerate(body):
					if movment_direction[ind] == 1:
						i[0] += 10
					elif movment_direction[ind] == 2:
						i[1] += 10
					elif movment_direction[ind] == 3:
						i[0] -= 10
					else:
						i[1] -= 10

			# move head			
			if move:
				# 10 pixel per 1/30 sec for 5 tick 
				if real_direction == 1:
					head[0] += 10
				elif real_direction == 2:
					head[1] += 10
				elif real_direction == 3:
					head[0] -= 10
				else:
					head[1] -= 10

				if move_counter == 4:
					move_counter = 0
					movment_direction.rotate(1)
					movment_direction[0] = real_direction
					move = False
				else:
					move_counter += 1

			draw_game_win(head, body)

		break
		# play_again()

	pygame.quit()


# ======================================================
# run game

main()
