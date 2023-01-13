import pygame
import time

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
win.fill(WITHE)
top_1 = pygame.image.load("./Assets/top_line1.png")
top_2 = pygame.image.load("./Assets/top_line2.png")
horizontal_line = pygame.image.load("./Assets/line.jpg")
vertical_line = pygame.transform.rotate(horizontal_line, 90)
snake_body = pygame.image.load("./Assets/body.png")
snake_head = pygame.image.load("./Assets/head.png")

# ======================================================
# blit base image

win.blit(top_1, (0, 0))
win.blit(top_2, (0, 93))
for i in range(11):
	win.blit(horizontal_line, (0, 100+(50*i)-1))
for i in range(11):
	win.blit(vertical_line, ((50*i)-1, 100))

# ======================================================
# game control func

def play_again():
	pass

# ======================================================
# update window func

def draw_game_win(): # head, body
	win.blit(snake_body, (2, 102))
	win.blit(snake_head, (52, 102))
	pygame.display.update()


# ======================================================
# main func

def main():
	clock = pygame.time.Clock()
	game = True
	while game:
		run = True
		snake = []
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					break

			draw_game_win()

		play_again()
	
	pygame.quit()


# ======================================================
# run game

main()
