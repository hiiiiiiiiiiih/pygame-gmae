#IMPORT THE IMPORTANT
import pygame
import sys
import random

pygame.init()

pygame.display.set_caption('Nombre del juego') 

#colors
RED = (255,0,0)
GREEN = (0,255,0)
GHOST = (0,255,0,25)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

#nonsense
spawn_time = 0
dificulty = 5 # mas grade el numero menos 
score = 0000000000
Win = False
level = 0

#powers
multi = 1
colro = WHITE
pow =[-160,300]
powers_list = [pow]
invis = 0
if dificulty == 4 or dificulty ==5:
	power_time = 60
elif dificulty == 3 or dificulty == 2:
	power_time = 120
else:
	power_time = 180
invistime = power_time

#screen size
SW = 320
SH = 600

#text
once = True
font2 = pygame.font.SysFont("comicsans",40,True)
font1 = pygame.font.SysFont("comicsans",30,True)





#Barier vars
barrier1x = SH/20
barrier1y = SH
barrier2x = SW
barrier2y = SH/20

#player vars
p_size = 20
p_x = (SW/2)-(p_size/2)
p_y = (SH/20 * 17)
p_speed = 20
screen = pygame.display.set_mode((SW,SH))

#falling? blocks vars
enemy_pos = [-30,0]
blocks_list = [enemy_pos]
if dificulty >= 3 and dificulty <=5:
	block_speed = 10
else:
	block_speed =5

gameover = False
end = False
clock = pygame.time.Clock()



#functions		
def invis_timer():
	global invis
	if invis == 0:
		collision_block(blocks_list)
		collision_power(powers_list,p_x,p_y,p_size)
	else:
		collision_power(powers_list,p_x,p_y,p_size)
	

def draw_player():
	global GREEN
	global BLUE
	global WHITE
	global multi
	global colro
	multi = multi + 1
	if multi == 4:
		colro= GREEN
		multi=-1
	elif multi == 2 :
		colro = BLUE
	elif multi == 0:
		colro = WHITE

	if invis == 1 and (invistime  % 2) == 0:
		pygame.draw.rect(screen,BLACK,(p_x,p_y,p_size,p_size))
	else:
		pygame.draw.rect(screen,GREEN,(p_x,p_y,p_size,p_size))

def power_order(powers_list):
	wide = len(powers_list)
	while len(powers_list) <= 0:
		wide = len(powers_list)

		power_order.x_pos = (random.randint(1,13) * p_size) + 10
		power_order.y_pos = 0
		powers_list.append([power_order.x_pos,power_order.y_pos])

def power_move(powers_list):
	global block_speed
	for pow in powers_list:
		pow[1] = pow[1] + block_speed

def draw_power(powers_list):
	global colro

	for pow in powers_list:
		pygame.draw.rect(screen,colro,(pow[0],pow[1],p_size,p_size))
	
def delete_power(powers_list):
	for pow in powers_list:
		if pow[1] >= SH:
			
			powers_list.pop(0)
			

def collision_power(powers_list,p_x,p_y,p_size):
	global invis
	for pow in powers_list:
		x_power =pow[0]
		y_power = pow[1]
		if p_y+ 10 >= y_power and p_y + 10 <= y_power + 20 and p_x+10 >= x_power and p_x + 10 <= x_power + 20:
			invis = 1


			

def dropper(blocks_list):
	long = len(blocks_list)
		
	while len(blocks_list) <= long:
		long = len(blocks_list) 
		
		dropper.x_pos = (random.randint(1,13) * p_size) + 10
		dropper.y_pos = 0
		blocks_list.append([dropper.x_pos,dropper.y_pos])
		
	

def move_blocks(blocks_list):
	for enemy_pos in blocks_list:
		enemy_pos[1] = enemy_pos[1] + block_speed

def draw_blocks(blocks_list):

	for enemy_pos in blocks_list:
		pygame.draw.rect(screen,RED,(enemy_pos[0],enemy_pos[1],p_size,p_size))
	
def delete_block(blocks_list):
	for enemy_pos in blocks_list:
		if enemy_pos[1] >= SH:
			
			blocks_list.pop(0)
			

def collision_block(blocks_list):
	global p_x
	global p_y
	global p_size
	global block_speed

	for enemy_pos in blocks_list:
		if p_y+5 >= enemy_pos[1] and p_y + 15 <= enemy_pos[1] + p_size and p_x+5 >= enemy_pos[0] and p_x + 15 <= enemy_pos[0] + p_size:
			p_y = p_y + (block_speed * 2)
			

def barrier():
	
	pygame.draw.rect(screen,BLUE,(0,0,barrier1x,barrier1y))
	pygame.draw.rect(screen,BLUE,(SW-barrier1x,0,barrier1x,barrier1y))
	pygame.draw.rect(screen,GREEN,(0,0,barrier2x,barrier2y))
	pygame.draw.rect(screen,RED,(0,SH-barrier2y,barrier2x,barrier2y))

