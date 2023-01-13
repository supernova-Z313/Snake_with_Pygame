import pygame
import time
# ======================================================
# Initialising pygame
# pygame.init()
# ======================================================
# init some base value

WIDTH, HEIGHT = 500, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("hello")

def main():
	run = True
	while run:
		time.sleep(1)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break

	pygame.quit()


main()
