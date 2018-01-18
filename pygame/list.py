import pygame, sys, random
from pygame.locals import *

#constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
DIAMOND = 4

#a dictionary linking resources to textures
textures = {
			DIRT : pygame.image.load('images/dirt.png'),
			GRASS : pygame.image.load('images/grass.png'),
			WATER : pygame.image.load('images/water.png'),
			COAL : pygame.image.load('images/coal.png'),
			DIAMOND : pygame.image.load('images/diamond.png')
		}

#useful game dimensions
TILESIZE = 40
MAPWIDTH = 3
MAPHEIGHT = 5

#a list of resources
resources = [DIRT,GRASS,WATER,COAL, DIAMOND]
#use list comprehension to create our tilemap
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]
#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

#loop through each row
for rw in range(MAPHEIGHT):
#loop through each column in that row
	for cl in range(MAPWIDTH):
		#pick a random number between 0 and 15
		randomNumber = random.randint(0,18)
		if randomNumber == 0:
			randNumber_2 = random.randint(0,3)
			if randNumber_2 == 0:
				title = DIAMOND
			elif randNumber_2 > 0:
				title = WATER
		#if a zero, then the tile is coal
		elif randomNumber == 1:
			tile = COAL
		#water if the random number is a 1 or a 2
		elif randomNumber == 2 or randomNumber == 4:
			tile = WATER
		elif randomNumber >= 5 and randomNumber <= 7:
			tile = GRASS
		else:
			tile = DIRT
		#set the position in the tilemap to the randomly chosen tile
		tilemap[rw][cl] = tile
	
while True:
	#get all the user events
	for event in pygame.event.get():
		#if the user wants to quit
		if event.type == QUIT:
			#and the game and close the window
			pygame.quit()
			sys.exit()
			
		#loop through each row
		for row in range(MAPHEIGHT):
			#loop through each column in the row
			for column in range(MAPWIDTH):
				#draw the resource at that position in the tilemap, using the correct image
				DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
				
		#update the display
		pygame.display.update()