def collision_always():
	global p_x
	global p_y
	global gameover
	global Win
	global once
	global level
	if p_x <= SW/20:
		p_x = p_x + p_speed
	if p_x >= SW-barrier1x:
		p_x = p_x - p_speed
	if p_y <= SW/20 +5:
		p_y = p_y + p_speed/2
	if p_y <= 35:
		Win = True
		level = 2
		
	if p_y >= SH - (SH/20):
		gameover = True;
		level = 2
		

	

def drawing(blocks_list,powers_list):
	global invis
	global Win 
	global invistime
	global score
	global level
	if level == 1:
		screen.fill(BLACK)

		

		barrier()
	
		if Win == False:
			draw_player()
			invis_timer()
			draw_blocks(blocks_list)
			draw_power(powers_list)
		if invis == 1:
			invistime = invistime -1

		if invistime == 1:
			invis = 0
			invistime = power_time
	
		

		

		move_blocks(blocks_list)

		

def controls():
	global p_y
	global p_x
	global p_speed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				p_x = p_x - p_speed
			elif event.key == pygame.K_RIGHT:
				p_x = p_x + p_speed
			elif event.key == pygame.K_UP:
				p_y = p_y - p_speed/2
			elif event.key == pygame.K_DOWN:
				p_y = p_y + p_speed/2

def escapesis():
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
		if event.type == pygame.QUIT:
			sys.exit()

def get_dif():
	global dificulty
	global level
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				dificulty = 0
				level = 1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_2:
				dificulty = 1
				level = 1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_3:
				dificulty = 2
				level = 1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_4:
				dificulty = 3
				level = 1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_5:
				dificulty = 4
				level = 1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_6:
				dificulty = 5
				level = 1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()

		if event.type == pygame.QUIT:
			sys.exit()
	

def printdiftext():
	text4 = font1.render("Presiona un numero ",1,(255,255,255))
	size4 = text4.get_width()
	screen.blit(text4,(SW/2-size4/2,230))
	text5 = font1.render("del 1 al 6 en tu teclado",1,(255,255,255))
	size5 = text5.get_width()
	screen.blit(text5,(SW/2-size5/2,270))
	text6 = font1.render("para selecionar dificultad",1,(255,255,255))
	size6 = text6.get_width()
	screen.blit(text6,(SW/2-size6/2,310))





























#main loop
while not end:

	if level == 0:
		get_dif()
		barrier()
		printdiftext()

	

	if gameover == True and level == 2  :
		if dificulty >= 1 :
			final_score = score * (dificulty ** 3)
			text = font2.render("Score: " + str(final_score)+ " L",1,(255,255,255))
			size = text.get_width()
			screen.blit(text,(SW/2-size/2,230))
			escapesis()
		elif dificulty == 0:
			final_score = score
			text = font2.render("Score: " + str(final_score)+ " L",1,(255,255,255))
			size = text.get_width()
			screen.blit(text,(SW/2-size/2,230))
			escapesis()
		text2 = font1.render("Presiona escape(esc)",1,(255,255,255))
		size2 = text2.get_width()
		screen.blit(text2,(SW/2-size2/2,270))
		text3 = font1.render("Para cerrar el juego",1,(255,255,255))
		size3 = text3.get_width()
		screen.blit(text3,(SW/2-size3/2,310))
		once = False

	if Win == True and level == 2:
		if dificulty >= 1 :
			final_score = score * (dificulty ** 3) 
			text = font2.render("Score: " + str(final_score )+ " W",1,(255,255,255))
			size = text.get_width()
			screen.blit(text,(SW/2-size/2,230))
			escapesis()
		elif dificulty == 0 :
			final_score = score 
			text = font2.render("Score: " + str(final_score)+ "W",1,(255,255,255))
			size = text.get_width()
			screen.blit(text,(SW/2-size/2,230))
			escapesis()
		text2 = font1.render("Presiona escapa(esc)",1,(255,255,255))
		size2 = text2.get_width()
		screen.blit(text2,(SW/2-size2/2,270))
		text3 = font1.render("Para cerrar el juego",1,(255,255,255))
		size3 = text3.get_width()
		screen.blit(text3,(SW/2-size3/2,310))
		once = False






	if once == True and level ==1 :
		drawing(blocks_list, powers_list) 

		power_move(powers_list)
	

		if spawn_time >= 5 -dificulty:
			dropper(blocks_list)
			spawn_time = 0

		if dificulty >= 1:
			chance =  random.randint(0,(dificulty**3))
		else:
			chance = dificulty

	
		if chance == dificulty:
			power_order(powers_list)
		
		
		
		

	


		spawn_time = spawn_time + 1

		delete_block(blocks_list)

		delete_power(powers_list)

		controls()

		collision_always()

	

		score += 1
		

	pygame.display.update()
	clock.tick(30)
