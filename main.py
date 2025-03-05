# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import *

def main():

	# Init Game
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()

	game_clock = pygame.time.Clock()  
	dt = 0

	# Set Screen Variables
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Create update / draw groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	# Update Player Containers
	Player.containers = (updatable, drawable)

	# Init Player
	player_x = SCREEN_WIDTH / 2
	player_y = SCREEN_HEIGHT / 2
	# player = Player(player_x, player_y)

	# Create Screen
	while True:
    
		# allows user to click to close program
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill('#000000')

		# update player
		# player.update(dt)
		updatable.update(dt)

		# draw player
		# player.draw(screen)
		for draw_group in drawable:
			draw_group.draw(screen)
		
		pygame.display.flip()   

		dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()