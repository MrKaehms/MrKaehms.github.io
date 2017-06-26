# Bob Kaehms
# PLTW CSP Training
# Remix a python program
# pygame Space Invaders, to SpongeBob WaterWorld
# NOTE: This game requires package pygame. Installation is tricky
# See https://www.webucator.com/blog/2015/03/installing-the-windows-64-bit-version-of-pygame/

from pygame import *
import random


class Sprite:
	def __init__(self, xpos, ypos, filename):
		self.x = xpos
		self.y = ypos
		self.bitmap = image.load(filename)
		self.bitmap.set_colorkey((0,0,0))
	def set_position(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
	def render(self):
		screen.blit(self.bitmap, (self.x, self.y))

class Gold(Sprite):
	def __init__(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
		self.bitmap = image.load('data/images/pirategold.png')
		self.drops=0;
		self.falling=False
		self.goldStop=0
		
	def render(self):
		screen.blit(self.bitmap, (self.x, self.y))
	def drop():
		self.y = self.y + 10	
	def delete(self):
		self.kill()
				
def Intersect(s1_x, s1_y, s2_x, s2_y):
	if (s1_x > s2_x - 32) and (s1_x < s2_x + 32) and (s1_y > s2_y - 32) and (s1_y < s2_y + 32):
		return 1
	else:
		return 0


def updateGoldPos(pg):
	if pg.x > 0 and pg.y < 550:
		pg.y+=2

def initGold():
	for count in range(5):
		gold.append(Sprite(0, 0, 'data/images/pirategold.png')) 
		
def goldUpdateActive():
	for count in range(5):
		if not gold[count].falling:
			updateFalling(gold[count])
			
def goldUpdatePositions():
	for count in range(5):
		if  gold[count].falling:
			if gold[count].y < 550:
				gold[count].y +=2			 			
				gold[count].render()
			else:
				gold[count].goldStop+=1
				if gold[count].goldStop > 200:
					gold[count].goldStop=0
					gold[count].x= random.randint(10, 650)	
					gold[count].y=0
					gold[count].falling=False
		else:
			updateFalling(gold[count])			
		gold[count].render()			
						
def updateFalling(g):
	r = random.randint(1, 3000)
	if 	r <=10:
		g.falling=True
		g.x= random.randint(10, 650)
		
def updateScore(score):

   scoretext=font.render("Score:"+str(score), 1,(255,255,255))
   screen.blit(scoretext, (660, 540))
	

init()
 
screen = display.set_mode((800,600))
key.set_repeat(1, 1)
display.set_caption('Sbob Waterworld')
 
backdrop = image.load('data/images/underwater-background.jpg')

 

x = 0
score = 0
font = font.SysFont("monospace", 40)
 
hero = Sprite(20, 500, 'data/images/sbob.png')
#scoreboard = Sprite(660, 540, 'data/images/scoreboard.jpg') 

crabtrap = Sprite(450, 0, 'data/images/crabtrap.png')
cha_ching = mixer.Sound('data/sounds/cha_ching.wav')  #load sound
bonk = mixer.Sound('data/sounds/bonk.wav')  #load sound

gold = []
for count in range(5):
	gold.append(Sprite(0, 0, 'data/images/pirategold.png')) 

for count in range(len(gold)):
		gold[count].falling = False
		gold[count].goldStop=0
		gold[count].render()
		

initGold()

cha_ching.play()

crabtrap.render()
quit = 0

while quit == 0:
	screen.blit(backdrop, (0, 0))

	goldUpdatePositions()

	
	crabtrap.y+=3
	if crabtrap.y > 580:
		crabtrap.x=random.randint(10, 650)
		crabtrap.y=0
		
	crabtrap.render()
	
#	scoreboard.render()	


	if Intersect(hero.x, hero.y, crabtrap.x, crabtrap.y):	
		quit = 1
		bonk.play()
		time.delay(1500)
		
	for count in range(len(gold)):	
		if Intersect(hero.x, hero.y, gold[count].x, gold[count].y):
			score +=1
			cha_ching.play()
			updateScore(score)
			gold[count].x= random.randint(10, 650)
			gold[count].y=0
			gold[count].falling=False
	
	for ourevent in event.get():
		if ourevent.type == QUIT:
			quit = 1
		if ourevent.type == KEYDOWN:
			if ourevent.key == K_RIGHT and hero.x < 590:
				hero.x += 5
			if ourevent.key == K_LEFT and hero.x > 10:
				hero.x -= 5




	hero.render()
	updateScore(score)
    
	display.update()
	time.delay(5)

