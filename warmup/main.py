import pygame
import time
from collections import deque
from random import choice
import os

# ======================================================
# Initialising pygame
# pygame.init()
pygame.font.init()

# ======================================================
# init Constant

FPS = 30
WITHE = (255, 255, 255)
BLACK_M = (18, 18, 18)
PERPEL = (255, 0, 255)
WIDTH, HEIGHT = 500, 600
DRAW_FIXER = 23
game_map = [[50*x+25, 50*y+125] for x in range(10) for y in range(10)]

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
button = pygame.image.load("./Assets/button.png")
setting_score = pygame.font.SysFont("comicsans", 20, bold=True, italic=False)
setting_finish = pygame.font.SysFont("comicsans", 50, bold=True, italic=False)
setting_reset = pygame.font.SysFont("comicsans", 25, bold=False, italic=False)

# ======================================================
# blit base image


# ======================================================
# game control func

def playing(state, score, clock): # _again_and_state_and_score
	f = open("score.txt", "r+")
	if int(f.read()) < score:
		f.close()
		os.remove("score.txt")
		f = open("score.txt", "a+")
		f.write(str(score))

	if state == 1:
		state_text = setting_finish.render("YOU WIN!", 1, PERPEL)
		win.blit(state_text, (125, 290))
	elif state == 2:
		return True
	else:
		state_text = setting_finish.render("YOU LOSE...", 1, PERPEL)
		win.blit(state_text, (100, 290))

	command = True
	rreset_ch = False

	while command:
		clock.tick(FPS)
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				command = False
				break
			if event.type == pygame.MOUSEBUTTONDOWN:
				# print(mouse[0], mouse[1])
				if 353 < mouse[0] < 447 and 23 < mouse[1] < 77:
					command = False
					rreset_ch = True
					break
		pygame.display.update()

	if rreset_ch:
		return True
	else:
		return False

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

def draw_game_win(head, body, apple, score, best_score_saved):
	win.fill(WITHE)
	win.blit(top_1, (0, 0))
	win.blit(top_2, (0, 93))
	win.blit(button, (350, 20))
	match_score = setting_score.render(f"Match Score: {score}", 1, BLACK_M)
	best_score = setting_score.render(f"Best Score: {best_score_saved}", 1, BLACK_M)
	reset_text = setting_reset.render(f"RESET", 1, PERPEL)
	win.blit(reset_text, (359, 30))
	win.blit(match_score, (10, 10))
	win.blit(best_score, (10, 50))
	for i in range(11):
		win.blit(horizontal_line, (0, 100+(50*i)-1))
	for i in range(11):
		win.blit(vertical_line, ((50*i)-1, 100))

	for i in body:
		win.blit(snake_body, (i[0]-23, i[1]-23))  # (2, 102)
	win.blit(snake_head, (head[0]-23, head[1]-23))  # (52, 102)

	if apple[1] == 5:
		win.blit(apple_5, (apple[0][0]-23, apple[0][1]-23))
	elif apple[1] == 10:
		win.blit(apple_10, (apple[0][0]-23, apple[0][1]-23))
	else: 
		win.blit(apple_15, (apple[0][0]-23, apple[0][1]-23))

	pygame.display.update()


# ======================================================
# new place of apple

def new_apple(game_map, body, head): # walls,
	game_map_c = game_map.copy()
	for i in body:
		game_map_c.remove(i)
	for i in head:
		game_map_c.remove(i)

	result_apple = choice(game_map_c)
	result_score = choice([5, 10, 15])

	return (result_apple, result_score)

# ======================================================
# main func

def main():
	clock = pygame.time.Clock()
	game = True
	while game:
		run = True
		score = 0
		state = 0
		f = open("score.txt", "a+")
		f.close()
		with open("score.txt", "r+") as f:
			best_score_saved = f.read()
			if best_score_saved == "":
				best_score_saved = 0
				f.write("0")
			else:
				best_score_saved = int(best_score_saved)

		walls = []
		for x in range(12):
		    for y in range(12):
		        if 0 < 50*x-25 < 500 and 100 < 50*y+75 < 600:
		            continue
		        walls.append([50*x-25, 50*y+75])

		head = [75, 125]
		body = [[25, 125]]
		head_c = head.copy()
		apple = new_apple(game_map, body, [head])
		add_to_end = False
		real_direction = 1
		user_direction = 1
		movment_direction = deque([1])
		fps_level = 0
		move = False
		move_counter = 0
		while run:
			clock.tick(FPS)

			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					game = False
					break
				if event.type == pygame.MOUSEBUTTONDOWN:
					# print(mouse[0], mouse[1])  350 20
					if 353 < mouse[0] < 447 and 23 < mouse[1] < 77:
						run = False
						state = 2
						break


			keys_pressed = pygame.key.get_pressed()
			user_direction = handel_movment(keys_pressed, user_direction)

			fps_level += 1
			if fps_level == 20:
				real_direction = user_direction
				move = True
				fps_level = 0
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

				if head_c == apple[0]:
					score += apple[1]
					last_peace = body[-1].copy()
					add_to_end =True
					if len(body) + 2 == 100:
						run = False
						state = 1
						break
					apple = new_apple(game_map, body, [head, head_c])

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
					if add_to_end:
						movment_direction.append(movment_direction[-1])
						body.append(last_peace)
						add_to_end = False
					movment_direction.rotate(1)
					movment_direction[0] = real_direction
					move = False
				else:
					move_counter += 1

			draw_game_win(head, body, apple, score, best_score_saved)

		if game:
			game = playing(state, score, clock)

	pygame.quit()


# ======================================================
# run game

main()
