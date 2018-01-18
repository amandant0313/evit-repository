import pygame, sys, random
from pygame.locals import *

#constants representing colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
DIAMOND = 4
LAVA = 5
ROCK = 6

#a dictionary linking resources to textures
textures = {
			DIRT : pygame.image.load('images/dirt.png'),
			GRASS : pygame.image.load('images/grass.png'),
			WATER : pygame.image.load('images/water.png'),
			COAL : pygame.image.load('images/coal.png'),
			DIAMOND : pygame.image.load('images/diamond.png'),
			LAVA : pygame.image.load('images/lava.png'),
			ROCK : pygame.image.load('images/rock.png')
		}
		
inventory = {
			DIRT : 0,
			GRASS : 0,
			WATER : 0,
			COAL : 0,
			DIAMOND : 0,
			LAVA : 0,
			ROCK : 0
		}
#useful game dimensions
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

#the player image
PLAYER = pygame.image.load('images/player.png')
#the position of the player [x,y]
playerPos = [0,0]

#a list of resources
resources = [DIRT, GRASS, WATER, COAL, DIAMOND, LAVA, ROCK]
#use list comprehension to create our tilemap
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 50))

#add a font for our inventory
INVFONT = pygame.font.Font('FreeSans/FreeSansBold.ttf', 18)

#loop through each row
for rw in range(MAPHEIGHT):
#loop through each column in that row
	for cl in range(MAPWIDTH):
		#pick a random number between 0 and 15
		randomNumber = random.randint(0,20)
		if randomNumber == 0:
			randNumber_2 = random.randint(0,3)
			if randNumber_2 == 0:
				title = DIAMOND
			elif randNumber_2 > 0:
				title = WATER
		#if a zero, then the tile is coal
		elif randomNumber == 1:
			title = COAL
		#water if the random number is a 1 or a 2
		elif randomNumber == 2 or randomNumber == 3:
			title = WATER
		elif randomNumber >= 4 and randomNumber <= 7:
			title = GRASS
		elif randomNumber >= 8 and randomNumber <=10:
			title = LAVA
		elif randomNumber >=11 and randomNumber <=14:
			title = ROCK
		else:
			title = DIRT
		#set the position in the tilemap to the randomly chosen tile
		tilemap[rw][cl] = title
		
while True:
	#get all the user events
	for event in pygame.event.get():
		#if the user wants to quit
		if event.type == QUIT:
			#end the game and close the window
			pygame.quit()
			sys.exit()
		#if a key is pressed
		elif event.type == KEYDOWN:
			#if the right arrow is pressed
			if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1:
				#change the player's x position
				playerPos[0] += 1
			if event.key == K_LEFT and playerPos[0] > 0:
				#change the player's x position
				playerPos[0] -= 1
			if event.key == K_UP and playerPos[1] > 0:
				#change the player's x position
				playerPos[1] -= 1
			if event.key == K_DOWN and playerPos[1] < MAPHEIGHT -1:
				#change the player's x position
				playerPos[1] += 1
			if event.key == K_SPACE:
				#what resource is the player standing on?
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				#player now has 1 more of this resource
				inventory[currentTile] += 1
				#the player is now standing on dirt
				tilemap[playerPos[1]][playerPos[0]] = DIRT
			
			#placing dirt
			if (event.key == K_1):
				#get the tile to swap with the dirt
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				#if we have dirt in our inventory
				if inventory[DIRT] > 0:
					#remove one dirt and place it
					inventory[DIRT] -= 1
					tilemap[playerPos[1]][playerPos[0]] = DIRT
					#swap the item that was there before
					inventory[currentTile] += 1
				
	#loop through each row
	for row in range(MAPHEIGHT):
		#loop through each column in the row
		for column in range(MAPWIDTH):
			#draw the resource at that position in the tilemap, using the correct image
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	
	#display the player at the correct position
	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
	
	#display the inventory, starting 10 pixels in
	placePosition = 10
	for item in resources:
		#add the image
		DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 30
		#add the text showing the amount in the inventory
		textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 50
		
	#update the display
	pygame.display.update()
	