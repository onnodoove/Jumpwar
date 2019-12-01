# Import necessary modules
import pygame
import sys
import random
import os
import math

 
pygame.init()
pygame.display.init()
pygame.mixer.pre_init()
pygame.font.init()

pygame.mixer.init()
myfont = pygame.font.SysFont('Arial', 20)
Exp=[0]

white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_grey = ((200,200,200))
dark_grey = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))

Beep = pygame.mixer.Sound('Beep.ogg')
Blast = pygame.mixer.Sound('Boom.ogg')
LevelUp=pygame.mixer.Sound('Applause.ogg')
Eating=pygame.mixer.Sound('Eating.ogg')
Sizzle=pygame.mixer.Sound('Sizzle.ogg')
Laser=pygame.mixer.Sound('Laser.ogg')
Yay=pygame.mixer.Sound('Yay.ogg')
Vaporize=pygame.mixer.Sound('Vaporize.ogg')
Teleport=pygame.mixer.Sound('Teleport.ogg')
Victory=pygame.mixer.Sound('Victory.ogg')
Hurt=pygame.mixer.Sound('Hurt.ogg')
Yeah=pygame.mixer.Sound('Yeah.ogg')
Launch=pygame.mixer.Sound('Launch.ogg')
Ahh=pygame.mixer.Sound('Ahh.ogg')
Steal=pygame.mixer.Sound('Steal.ogg')

RedStar=pygame.image.load('RedStar.png')
YellowStar=pygame.image.load('YellowStar.png')
BlueStar=pygame.image.load('BlueStar.png')
Asteroid=pygame.image.load('Asteroid.png')
Asteroid2=pygame.image.load('Asteroid2.png')
Asteroid3=pygame.image.load('Asteroid3.png')
Wormhole=pygame.image.load('Wormhole.png')

Drone=pygame.image.load('Drone.png')
Drone2=pygame.image.load('Drone2.png')
Drone3=pygame.image.load('Drone3.png')
Drone4=pygame.image.load('Drone4.png')
Drone5=pygame.image.load('Drone5.png')
Drone6=pygame.image.load('Drone6.png')
Drone7=pygame.image.load('Drone7.png')
Drone8=pygame.image.load('Drone8.png')
Drone9=pygame.image.load('Drone9.png')
Drone10=pygame.image.load('Drone10.png')
Drone11=pygame.image.load('Drone11.png')
Drone12=pygame.image.load('Drone12.png')
Drone13=pygame.image.load('Drone13.png')
Drone14=pygame.image.load('Drone14.png')
Drone15=pygame.image.load('Drone15.png')

HunterDrone=pygame.image.load('HunterDrone.png')

Interceptor=pygame.image.load('Interceptor.png')
Interceptor2=pygame.image.load('Interceptor2.png')
Interceptor3=pygame.image.load('Interceptor3.png')
Interceptor4=pygame.image.load('Interceptor4.png')
Interceptor5=pygame.image.load('Interceptor5.png')
Interceptor6=pygame.image.load('Interceptor6.png')
Interceptor7=pygame.image.load('Interceptor7.png')
Interceptor8=pygame.image.load('Interceptor8.png')
Interceptor9=pygame.image.load('Interceptor9.png')
Interceptor10=pygame.image.load('Interceptor10.png')

Frigat=pygame.image.load('Frigat.png')
Frigat2=pygame.image.load('Frigat2.png')
Frigat3=pygame.image.load('Frigat3.png')
Frigat4=pygame.image.load('Frigat4.png')
Frigat5=pygame.image.load('Frigat5.png')
Frigat6=pygame.image.load('Frigat6.png')

MissilePlatform=pygame.image.load('MissilePlatform.png')
MissilePlatform2=pygame.image.load('MissilePlatform2.png')

Liberator=pygame.image.load('Liberator.png')

Teleporter=pygame.image.load('Teleporter.png')
Eye=pygame.image.load('Eye.png')
Leech=pygame.image.load('Leech.png')
Ramjet=pygame.image.load('Ramjet.png')
Mothership=pygame.image.load('Mothership.png')

Bomb=pygame.image.load('Bomb.png')
Stop=pygame.image.load('Stop.png')
JGrid = pygame.image.load('JGrid.png')
Galaxy=pygame.image.load('Galaxy.png')
GalaxySmall=pygame.image.load('GalaxySmall.png')
RadarScreen=pygame.image.load('Radar.png')
Bombs=pygame.image.load('Bombs.png')
LaserBeams=pygame.image.load('LaserBeams.png')
SunCrash=pygame.image.load('SunCrash.png')
AsteroidHarvest=pygame.image.load('Asteroids.png')
Numpad=pygame.image.load('Numpad.png')
LaserScreen=pygame.image.load('LaserScreen.png')
MissileScreen=pygame.image.load('MissileScreen.png')
EnemyScreen=pygame.image.load('EnemyScreen.png')
RadarExample=pygame.image.load('RadarScreen.png')

Happy=pygame.image.load('Happy.png')
Sad=pygame.image.load('Sad.png')

Explosion=pygame.image.load('Blast.png')

Level=0
PlayerLevel=0
PlayerHull=0
PlayerMissiles=0
Exp=[None]

pygame.display.set_icon(Galaxy)
pygame.display.set_caption('Jumpwar')
Width=int(1000)
Heigth=int(1000)
screen = pygame.display.set_mode((Width, Heigth))
CollectedEnemies=[None]*7

Load=open('Jumpwar.sav', 'r')
LoadList=list(Load)
Load.close()
SaveCounter=0

def wait():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
	                		return
	
def DoHelp ():
	global myfont
	Selection=True
	while Selection:
		Status = myfont.render('Press enter to start the game', False, yellow)		
		text1 = myfont.render('Welcome to Jumpwar, a turn-based, tactical, space game.', False, green)
		text2 = myfont.render('Make a choice to read about parts of the game:', False, green)
		text3 = myfont.render('1> Purpose of the game', False, green)
		text4 = myfont.render('2> Movement', False, green)
		text5 = myfont.render('3> Firing weapons', False, green)
		text6 = myfont.render('4> Finding enemies', False, green)
		text7 = myfont.render('5> Repairing your ship', False, green)
		text8 = myfont.render('6> Moving to the next level of the game', False, green)
		text9 = myfont.render('7> In-game sounds', False, green)
		text10 = myfont.render('Press h anywhere in-game to return to the help-screens, ESC quits the game', False, green)

		screen.blit(Galaxy,(0,0))
		screen.blit(text1,(0,0))
		screen.blit(text2,(0,50))
		screen.blit(text3,(0,100))
		screen.blit(text4,(0,150))
		screen.blit(text5,(0,200))
		screen.blit(text6,(0,250))
		screen.blit(text7,(0,300))
		screen.blit(text8,(0,350))
		screen.blit(text9,(0,400))
		screen.blit(text10,(0,450))

		screen.blit(Status,(0,980))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP1 or event.key == pygame.K_1:
					DoHelpPurpose()
				if event.key == pygame.K_KP2 or event.key == pygame.K_2:
					DoHelpMovement()		
				if event.key == pygame.K_KP3 or event.key == pygame.K_3:
					DoHelpWeapons()
				if event.key == pygame.K_KP4 or event.key == pygame.K_4:
					DoHelpEnemies()
				if event.key == pygame.K_KP5 or event.key == pygame.K_5:
					DoHelpRepair()
				if event.key == pygame.K_KP6 or event.key == pygame.K_6:
					DoHelpNextLevel()
				if event.key == pygame.K_KP7 or event.key == pygame.K_7:
					DoHelpSounds()
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
					Selection=False

	return

def DoHelpPurpose():
	Status = myfont.render('Press enter', False, yellow)		
	text1 = myfont.render('You will appear on the edge of a field of 200x200 positions', False, green)
	text2 = myfont.render('Your goal is to kill enough enemies so the wormhole opens', False, green)
	text3 = myfont.render('Once that happens the location of the wormhole is shown upper left', False, green)
	text4 = myfont.render('All locations in-game are shown in x and y coordinates', False, green)
	text5 = myfont.render('You will have three actions before the enemies begin their actions', False, green)
	text6 = myfont.render('After that your round of actions begins again, unless you died', False, green)
	text7 = myfont.render('You may move, fire your laser or fire a missile in any combination', False, green)

	screen.blit(Galaxy,(0,0))
	screen.blit(text1,(0,0))
	screen.blit(text2,(0,50))
	screen.blit(text3,(0,100))
	screen.blit(text4,(0,150))
	screen.blit(text5,(0,200))
	screen.blit(text6,(0,250))
	screen.blit(text7,(0,300))

	screen.blit(Status,(0,980))
	pygame.display.flip()
	wait()
	return

def DoHelpMovement():
	Status = myfont.render('Press enter', False, yellow)		
	text1 = myfont.render('To move your ship you press a number on your numpad', False, green)
	text2 = myfont.render('2 for down, 8 for up, 4 for left, 6 for right, diagonal is also possible', False, green)
	text3 = myfont.render('You will move in a straight line, distance is set ', False, green)
	text4 = myfont.render('by + and - on your numpad', False, green)
	text5 = myfont.render('5 on your numpad will end your turn, after that the enemies will move', False, green)

	screen.blit(Galaxy,(0,0))
	screen.blit(Numpad,(400,0))
	screen.blit(text1,(0,300))
	screen.blit(text2,(0,350))
	screen.blit(text3,(0,400))
	screen.blit(text4,(0,450))
	screen.blit(text5,(0,500))

	screen.blit(Status,(0,980))
	pygame.display.flip()
	wait()

	return

def DoHelpWeapons():
	Status = myfont.render('Press enter', False, yellow)		
	text1 = myfont.render('Your ship has a laser (with unlimited ammo, range 4) and can fire missiles (limited ammo, range 20).', False, green)
	text2 = myfont.render('To fire the laser, press /, the top left screen will appear where you can select your target', False, green)
	text3 = myfont.render('To fire a missile, press 0 on the numpad, the top right screen will appear where you can select your target', False, green)

	screen.blit(Galaxy,(0,0))
	screen.blit(LaserScreen,(0,0))
	screen.blit(MissileScreen,(600,0))

	screen.blit(text1,(0,500))
	screen.blit(text2,(0,550))
	screen.blit(text3,(0,600))

	screen.blit(Status,(0,980))
	pygame.display.flip()
	wait()
	return

def DoHelpEnemies():
	Status = myfont.render('Press enter', False, yellow)		
	text1 = myfont.render('At the bottom of your screen the location of the closest enemy will be shown', False, green)
	text2 = myfont.render('If you want to know more about this enemy you can press * (or del for the most dangerous enemy)', False, green)
	text3 = myfont.render('Your ship also comes equipped with a local scanner (end) which will show the enemies in range', False, green)

	screen.blit(Galaxy,(0,0))
	screen.blit(EnemyScreen,(0,0))
	screen.blit(RadarExample,(600,0))

	screen.blit(text1,(0,500))
	screen.blit(text2,(0,550))
	screen.blit(text3,(0,600))

	screen.blit(Status,(0,980))
	pygame.display.flip()
	wait()

	return

def DoHelpRepair():
	Status = myfont.render('Press enter', False, yellow)		
	text1 = myfont.render('Apart from the wormhole and enemies, there are two more kinds of objects in game:', False, green)
	text2 = myfont.render('Stars do damage when moved over:', False, green)
	text3 = myfont.render('Red stars do 100 damage', False, green)
	text4 = myfont.render('Yellow stars do 200 damage', False, green)
	text5 = myfont.render('Blue stars do 300 damage', False, green)
	text6 = myfont.render('Next are the asteroids, those repair your ship and supply missiles', False, green)
	text7 = myfont.render('Small asteroids give 100 hull and 2 missiles', False, green)
	text8 = myfont.render('Medium asteroids give 200 hull and 3 missiles', False, green)
	text9 = myfont.render('Large asteroids give 300 hull and 5 missiles', False, green)

	screen.blit(Galaxy,(0,0))
	screen.blit(RedStar,(0,100))
	screen.blit(YellowStar,(0,150))
	screen.blit(BlueStar,(0,200))
	screen.blit(Asteroid,(0,300))
	screen.blit(Asteroid2,(0,350))
	screen.blit(Asteroid3,(0,400))

	screen.blit(text1,(0,0))
	screen.blit(text2,(0,50))
	screen.blit(text3,(50,100))
	screen.blit(text4,(50,150))
	screen.blit(text5,(50,200))
	screen.blit(text6,(0,250))
	screen.blit(text7,(50,300))
	screen.blit(text8,(50,350))
	screen.blit(text9,(50,400))

	screen.blit(Status,(0,980))
	pygame.display.flip()
	wait()

	return

def DoHelpNextLevel():
	Status = myfont.render('Press enter', False, yellow)		
	text1 = myfont.render('As mentioned before you have to kill a certain amount of the enemies in the game for the wormhole to open.', False, green)
	text2 = myfont.render('The percentage of the necessary kills will be shown in the upper left corner.', False, green)
	text3 = myfont.render('Once it reaches 100% the location of the wormhole will be shown, be warned, there might still be enemies', False, green)
	text4 = myfont.render('Closed wormhole', False, green)
	text5 = myfont.render('Opened wormhole', False, green)
	text6 = myfont.render('Once you are on the open wormhole, end your turn with 5, the enemies will move and the next level will start', False, green)

	screen.blit(Galaxy,(0,0))
	screen.blit(Stop,(0,150))
	screen.blit(Wormhole,(0,200))

	screen.blit(text1,(0,0))
	screen.blit(text2,(0,50))
	screen.blit(text3,(0,100))
	screen.blit(text4,(50,150))
	screen.blit(text5,(50,200))
	screen.blit(text6,(0,250))

	screen.blit(Status,(0,980))
	pygame.display.flip()
	wait()

	return

def DoHelpSounds():
	Selection=True
	while Selection:
		Status = myfont.render('Press enter', False, yellow)		
		text1 = myfont.render('1> Missile hit', False, green)
		text2 = myfont.render('2> Explosion (when blown up by missile or crashing into star', False, green)
		text3 = myfont.render('3> Leveling up/ship restored', False, green)
		text4 = myfont.render('4> Eating asteroid (normal)', False, green)
		text5 = myfont.render('5> Moving through star', False, green)
		text6 = myfont.render('6> Laser hit', False, green)
		text7 = myfont.render('7> Wormhole opens', False, green)
		text8 = myfont.render('8> Teleported to next level', False, green)
		text9 = myfont.render('9> Getting hit when severely damaged (player)', False, green)
		text10 = myfont.render('a> Eating asteroid when severely damaged (player)', False, green)
		text11 = myfont.render('b> Eating asteroid when severely damaged (enemy)', False, green)

		screen.blit(Galaxy,(0,0))
		screen.blit(text1,(0,0))
		screen.blit(text2,(0,50))
		screen.blit(text3,(0,100))
		screen.blit(text4,(0,150))
		screen.blit(text5,(0,200))
		screen.blit(text6,(0,250))
		screen.blit(text7,(0,300))
		screen.blit(text8,(0,350))
		screen.blit(text9,(0,400))
		screen.blit(text10,(0,450))
		screen.blit(text11,(0,500))

		screen.blit(Status,(0,980))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP1 or event.key == pygame.K_1:
					Beep.play()
				if event.key == pygame.K_KP2 or event.key == pygame.K_2:
					Blast.play()
				if event.key == pygame.K_KP3 or event.key == pygame.K_3:
					LevelUp.play()
				if event.key == pygame.K_KP4 or event.key == pygame.K_4:
					Eating.play()
				if event.key == pygame.K_KP5 or event.key == pygame.K_5:
					Sizzle.play()
				if event.key == pygame.K_KP6 or event.key == pygame.K_6:
					Laser.play()
				if event.key == pygame.K_KP7 or event.key == pygame.K_7:
					Yay.play()
				if event.key == pygame.K_KP8 or event.key == pygame.K_8:
					Teleport.play()
				if event.key == pygame.K_KP9 or event.key == pygame.K_9:
					Hurt.play()
				if event.key == pygame.K_a:
					Yeah.play()
				if event.key == pygame.K_b:
					Ahh.play()
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
					Selection=False

	return

def LoadGame ():
	global Level
	global PlayerLevel
	global PlayerHull
	global PlayerMissiles
	global Exp
	global SaveCounter

	LevelSave1=int(LoadList[0].rstrip())
	LevelSave2=int(LoadList[5].rstrip())
	LevelSave3=int(LoadList[10].rstrip())
	LevelSave4=int(LoadList[15].rstrip())
	LevelSave5=int(LoadList[20].rstrip())
	LevelSave6=int(LoadList[25].rstrip())

	SLevelSave1=str(LevelSave1)
	SLevelSave2=str(LevelSave2)
	SLevelSave3=str(LevelSave3)
	SLevelSave4=str(LevelSave4)
	SLevelSave5=str(LevelSave5)
	SLevelSave6=str(LevelSave6)

	if LevelSave1==1:
		Save1Status='Save slot 1, new game'
	else:
		Save1Status='Save slot 1, level: '+SLevelSave1+' Ship Level: '+str(LoadList[1].rstrip())+' Hull: '+str(LoadList[2].rstrip())+' Missiles: '+str(LoadList[3].rstrip())
	if LevelSave2==1:
		Save2Status='Save slot 2, new game'
	else:
		Save2Status='Save slot 2, level: '+SLevelSave2+' Ship Level: '+str(LoadList[6].rstrip())+' Hull: '+str(LoadList[7].rstrip())+' Missiles: '+str(LoadList[8].rstrip())
	if LevelSave3==1:
		Save3Status='Save slot 3, new game'
	else:
		Save3Status='Save slot 3, level: '+SLevelSave3+' Ship Level: '+str(LoadList[11].rstrip())+' Hull: '+str(LoadList[12].rstrip())+' Missiles: '+str(LoadList[13].rstrip())
	if LevelSave4==1:
		Save4Status='Save slot 4, new game'
	else:
		Save4Status='Save slot 4, level: '+SLevelSave4+' Ship Level: '+str(LoadList[16].rstrip())+' Hull: '+str(LoadList[17].rstrip())+' Missiles: '+str(LoadList[18].rstrip())
	if LevelSave5==1:
		Save5Status='Save slot 5, new game'
	else:
		Save5Status='Save slot 5, level: '+SLevelSave5+' Ship Level: '+str(LoadList[21].rstrip())+' Hull: '+str(LoadList[22].rstrip())+' Missiles: '+str(LoadList[23].rstrip())
	if LevelSave6==1:
		Save6Status='Save slot 6, new game'
	else:
		Save6Status='Save slot 6, level: '+SLevelSave6+' Ship Level: '+str(LoadList[26].rstrip())+' Hull: '+str(LoadList[27].rstrip())+' Missiles: '+str(LoadList[28].rstrip())

	Save1Text = myfont.render(Save1Status, False, green)
	Save2Text = myfont.render(Save2Status, False, green)
	Save3Text = myfont.render(Save3Status, False, green)
	Save4Text = myfont.render(Save4Status, False, green)
	Save5Text = myfont.render(Save5Status, False, green)
	Save6Text = myfont.render(Save6Status, False, green)
	Status = myfont.render('Select a save slot or press ESC to quit', False, yellow)
	
	screen.blit(Galaxy,(0,0))
	screen.blit(Save1Text,(0,0))
	screen.blit(Save2Text,(0,50))
	screen.blit(Save3Text,(0,100))
	screen.blit(Save4Text,(0,150))
	screen.blit(Save5Text,(0,200))
	screen.blit(Save6Text,(0,250))
	screen.blit(Status,(0,980))

	pygame.display.flip()

	Selection=True
	while Selection:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP1 or event.key == pygame.K_1:
					SaveCounter=0
					Level=int(LoadList[0].rstrip())
					PlayerLevel=int(LoadList[1].rstrip())
					PlayerHull=int(LoadList[2].rstrip())
					PlayerMissiles=int(LoadList[3].rstrip())
					Exp[0]=LoadList[4].rstrip()
					Selection=False
				if event.key == pygame.K_KP2 or event.key == pygame.K_2:
					SaveCounter=5
					Level=int(LoadList[5].rstrip())
					PlayerLevel=int(LoadList[6].rstrip())
					PlayerHull=int(LoadList[7].rstrip())
					PlayerMissiles=int(LoadList[8].rstrip())
					Exp[0]=LoadList[9].rstrip()
					Selection=False
				if event.key == pygame.K_KP3 or event.key == pygame.K_3:
					SaveCounter=10
					Level=int(LoadList[10].rstrip())
					PlayerLevel=int(LoadList[11].rstrip())
					PlayerHull=int(LoadList[12].rstrip())
					PlayerMissiles=int(LoadList[13].rstrip())
					Exp[0]=LoadList[14].rstrip()
					Selection=False
				if event.key == pygame.K_KP4 or event.key == pygame.K_4:
					SaveCounter=15
					Level=int(LoadList[15].rstrip())
					PlayerLevel=int(LoadList[16].rstrip())
					PlayerHull=int(LoadList[17].rstrip())
					PlayerMissiles=int(LoadList[18].rstrip())
					Exp[0]=LoadList[19].rstrip()
					Selection=False
				if event.key == pygame.K_KP5 or event.key == pygame.K_5:
					SaveCounter=20
					Level=int(LoadList[20].rstrip())
					PlayerLevel=int(LoadList[21].rstrip())
					PlayerHull=int(LoadList[22].rstrip())
					PlayerMissiles=int(LoadList[23].rstrip())
					Exp[0]=LoadList[24].rstrip()
					Selection=False
				if event.key == pygame.K_KP6 or event.key == pygame.K_6:
					SaveCounter=25
					Level=int(LoadList[25].rstrip())
					PlayerLevel=int(LoadList[26].rstrip())
					PlayerHull=int(LoadList[27].rstrip())
					PlayerMissiles=int(LoadList[28].rstrip())
					Exp[0]=LoadList[29].rstrip()
					Selection=False
				if event.key == pygame.K_ESCAPE:
					sys.exit()

	return

DoHelp()	
LoadGame()
Action=0
ScreenRange=list()
MissileTargetList=list()
LaserTargetList=list()


def GetScreenItem (ObjectImage):
	if ObjectImage == 'RedStar':
		ScreenItem=RedStar
	elif ObjectImage == 'YellowStar':
		ScreenItem=YellowStar
	elif ObjectImage == 'BlueStar':
		ScreenItem=BlueStar
	elif ObjectImage == 'Asteroid':
		ScreenItem=Asteroid
	elif ObjectImage == 'Asteroid2':
		ScreenItem=Asteroid2
	elif ObjectImage == 'Asteroid3':
		ScreenItem=Asteroid3
	elif ObjectImage == 'Wormhole':
		ScreenItem=Wormhole
	elif ObjectImage == 'Bomb':
		ScreenItem=Bomb
	elif ObjectImage == 'Stop':
		ScreenItem=Stop
	elif ObjectImage == 'Happy':
		ScreenItem=Happy
	elif ObjectImage == 'Sad':
		ScreenItem=Sad
	elif ObjectImage == 'Explosion':
		ScreenItem=Explosion
	elif ObjectImage == 'Drone\n':
		ScreenItem=Drone
	elif ObjectImage == 'Drone2\n':
		ScreenItem=Drone2
	elif ObjectImage == 'Drone3\n':
		ScreenItem=Drone3
	elif ObjectImage == 'Drone4\n':
		ScreenItem=Drone4
	elif ObjectImage == 'Drone5\n':
		ScreenItem=Drone5
	elif ObjectImage == 'Drone6\n':
		ScreenItem=Drone6
	elif ObjectImage == 'Drone7\n':
		ScreenItem=Drone7
	elif ObjectImage == 'Drone8\n':
		ScreenItem=Drone8
	elif ObjectImage == 'Drone9\n':
		ScreenItem=Drone9
	elif ObjectImage == 'Drone10\n':
		ScreenItem=Drone10
	elif ObjectImage == 'Drone11\n':
		ScreenItem=Drone11
	elif ObjectImage == 'Drone12\n':
		ScreenItem=Drone12
	elif ObjectImage == 'Drone13\n':
		ScreenItem=Drone13
	elif ObjectImage == 'Drone14\n':
		ScreenItem=Drone14
	elif ObjectImage == 'Drone15\n':
		ScreenItem=Drone15
	elif ObjectImage == 'Interceptor\n':
		ScreenItem=Interceptor
	elif ObjectImage == 'Interceptor2\n':
		ScreenItem=Interceptor2
	elif ObjectImage == 'Interceptor3\n':
		ScreenItem=Interceptor3
	elif ObjectImage == 'Interceptor4\n':
		ScreenItem=Interceptor4
	elif ObjectImage == 'Interceptor5\n':
		ScreenItem=Interceptor5
	elif ObjectImage == 'Interceptor6\n':
		ScreenItem=Interceptor6
	elif ObjectImage == 'Interceptor7\n':
		ScreenItem=Interceptor7
	elif ObjectImage == 'Interceptor8\n':
		ScreenItem=Interceptor8
	elif ObjectImage == 'Interceptor9\n':
		ScreenItem=Interceptor9
	elif ObjectImage == 'Interceptor10\n':
		ScreenItem=Interceptor10
	elif ObjectImage == 'Frigat\n':
		ScreenItem=Frigat
	elif ObjectImage == 'Frigat2\n':
		ScreenItem=Frigat2
	elif ObjectImage == 'Frigat3\n':
		ScreenItem=Frigat3
	elif ObjectImage == 'Frigat4\n':
		ScreenItem=Frigat4
	elif ObjectImage == 'Frigat5\n':
		ScreenItem=Frigat5
	elif ObjectImage == 'Frigat6\n':
		ScreenItem=Frigat6
	elif ObjectImage == 'MissilePlatform\n':
		ScreenItem=MissilePlatform
	elif ObjectImage == 'MissilePlatform2\n':
		ScreenItem=MissilePlatform2
	elif ObjectImage == 'Liberator\n':
		ScreenItem=Liberator
	elif ObjectImage == 'Teleporter\n':
		ScreenItem=Teleporter
	elif ObjectImage == 'Eye\n':
		ScreenItem=Eye
	elif ObjectImage == 'Leech\n':
		ScreenItem=Leech
	elif ObjectImage == 'Ramjet\n':
		ScreenItem=Ramjet
	elif ObjectImage == 'Mothership\n':
		ScreenItem=Mothership
	elif ObjectImage == 'HunterDrone\n':
		ScreenItem=HunterDrone

	return (ScreenItem)


def VisualScan (Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY):
	del ScreenRange[:]
	# Get items in range of screen
	# First stars
	Counter=0
	MaxCounter=len(Stars)
	while Counter < MaxCounter:
		StarType=Stars[Counter]
		StarX=Stars[Counter+1]
		StarY=Stars[Counter+2]
		XDiff=StarX-PlayerX
		YDiff=StarY-PlayerY
		if (-10 <= XDiff) and ( XDiff <= 10) and (-10 <= YDiff) and (YDiff <= 10):
			if StarType==1:
				StarImage='RedStar'
			elif StarType==2:
				StarImage='YellowStar'
			else:
				StarImage='BlueStar'
			ScreenRange.append(StarImage)
			ScreenRange.append(XDiff)
			ScreenRange.append(YDiff)
		Counter=Counter+3
	
	# Then asteroids
	Counter=0
	MaxCounter=len(Asteroids)
	while Counter < MaxCounter:
		AsteroidsType=int(Asteroids[Counter])
		if AsteroidsType==1:
			AsteroidsImage='Asteroid'
		elif AsteroidsType==2:
			AsteroidsImage='Asteroid2'
		if AsteroidsType==3:
			AsteroidsImage='Asteroid3'
		AsteroidsX=Asteroids[Counter+1]
		AsteroidsY=Asteroids[Counter+2]
		XDiff=AsteroidsX-PlayerX
		YDiff=AsteroidsY-PlayerY
		if (-10 <= XDiff) and ( XDiff <= 10) and (-10 <= YDiff) and (YDiff <= 10):
			ScreenRange.append(AsteroidsImage)
			ScreenRange.append(XDiff)
			ScreenRange.append(YDiff)
		Counter=Counter+3
		
	# Then enemies
	Counter=0
	MaxCounter=len(Enemies)
	while Counter < MaxCounter:
		EnemyType=Enemies[Counter+2]
		EnemyX=int(Enemies[Counter+10])
		EnemyY=int(Enemies[Counter+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if (-10 <= XDiff) and ( XDiff <= 10) and (-10 <= YDiff) and (YDiff <= 10):
			ScreenRange.append(EnemyType)
			ScreenRange.append(XDiff)
			ScreenRange.append(YDiff)
		Counter=Counter+13
	
	# Then Wormhole
	XDiff=WormholeX-PlayerX
	YDiff=WormholeY-PlayerY
	if (-10 <= XDiff) and ( XDiff <= 10) and (-10 <= YDiff) and (YDiff <= 10):
		if EnemyKills < EnemyKillTarget:
			ScreenRange.append('Stop')
		else:
			ScreenRange.append('Wormhole')
		ScreenRange.append(XDiff)
		ScreenRange.append(YDiff)

	XDiff=MissilePosX-PlayerX
	YDiff=MissilePosY-PlayerY
	ScreenRange.append('Bomb')
	ScreenRange.append(XDiff)
	ScreenRange.append(YDiff)

	XDiff=ExplosionX-PlayerX
	YDiff=ExplosionY-PlayerY
	ScreenRange.append('Explosion')
	ScreenRange.append(XDiff)
	ScreenRange.append(YDiff)
	
	return(ScreenRange)

def StarDetect (Stars, PlayerX, PlayerY):
	Counter=0
	CrashStar=0
	MaxCounter=len(Stars)
	while Counter < MaxCounter:
		StarType=Stars[Counter]
		StarX=Stars[Counter+1]
		StarY=Stars[Counter+2]
		if (PlayerX == StarX) and (PlayerY == StarY):
			CrashStar=StarType
		Counter=Counter+3
	return(CrashStar)

def ScanClosestAsteroid (PlayerX, PlayerY):
	Counter=0
	SetAsteroidDistance=20000000
	AsteroidText=''
	ShowX=0
	ShowY=0
	MaxCounter=len(Asteroids)
	while Counter < MaxCounter:
		AsteroidType=int(Asteroids[Counter])
		AsteroidX=int(Asteroids[Counter+1])
		AsteroidY=int(Asteroids[Counter+2])
		Xdiff=AsteroidX-PlayerX
		Ydiff=AsteroidY-PlayerY
		if (Xdiff==0) and (Ydiff==0):
			AsteroidDistance=0
			if AsteroidType==1:
				AsteroidName='Small asteroid at: '
			elif AsteroidType==2:
				AsteroidName='Medium asteroid at: '
			elif AsteroidType==3:
				AsteroidName='Large asteroid at: '
			ShowX=Xdiff
			ShowY=Ydiff
		else:
			AsteroidDistance=math.sqrt((Xdiff**2+Ydiff**2))
			if AsteroidDistance < SetAsteroidDistance:
				SetAsteroidDistance=AsteroidDistance
				if AsteroidType==1:
					AsteroidName='Small asteroid at: '
				elif AsteroidType==2:
					AsteroidName='Medium asteroid at: '
				elif AsteroidType==3:
					AsteroidName='Large asteroid at: '
				ShowX=Xdiff
				ShowY=Ydiff
				AsteroidText=AsteroidName+' x'+str(ShowX)+' y'+str(ShowY)
		Counter=Counter+3

	return (AsteroidText)

def SetStatus():
	global Exp
	global ExpNeeded
	global Action
	SAction=str(Action+1)
	ExpInt=int(Exp[0])
	NeededInt=int(ExpNeeded)
	PlayerLaserDamage=str(PlayerLevel*10)
	PlayerMissileDamage=str(PlayerLevel*15)
	if PlayerLevel < 20:
		Levelup=' Level up: '
	else:
		Levelup=' Healing: '
	LevelUpProgress=str(int((ExpInt/NeededInt)*100))
	Status='Level: '+str(Level)+' Ship Level: '+str(PlayerLevel)+' Dam: '+PlayerLaserDamage+'-'+PlayerMissileDamage+' Speed: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '+str(int(PlayerHull))+'/'+\
str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+Levelup+LevelUpProgress+'% move: '+SAction+'/3'
	return (Status)

def DoScreen (ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus):
	WXdiff=100-PlayerX
	WYdiff=100-PlayerY
	if len(Enemies)>0:	
		ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
		EnemyX=int(Enemies[ClosestEnemy+10])
		EnemyY=int(Enemies[ClosestEnemy+11])
	global WormholeOpenPlayed
	PlayerHealth=str(int((PlayerHull/(PlayerLevel*100))*100))+'%'
	if EnemyKills >= EnemyKillTarget:
		WormholeText='Wormhole open at: x'+str(WXdiff)+' y'+str(WYdiff)
	else:
		WormholeText='Current levelmap progress: '+str(int((EnemyKills/EnemyKillTarget)*100))+'%'
	if PlayerHull > PlayerLevel*50 and PlayerMissiles >0:
		StatusColor=green
		AsteroidText='Ship hull '+PlayerHealth
	else:
		if PlayerHull > PlayerLevel*50:
			StatusColor=green
		else:
			StatusColor=red
		if len(Asteroids) > 0:
			AsteroidText=ScanClosestAsteroid(PlayerX, PlayerY)
		else:
			AsteroidText='No asteroids left'
	if len(Enemies)>0:
		NumberOfEnemies=str(int(len(Enemies)/13))
		EnemyX=int(Enemies[ClosestEnemy+10])
		EnemyY=int(Enemies[ClosestEnemy+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			SafetyText=myfont.render('Danger', False, red)
		else:
			SafetyText=myfont.render('Safe', False, green)
	else:
		NumberOfEnemies='0'
		SafetyText=myfont.render('Safe', False, green)
	EnemyText='Enemies: '+NumberOfEnemies
	textsurface3 = myfont.render(WormholeText, False, StatusColor)
	textsurface4 = myfont.render(AsteroidText, False, StatusColor)
	textsurface5 = myfont.render(EnemyText, False, StatusColor)
	textsurface = myfont.render(Status, False, StatusColor)
	HelpText = myfont.render('Press h for help', False, green)
	if PlayerHull > PlayerLevel*50:
		PlayerImage=Happy
	elif PlayerHull > 0:
		PlayerImage=Sad
	else:
		PlayerImage=Explosion
#	pygame.display.set_icon(JGrid)
#	pygame.display.set_caption('Jumpwar')
#	Width=int(1000)
#	Heigth=int(1000)
#	screen = pygame.display.set_mode((Width, Heigth))
	screen.blit(JGrid, (0,0))
	screen.blit(PlayerImage, (475,475))
	pygame.display.flip()
	Counter=0
	MaxCounter=len(ScreenRange)
	while Counter < MaxCounter:
		ObjectImage=ScreenRange[Counter]
		ScreenItem=GetScreenItem(ObjectImage)
		XDiff=ScreenRange[Counter+1]
		YDiff=ScreenRange[Counter+2]
		ScreenX=(XDiff+10)*47.5
		YConvert=YDiff*-1
		ScreenY=(YConvert+10)*47.5
		screen.blit(ScreenItem, (ScreenX,ScreenY))
		Counter=Counter+3
	screen.blit(textsurface3,(0,0))
	screen.blit(textsurface4,(0,20))
	screen.blit(textsurface5,(800,0))
	screen.blit(SafetyText,(800,20))
	screen.blit(textsurface,(0,960))
	screen.blit(EnemyStatus,(0,940))
	screen.blit(HelpText,(440,0))
	if EnemyKills >= EnemyKillTarget:
		if WormholeOpenPlayed==0:
			screen.blit(GalaxySmall,(300,300))
			textWormhole='Wormhole now open'
			text01 = myfont.render(textWormhole, False, (255, 255, 0))
			textEnter='Press enter'
			text02 = myfont.render(textEnter, False, (255, 255, 0))

			screen.blit(text01,(300,300))
			screen.blit(text02,(300,680))
			screen.blit(Wormhole,(475,475))
			Yay.play()
			WormholeOpenPlayed=1
			pygame.display.flip()
			wait()

	pygame.display.flip()
	return

def DoEnemyInfo (Enemies, PlayerX, PlayerY, ClosestEnemy):
	if len(Enemies)>0:
		EnemyLevel=int(Enemies[ClosestEnemy])
		EnemyName=str(Enemies[ClosestEnemy+1]).rstrip()
		EnemyDamageLaser=int(Enemies[ClosestEnemy+3])
		EnemyDamageMissile=int(EnemyDamageLaser*1.5)
	
#		EnemyArmor=EnemyLevel*100
#		PlayerDamage=PlayerLevel*15
#		if EnemyArmor >= PlayerDamage*5:
#			Armor='Very heavy'
#		elif EnemyArmor >= PlayerDamage*4:
#			Armor='Heavy'
#		elif EnemyArmor >= PlayerDamage*3:
#			Armor='Medium'
#		elif EnemyArmor >= PlayerDamage*2:
#			Armor='Light'
#		else:
#			Armor='Very light'
	
		EnemyDamage=(EnemyDamageMissile/PlayerHull)
		if EnemyDamage < 0.1:
			EnemyDanger='Very low'
			EnemyColor=green
		elif EnemyDamage < 0.2:
			EnemyDanger='Low'
			EnemyColor=light_grey
		elif EnemyDamage < 0.3:
			EnemyDanger='Medium'
			EnemyColor=yellow
		elif EnemyDamage <= 0.4:
			EnemyDanger='High'
			EnemyColor=orange
		elif EnemyDamage > 0.4:
			EnemyDanger='Very high'
			EnemyColor=red

		EnemySpeed=str(Enemies[ClosestEnemy+4]).rstrip()
		EnemyScan=int(Enemies[ClosestEnemy+5])
		EnemyHull=int(Enemies[ClosestEnemy+6])
		EnemyMissiles=str(Enemies[ClosestEnemy+7]).rstrip()
		EnemyX=int(Enemies[ClosestEnemy+10])
		EnemyY=int(Enemies[ClosestEnemy+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		PDist=PlayerDistance(EnemyX, EnemyY, PlayerX, PlayerY)
		Mood=str(Enemies[ClosestEnemy+12]).rstrip()
		ObjectImage=str(Enemies[ClosestEnemy+2])
		EnemyHealth=str(int((EnemyHull/(EnemyLevel*100))*100))+'%'
		ScreenItem=GetScreenItem(ObjectImage)
	else:
		EnemyLevel='NVT'
		EnemyName='Wormhole'
		EnemyDamageLaser='NVT'
		EnemySpeed='NVT'
		EnemyScan='NVT'
		EnemyHull='NVT'
		EnemyMissiles='NVT'
		EnemyX='NVT'
		EnemyY='NVT'
		XDiff=100-PlayerX
		YDiff=100-PlayerY
		Mood='Open'
		ScreenItem=Wormhole
		EnemyHealth='100%'
		EnemyColor=green


	textHeader='Closest Enemy'
	text00 = myfont.render(textHeader, False, EnemyColor)
	textEnemyPic='Enemy         : '
	text01 = myfont.render(textEnemyPic, False, EnemyColor)
	textEnemyName='Name           : '+EnemyName
	text02 = myfont.render(textEnemyName, False, EnemyColor)
	textEnemyDamage='Damage       : '+str(EnemyDamageLaser)+'-'+str(EnemyDamageMissile)
	text03 = myfont.render(textEnemyDamage, False, EnemyColor)
	textEnemySpeed='Speed          : '+EnemySpeed
	text04 = myfont.render(textEnemySpeed, False, EnemyColor)
	textEnemyScan='Scan Range: '+str(EnemyScan)
	text05 = myfont.render(textEnemyScan, False, EnemyColor)
	textEnemyHull='Hull              : '+str(EnemyHull)
	text06 = myfont.render(textEnemyHull, False, EnemyColor)
	textEnemyMissiles='Missiles       : '+EnemyMissiles
	text07 = myfont.render(textEnemyMissiles, False, EnemyColor)
	textEnemyPosition='Position       : x'+str(XDiff)+' y'+str(YDiff)
	text08 = myfont.render(textEnemyPosition, False, EnemyColor)
	textEnemyMood='Status          : '+Mood
	text09 = myfont.render(textEnemyMood, False, EnemyColor)
	text10 = myfont.render('Press enter', False, yellow)

	Width=int(1000)
	Heigth=int(1000)

	Status=SetStatus()

	DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

	screen.blit(GalaxySmall,(300,300))
	screen.blit(text00,(300,320))
	screen.blit(text01,(300,380))
	screen.blit(ScreenItem, (450,370))

	screen.blit(text02,(300,420))
	screen.blit(text03,(300,440))
	screen.blit(text04,(300,460))
	screen.blit(text05,(300,480))
	screen.blit(text06,(300,500))
	screen.blit(text07,(300,520))
	screen.blit(text08,(300,540))
	screen.blit(text09,(300,560))
	screen.blit(text10,(300,580))
	pygame.display.flip()
	wait()
	return

def DoEnemyXL (Enemies, PlayerX, PlayerY):
	if len(Enemies)>0:
		EnemyXL=GetEnemyXL(Enemies)
		EnemyLevel=int(Enemies[EnemyXL])
		EnemyName=str(Enemies[EnemyXL+1]).rstrip()
		EnemyDamageLaser=int(Enemies[EnemyXL+3])
		EnemyDamageMissile=int(EnemyDamageLaser*1.5)
	
#		EnemyArmor=EnemyLevel*100
#		PlayerDamage=PlayerLevel*15
#		if EnemyArmor >= PlayerDamage*5:
#			Armor='Very heavy'
#		elif EnemyArmor >= PlayerDamage*4:
#			Armor='Heavy'
#		elif EnemyArmor >= PlayerDamage*3:
#			Armor='Medium'
#		elif EnemyArmor >= PlayerDamage*2:
#			Armor='Light'
#		else:
#			Armor='Very light'
	
		EnemyDamage=(EnemyDamageMissile/PlayerHull)
		if EnemyDamage < 0.1:
			EnemyDanger='Very low'
			EnemyColor=green
		elif EnemyDamage < 0.2:
			EnemyDanger='Low'
			EnemyColor=light_grey
		elif EnemyDamage < 0.3:
			EnemyDanger='Medium'
			EnemyColor=yellow
		elif EnemyDamage <= 0.4:
			EnemyDanger='High'
			EnemyColor=orange
		elif EnemyDamage > 0.4:
			EnemyDanger='Very high'
			EnemyColor=red

		EnemySpeed=str(Enemies[EnemyXL+4]).rstrip()
		EnemyScan=int(Enemies[EnemyXL+5])
		EnemyHull=int(Enemies[EnemyXL+6])
		EnemyMissiles=str(Enemies[EnemyXL+7]).rstrip()
		EnemyX=int(Enemies[EnemyXL+10])
		EnemyY=int(Enemies[EnemyXL+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		PDist=PlayerDistance(EnemyX, EnemyY, PlayerX, PlayerY)
		Mood=str(Enemies[EnemyXL+12]).rstrip()
		ObjectImage=str(Enemies[EnemyXL+2])
		EnemyHealth=str(int((EnemyHull/(EnemyLevel*100))*100))+'%'
		ScreenItem=GetScreenItem(ObjectImage)
	else:
		EnemyLevel='NVT'
		EnemyName='Wormhole'
		EnemyDamageLaser='NVT'
		EnemySpeed='NVT'
		EnemyScan='NVT'
		EnemyHull='NVT'
		EnemyMissiles='NVT'
		EnemyX='NVT'
		EnemyY='NVT'
		XDiff=100-PlayerX
		YDiff=100-PlayerY
		Mood='Open'
		ScreenItem=Wormhole
		EnemyHealth='100%'
		EnemyColor=green

	textEnemyXL='Most dangerous enemy'
	text00 = myfont.render(textEnemyXL, False, EnemyColor)
	textEnemyPic='Enemy         : '
	text01 = myfont.render(textEnemyPic, False, EnemyColor)
	textEnemyName='Name           : '+EnemyName
	text02 = myfont.render(textEnemyName, False, EnemyColor)
	textEnemyDamage='Damage       : '+str(EnemyDamageLaser)+'-'+str(EnemyDamageMissile)
	text03 = myfont.render(textEnemyDamage, False, EnemyColor)
	textEnemySpeed='Speed          : '+EnemySpeed
	text04 = myfont.render(textEnemySpeed, False, EnemyColor)
	textEnemyScan='Scan Range: '+str(EnemyScan)
	text05 = myfont.render(textEnemyScan, False, EnemyColor)
	textEnemyHull='Hull              : '+str(EnemyHull)
	text06 = myfont.render(textEnemyHull, False, EnemyColor)
	textEnemyMissiles='Missiles       : '+EnemyMissiles
	text07 = myfont.render(textEnemyMissiles, False, EnemyColor)
	textEnemyPosition='Position       : x'+str(XDiff)+' y'+str(YDiff)
	text08 = myfont.render(textEnemyPosition, False, EnemyColor)
	textEnemyMood='Status          : '+Mood
	text09 = myfont.render(textEnemyMood, False, EnemyColor)
	text10 = myfont.render('Press enter', False, yellow)

	Width=int(1000)
	Heigth=int(1000)

	Status=SetStatus()

	DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

	screen.blit(GalaxySmall,(300,300))
	screen.blit(text00,(300,320))	
	screen.blit(text01,(300,380))
	screen.blit(ScreenItem, (450,370))

	screen.blit(text02,(300,420))
	screen.blit(text03,(300,440))
	screen.blit(text04,(300,460))
	screen.blit(text05,(300,480))
	screen.blit(text06,(300,500))
	screen.blit(text07,(300,520))
	screen.blit(text08,(300,540))
	screen.blit(text09,(300,560))
	screen.blit(text10,(300,580))
	pygame.display.flip()
	wait()
	return

def NewLevel (Level):
	Status = myfont.render('Press enter to continue - ESC to quit', False, yellow)		
	text1 = myfont.render('Welcome to Level: '+str(Level), False, green)
	Teleportertext = myfont.render('Teleporter will move you all over the map!', False, red)
	Eyetext = myfont.render('Cannot escape the Eye!', False, red)
	Leechtext = myfont.render('Leech will suck you dry!', False, red)
	Ramjettext = myfont.render('None are faster than the Ramjet!', False, red)
	Mothershiptext = myfont.render('Meet the army of the Mothership!', False, red)

#	pygame.display.set_icon(Galaxy)
#	pygame.display.set_caption('Jumpwar')
#	Width=int(1000)
#	Heigth=int(1000)
#	screen = pygame.display.set_mode((Width, Heigth))
	screen.blit(Galaxy, (0,0))
	screen.blit(text1,(300,300))
	if Level==6:
		screen.blit(Teleportertext,(300,350))
	if Level==12:
		screen.blit(Eyetext,(300,350))
	if Level==18:
		screen.blit(Leechtext,(300,350))
	if Level==24:
		screen.blit(Ramjettext,(300,350))
	if Level==30:
		screen.blit(Mothershiptext,(300,350))

	screen.blit(Status,(0,980))
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
	                		return
				elif event.key == pygame.K_ESCAPE:
					sys.exit()
	return

def DoVictory ():
	Victory.play()
	Status = myfont.render('Press enter', False, (255, 255, 0))		
	text1 = myfont.render('Congratulations on beating Jumpwar!', False, (255, 255, 0))

#	pygame.display.set_icon(Galaxy)
#	pygame.display.set_caption('Jumpwar')
#	Width=int(1000)
#	Heigth=int(1000)
#	screen = pygame.display.set_mode((Width, Heigth))
	screen.blit(Galaxy, (0,0))
	screen.blit(text1,(300,300))
	screen.blit(Status,(0,980))
	pygame.display.flip()
	wait()
	return


def ScanEnemies (Enemies, PlayerX, PlayerY, Radar, ScanEnemy):
	Counter=0
	SetEnemyDistance=20000000
	MaxCounter=len(Enemies)
	while Counter < MaxCounter:
		EnemyLevel=int(Enemies[Counter])
		EnemyName=Enemies[Counter+1]
		EnemyHealth=Enemies[Counter+6]
		EnemyX=int(Enemies[Counter+10])
		EnemyY=int(Enemies[Counter+11])
		Xdiff=EnemyX-PlayerX
		Ydiff=EnemyY-PlayerY
		if (Xdiff==0) and (Ydiff==0):
			EnemyDistance=0
		else:
			EnemyDistance=math.sqrt((Xdiff**2+Ydiff**2))
		if EnemyDistance < SetEnemyDistance:
			SetEnemyDistance=EnemyDistance
			ScanEnemy=Counter
		Counter=Counter+13
	return (ScanEnemy)

def GetEnemyXL (Enemies):
	Counter=0
	SetEnemyDanger=0
	MaxCounter=len(Enemies)
	while Counter < MaxCounter:
		EnemyLevel=int(Enemies[Counter])
		EnemyName=Enemies[Counter+1]
		EnemyDamageLaser=int(Enemies[Counter+3])
		EnemySpeed=int(Enemies[Counter+4])
		EnemyMissiles=int(Enemies[Counter+8])
		EnemyScan=int(Enemies[Counter+5])
		EnemyDef=int(Enemies[Counter+8])
		EnemyHealth=int(Enemies[Counter+6])
		EnemyX=int(Enemies[Counter+10])
		EnemyY=int(Enemies[Counter+11])
		Xdiff=EnemyX-PlayerX
		Ydiff=EnemyY-PlayerY
		EnemyDanger=int(((EnemyDamageLaser/10)+EnemySpeed+EnemyLevel+EnemyMissiles)/4)
		if EnemyDanger >= SetEnemyDanger:
			SetEnemyDanger=EnemyDanger
			EnemyXL=Counter
		Counter=Counter+13
	return (EnemyXL)

def CollectEnemies (Enemies,CollectedEnemies, PlayerX, PlayerY):
	if len(Enemies)>0:
		Counter=len(Enemies)-13
		CounterCollected=0
		PlayerScan=PlayerLevel*2
		if PlayerScan < 20:
			PlayerScan=20
		while Counter >= 0:
			if CounterCollected > 6:
				break
			EnemyX=int(Enemies[Counter+10])
			EnemyY=int(Enemies[Counter+11])
			XDiff=EnemyX-PlayerX
			YDiff=EnemyY-PlayerY
			if ((-1*PlayerScan) <= XDiff) and ( XDiff <= PlayerScan) and ((-1*PlayerScan) <= YDiff) and (YDiff <= PlayerScan):
				CollectedEnemies[CounterCollected]=Counter
				CounterCollected=CounterCollected+1
			Counter=Counter-13
	return (CollectedEnemies)

def DoEnemyList (Enemies, CollectedEnemies, PlayerX, PlayerY):
	CollectEnemies(Enemies,CollectedEnemies, PlayerX, PlayerY)
	screen.blit(RadarScreen,(300,300))
	text10 = myfont.render('Press enter', False, yellow)
	if not CollectedEnemies[0]==None:
		ObjectImage=Enemies[CollectedEnemies[0]+2]
		ScreenItem=GetScreenItem(ObjectImage)
		screen.blit(ScreenItem,(300,300))
		EnemyX=int(Enemies[CollectedEnemies[0]+10])
		EnemyY=int(Enemies[CollectedEnemies[0]+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			Lock=' LOCK'
		else:
			Lock=''
		Mood=str(Enemies[CollectedEnemies[0]+12]).rstrip()
		Pos='x'+str(XDiff)+' y'+str(YDiff)+' '
		EnemyHealth=str(Enemies[CollectedEnemies[0]+6]).rstrip()
		Text=Pos+EnemyHealth+' '+Mood+Lock
		EnemyText=myfont.render(Text, False, yellow)
		screen.blit(EnemyText,(350,300))
	if not CollectedEnemies[1]==None:
		ObjectImage=Enemies[CollectedEnemies[1]+2]
		ScreenItem=GetScreenItem(ObjectImage)
		screen.blit(ScreenItem,(300,350))
		EnemyX=int(Enemies[CollectedEnemies[1]+10])
		EnemyY=int(Enemies[CollectedEnemies[1]+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			Lock=' LOCK'
		else:
			Lock=''
		Mood=str(Enemies[CollectedEnemies[1]+12]).rstrip()
		Pos='x'+str(XDiff)+' y'+str(YDiff)+' '
		EnemyHealth=str(Enemies[CollectedEnemies[1]+6]).rstrip()
		Text=Pos+EnemyHealth+' '+Mood+Lock
		EnemyText=myfont.render(Text, False, yellow)
		screen.blit(EnemyText,(350,350))
	if not CollectedEnemies[2]==None:
		ObjectImage=Enemies[CollectedEnemies[2]+2]
		ScreenItem=GetScreenItem(ObjectImage)
		screen.blit(ScreenItem,(300,400))
		EnemyX=int(Enemies[CollectedEnemies[2]+10])
		EnemyY=int(Enemies[CollectedEnemies[2]+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			Lock=' LOCK'
		else:
			Lock=''
		Mood=str(Enemies[CollectedEnemies[2]+12]).rstrip()
		Pos='x'+str(XDiff)+' y'+str(YDiff)+' '
		EnemyHealth=str(Enemies[CollectedEnemies[2]+6]).rstrip()
		Text=Pos+EnemyHealth+' '+Mood+Lock
		EnemyText=myfont.render(Text, False, yellow)
		screen.blit(EnemyText,(350,400))
	if not CollectedEnemies[3]==None:
		ObjectImage=Enemies[CollectedEnemies[3]+2]
		ScreenItem=GetScreenItem(ObjectImage)
		screen.blit(ScreenItem,(300,450))
		EnemyX=int(Enemies[CollectedEnemies[3]+10])
		EnemyY=int(Enemies[CollectedEnemies[3]+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			Lock=' LOCK'
		else:
			Lock=''
		Mood=str(Enemies[CollectedEnemies[3]+12]).rstrip()
		Pos='x'+str(XDiff)+' y'+str(YDiff)+' '
		EnemyHealth=str(Enemies[CollectedEnemies[3]+6]).rstrip()
		Text=Pos+EnemyHealth+' '+Mood+Lock
		EnemyText=myfont.render(Text, False, yellow)
		screen.blit(EnemyText,(350,450))
	if not CollectedEnemies[4]==None:
		ObjectImage=Enemies[CollectedEnemies[4]+2]
		ScreenItem=GetScreenItem(ObjectImage)
		screen.blit(ScreenItem,(300,500))
		EnemyX=int(Enemies[CollectedEnemies[4]+10])
		EnemyY=int(Enemies[CollectedEnemies[4]+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			Lock=' LOCK'
		else:
			Lock=''
		Mood=str(Enemies[CollectedEnemies[4]+12]).rstrip()
		Pos='x'+str(XDiff)+' y'+str(YDiff)+' '
		EnemyHealth=str(Enemies[CollectedEnemies[4]+6]).rstrip()
		Text=Pos+EnemyHealth+' '+Mood+Lock
		EnemyText=myfont.render(Text, False, yellow)
		screen.blit(EnemyText,(350,500))
	if not CollectedEnemies[5]==None:
		ObjectImage=Enemies[CollectedEnemies[5]+2]
		ScreenItem=GetScreenItem(ObjectImage)
		screen.blit(ScreenItem,(300,550))
		EnemyX=int(Enemies[CollectedEnemies[5]+10])
		EnemyY=int(Enemies[CollectedEnemies[5]+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			Lock=' LOCK'
		else:
			Lock=''
		Mood=str(Enemies[CollectedEnemies[5]+12]).rstrip()
		Pos='x'+str(XDiff)+' y'+str(YDiff)+' '
		EnemyHealth=str(Enemies[CollectedEnemies[5]+6]).rstrip()
		Text=Pos+EnemyHealth+' '+Mood+Lock
		EnemyText=myfont.render(Text, False, yellow)
		screen.blit(EnemyText,(350,550))
	if not CollectedEnemies[6]==None:
		ObjectImage=Enemies[CollectedEnemies[6]+2]
		ScreenItem=GetScreenItem(ObjectImage)
		screen.blit(ScreenItem,(300,600))
		EnemyX=int(Enemies[CollectedEnemies[6]+10])
		EnemyY=int(Enemies[CollectedEnemies[6]+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			Lock=' LOCK'
		else:
			Lock=''
		Mood=str(Enemies[CollectedEnemies[6]+12]).rstrip()
		Pos='x'+str(XDiff)+' y'+str(YDiff)+' '
		EnemyHealth=str(Enemies[CollectedEnemies[6]+6]).rstrip()
		Text=Pos+EnemyHealth+' '+Mood+Lock
		EnemyText=myfont.render(Text, False, yellow)
		screen.blit(EnemyText,(350,600))
	screen.blit(text10,(300,650))
	pygame.display.flip()
	wait()
	return


def PlayerDistance (EnemyX, EnemyY, PlayerX, PlayerY):
	XDiff=PlayerX-EnemyX
	YDiff=PlayerY-EnemyY
	if (XDiff==0) and (YDiff==0):
		PlayerDist=0
	else:
		PlayerDist=math.sqrt((XDiff**2+YDiff**2))
	return (PlayerDist)

def MissileScan (Enemies, MissileTargetList):
	Counter=0
	NumberofTargets=0
	del MissileTargetList[:]
	MaxCounter=len(Enemies)
	while Counter < MaxCounter:
		EnemyX=int(Enemies[Counter+10])
		EnemyY=int(Enemies[Counter+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			if NumberofTargets < 7:
				MissileTargetList.append(Counter)
				MissileTargetList.append(XDiff)
				MissileTargetList.append(YDiff)
				NumberofTargets=NumberofTargets+1
			else:
				break
		Counter=Counter+13
	return (MissileTargetList)

def LaserScan (Enemies, laserTargetList):
	Counter=0
	NumberofTargets=0
	del LaserTargetList[:]
	MaxCounter=len(Enemies)
	while Counter < MaxCounter:
		EnemyX=int(Enemies[Counter+10])
		EnemyY=int(Enemies[Counter+11])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-4) <= XDiff) and ( XDiff <= 4) and ((-4) <= YDiff) and (YDiff <= 4):
			if NumberofTargets < 7:
				laserTargetList.append(Counter)
				laserTargetList.append(XDiff)
				laserTargetList.append(YDiff)
				NumberofTargets=NumberofTargets+1
			else:
				break
		Counter=Counter+13
	return (laserTargetList)

def SelectLaserEnemy (LaserTargetList, Enemies):
	text10 = myfont.render('Select Laser target or press enter to cancel', False, yellow)

	EnemyOneName='empty'
	EnemyTwoName='empty'
	EnemyThreeName='empty'
	EnemyFourName='empty'
	EnemyFiveName='empty'
	EnemySixName='empty'
	EnemySevenName='empty'

	Loc1=''
	Loc2=''
	Loc3=''
	Loc4=''
	Loc5=''
	Loc6=''
	Loc7=''

	VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
	DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

	screen.blit(LaserBeams,(300,300))
	screen.blit(text10,(300,300))

	FirstEnemy=LaserTargetList[0]
	Loc1=' x'+str(LaserTargetList[1])+' y'+str(LaserTargetList[2])
	EnemyOneName='1: '+Enemies[FirstEnemy+1]+' '+str(Enemies[FirstEnemy+6]).rstrip()+' '+Loc1
	text = myfont.render(EnemyOneName, False, sky_blue)
	screen.blit(text,(300,350))
	ObjectImage=Enemies[FirstEnemy+2]
	ScreenItem=GetScreenItem(ObjectImage)
	screen.blit(ScreenItem,(650,350))

	if len(LaserTargetList) > 3:
		SecondEnemy=LaserTargetList[3]
		Loc2=' x'+str(LaserTargetList[4])+' y'+str(LaserTargetList[5])
		EnemyTwoName='2: '+Enemies[SecondEnemy+1]+' '+str(Enemies[SecondEnemy+6]).rstrip()+' '+Loc2
		text = myfont.render(EnemyTwoName, False, sky_blue)
		screen.blit(text,(300,400))
		ObjectImage=Enemies[SecondEnemy+2]
		ScreenItem=GetScreenItem(ObjectImage)
		screen.blit(ScreenItem,(650,400))

		if len(LaserTargetList) > 6:
			ThirdEnemy=LaserTargetList[6]
			Loc3=' x'+str(LaserTargetList[7])+' y'+str(LaserTargetList[8])
			EnemyThreeName='3: '+Enemies[ThirdEnemy+1]+' '+str(Enemies[ThirdEnemy+6]).rstrip()+' '+Loc3
			text = myfont.render(EnemyThreeName, False, sky_blue)
			screen.blit(text,(300,450))
			ObjectImage=Enemies[ThirdEnemy+2]
			ScreenItem=GetScreenItem(ObjectImage)
			screen.blit(ScreenItem,(650,450))

			if len(LaserTargetList) > 9:
				FourthEnemy=LaserTargetList[9]
				Loc4=' x'+str(LaserTargetList[10])+' y'+str(LaserTargetList[11])
				EnemyFourName='4: '+Enemies[FourthEnemy+1]+' '+str(Enemies[FourthEnemy+6]).rstrip()+' '+Loc4
				text = myfont.render(EnemyFourName, False, sky_blue)
				screen.blit(text,(300,500))
				ObjectImage=Enemies[FourthEnemy+2]
				ScreenItem=GetScreenItem(ObjectImage)
				screen.blit(ScreenItem,(650,500))

				if len(LaserTargetList) > 12:
					FifthEnemy=LaserTargetList[12]
					Loc5=' x'+str(LaserTargetList[13])+' y'+str(LaserTargetList[14])
					EnemyFiveName='5: '+Enemies[FifthEnemy+1]+' '+str(Enemies[FifthEnemy+6]).rstrip()+' '+Loc5
					text = myfont.render(EnemyFiveName, False, sky_blue)
					screen.blit(text,(300,550))
					ObjectImage=Enemies[FifthEnemy+2]
					ScreenItem=GetScreenItem(ObjectImage)
					screen.blit(ScreenItem,(650,550))

					if len(LaserTargetList) > 15:
						SixthEnemy=LaserTargetList[15]
						Loc6=' x'+str(LaserTargetList[16])+' y'+str(LaserTargetList[17])
						EnemySixName='6: '+Enemies[SixthEnemy+1]+' '+str(Enemies[SixthEnemy+6]).rstrip()+' '+Loc6
						text = myfont.render(EnemySixName, False, sky_blue)
						screen.blit(text,(300,600))
						ObjectImage=Enemies[SixthEnemy+2]
						ScreenItem=GetScreenItem(ObjectImage)
						screen.blit(ScreenItem,(650,600))

						if len(LaserTargetList) > 18:
							SeventhEnemy=LaserTargetList[18]
							Loc7=' x'+str(LaserTargetList[19])+' y'+str(LaserTargetList[20])
							EnemySevenName='7: '+Enemies[SeventhEnemy+1]+' '+str(Enemies[SeventhEnemy+6]).rstrip()+' '+Loc7
							text = myfont.render(EnemyFiveName, False, sky_blue)
							screen.blit(text,(300,550))
							ObjectImage=Enemies[SeventhEnemy+2]
							ScreenItem=GetScreenItem(ObjectImage)
							screen.blit(ScreenItem,(650,550))

	pygame.display.flip()
	Selection=True
	while Selection:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP1 or event.key == pygame.K_1:
					LaserTarget=LaserTargetList[0]
					Selection=False
				if event.key == pygame.K_KP2 or event.key == pygame.K_2:
					if len(LaserTargetList) > 3:
						LaserTarget=LaserTargetList[3]
						Selection=False
				if event.key == pygame.K_KP3 or event.key == pygame.K_3:
					if len(LaserTargetList) > 6:
						LaserTarget=LaserTargetList[6]
						Selection=False
				if event.key == pygame.K_KP4 or event.key == pygame.K_4:
					if len(LaserTargetList) > 9:
						LaserTarget=LaserTargetList[9]
						Selection=False
				if event.key == pygame.K_KP5 or event.key == pygame.K_5:
					if len(LaserTargetList) > 12:
						LaserTarget=LaserTargetList[12]
						Selection=False
				if event.key == pygame.K_KP6 or event.key == pygame.K_6:
					if len(LaserTargetList) > 15:
						LaserTarget=LaserTargetList[15]
						Selection=False
				if event.key == pygame.K_KP7 or event.key == pygame.K_7:
					if len(LaserTargetList) > 18:
						LaserTarget=LaserTargetList[18]
						Selection=False
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
					LaserTarget=20000000
					Selection=False
	return(LaserTarget)


def SelectMissileEnemy (MissileTargetList, Enemies):
	text10 = myfont.render('Select Missile target or press enter to cancel', False, yellow)

	EnemyOneName='empty'
	EnemyTwoName='empty'
	EnemyThreeName='empty'
	EnemyFourName='empty'
	EnemyFiveName='empty'
	EnemySixName='empty'
	EnemySevenName='empty'

	Loc1=''
	Loc2=''
	Loc3=''
	Loc4=''
	Loc5=''
	Loc6=''
	Loc7=''

	VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
	DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

	screen.blit(Bombs,(300,300))
	screen.blit(text10,(300,300))

	FirstEnemy=MissileTargetList[0]
	Loc1=' x'+str(MissileTargetList[1])+' y'+str(MissileTargetList[2])
	EnemyOneName='1: '+Enemies[FirstEnemy+1]+' '+str(Enemies[FirstEnemy+6]).rstrip()+' '+Loc1
	text = myfont.render(EnemyOneName, False, sky_blue)
	screen.blit(text,(300,350))
	ObjectImage=Enemies[FirstEnemy+2]
	ScreenItem=GetScreenItem(ObjectImage)
	screen.blit(ScreenItem,(650,350))

	if len(MissileTargetList) > 3:
		SecondEnemy=MissileTargetList[3]
		Loc2=' x'+str(MissileTargetList[4])+' y'+str(MissileTargetList[5])
		EnemyTwoName='2: '+Enemies[SecondEnemy+1]+' '+str(Enemies[SecondEnemy+6]).rstrip()+Loc2
		text = myfont.render(EnemyTwoName, False, sky_blue)
		screen.blit(text,(300,400))
		ObjectImage=Enemies[SecondEnemy+2]
		ScreenItem=GetScreenItem(ObjectImage)
		screen.blit(ScreenItem,(650,400))

		if len(MissileTargetList) > 6:
			ThirdEnemy=MissileTargetList[6]
			Loc3=' x'+str(MissileTargetList[7])+' y'+str(MissileTargetList[8])
			EnemyThreeName='3: '+Enemies[ThirdEnemy+1]+' '+str(Enemies[ThirdEnemy+6]).rstrip()+Loc3
			text = myfont.render(EnemyThreeName, False, sky_blue)
			screen.blit(text,(300,450))
			ObjectImage=Enemies[ThirdEnemy+2]
			ScreenItem=GetScreenItem(ObjectImage)
			screen.blit(ScreenItem,(650,450))

			if len(MissileTargetList) > 9:
				FourthEnemy=MissileTargetList[9]
				Loc4=' x'+str(MissileTargetList[10])+' y'+str(MissileTargetList[11])
				EnemyFourName='4: '+Enemies[FourthEnemy+1]+' '+str(Enemies[FourthEnemy+6]).rstrip()+Loc4
				text = myfont.render(EnemyFourName, False, sky_blue)
				screen.blit(text,(300,500))
				ObjectImage=Enemies[FourthEnemy+2]
				ScreenItem=GetScreenItem(ObjectImage)
				screen.blit(ScreenItem,(650,500))

				if len(MissileTargetList) > 12:
					FifthEnemy=MissileTargetList[12]
					Loc5=' x'+str(MissileTargetList[13])+' y'+str(MissileTargetList[14])
					EnemyFiveName='5: '+Enemies[FifthEnemy+1]+' '+str(Enemies[FifthEnemy+6]).rstrip()+Loc5
					text = myfont.render(EnemyFiveName, False, sky_blue)
					screen.blit(text,(300,550))
					ObjectImage=Enemies[FifthEnemy+2]
					ScreenItem=GetScreenItem(ObjectImage)
					screen.blit(ScreenItem,(650,550))

					if len(MissileTargetList) > 15:
						SixthEnemy=MissileTargetList[15]
						Loc6=' x'+str(MissileTargetList[16])+' y'+str(MissileTargetList[17])
						EnemySixName='6: '+Enemies[SixthEnemy+1]+' '+str(Enemies[SixthEnemy+6]).rstrip()+Loc6
						text = myfont.render(EnemySixName, False, sky_blue)
						screen.blit(text,(300,600))
						ObjectImage=Enemies[SixthEnemy+2]
						ScreenItem=GetScreenItem(ObjectImage)
						screen.blit(ScreenItem,(650,600))

						if len(MissileTargetList) > 18:
							SeventhEnemy=MissileTargetList[18]
							Loc7=' x'+str(MissileTargetList[19])+' y'+str(MissileTargetList[20])
							EnemySevenName='7: '+Enemies[SeventhEnemy+1]+' '+str(Enemies[SeventhEnemy+6]).rstrip()+Loc7
							text = myfont.render(EnemySevenName, False, sky_blue)
							screen.blit(text,(300,650))
							ObjectImage=Enemies[SeventhEnemy+2]
							ScreenItem=GetScreenItem(ObjectImage)
							screen.blit(ScreenItem,(650,650))

	pygame.display.flip()
	Selection=True
	while Selection:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP1 or event.key == pygame.K_1:
					MissileTarget=MissileTargetList[0]
					Selection=False
				if event.key == pygame.K_KP2 or event.key == pygame.K_2:
					if len(MissileTargetList) > 3:
						MissileTarget=MissileTargetList[3]
						Selection=False
				if event.key == pygame.K_KP3 or event.key == pygame.K_3:
					if len(MissileTargetList) > 6:
						MissileTarget=MissileTargetList[6]
						Selection=False
				if event.key == pygame.K_KP4 or event.key == pygame.K_4:
					if len(MissileTargetList) > 9:
						MissileTarget=MissileTargetList[9]
						Selection=False
				if event.key == pygame.K_KP5 or event.key == pygame.K_5:
					if len(MissileTargetList) > 12:
						MissileTarget=MissileTargetList[12]
						Selection=False
				if event.key == pygame.K_KP6 or event.key == pygame.K_6:
					if len(MissileTargetList) > 15:
						MissileTarget=MissileTargetList[15]
						Selection=False
				if event.key == pygame.K_KP7 or event.key == pygame.K_7:
					if len(MissileTargetList) > 18:
						MissileTarget=MissileTargetList[18]
						Selection=False
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
					MissileTarget=20000000
					Selection=False
	return(MissileTarget)
		
			
def GetEnemyStatus (Enemies, PlayerX, PlayerY, ClosestEnemy):
	EnemyDistance=1000000
	if ClosestEnemy > (len(Enemies)*13):
		EnemyStat = 'No enemies'
		EnemyColor=green
	else:
		EnemyMaxHull=int(Enemies[ClosestEnemy])*100
		EnemyHull=str(Enemies[ClosestEnemy+6]).rstrip()
		EnemyMissiles=str(Enemies[ClosestEnemy+7]).rstrip()
		EnemyX=int(Enemies[ClosestEnemy+10])
		EnemyY=int(Enemies[ClosestEnemy+11])
		EnemyMood=Enemies[ClosestEnemy+12].rstrip()
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		EnemyDamageLaser=int(Enemies[ClosestEnemy+3])
		EnemyDamageMissile=int(EnemyDamageLaser*1.5)
		EnemyDamage=(EnemyDamageMissile/PlayerHull)
		if EnemyDamage < 0.1:
			EnemyColor=green
		elif EnemyDamage < 0.2:
			EnemyColor=light_grey
		elif EnemyDamage < 0.3:
			EnemyColor=yellow
		elif EnemyDamage <= 0.4:
			EnemyColor=orange
		elif EnemyDamage > 0.4:
			EnemyColor=red
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			if ((-4) <= XDiff) and ( XDiff <= 4) and ((-4) <= YDiff) and (YDiff <= 4):
				EnemyStat=str(Enemies[ClosestEnemy+1]).rstrip()+' at: x'+str(XDiff)+' y'+str(YDiff)+' ('+EnemyMood+')'+' Hull: '+EnemyHull+' Missiles: '+EnemyMissiles+' LASER LOCK'
			else:
				if PlayerMissiles > 0:
					EnemyStat=str(Enemies[ClosestEnemy+1]).rstrip()+' at: x'+str(XDiff)+' y'+str(YDiff)+' ('+EnemyMood+')'+' Hull: '+EnemyHull+' Missiles: '+EnemyMissiles+' MISSILE LOCK'
				else:
					EnemyStat=str(Enemies[ClosestEnemy+1]).rstrip()+' at: x'+str(XDiff)+' y'+str(YDiff)+' ('+EnemyMood+')'+' Hull: '+EnemyHull+' Missiles: '+EnemyMissiles+' NO MISSILES'
		else:
			EnemyStat=str(Enemies[ClosestEnemy+1]).rstrip()+' at: x'+str(XDiff)+' y'+str(YDiff)+' ('+EnemyMood+')'+' Hull: '+EnemyHull+' Missiles: '+EnemyMissiles+' OUT OF RANGE'
	EnemyStatus = myfont.render(EnemyStat, False, EnemyColor)
	return(EnemyStatus)

def FireMissile (Enemies, Stars, Asteroids, MissileTarget, PlayerLevel, Exp, Nexp):
	global EnemyKills
	Nexp=int(Exp[0])
	PlayerMissileDamage=PlayerLevel*15
	SPlayerMissileDamage=str(PlayerMissileDamage)
	EnemyName=Enemies[MissileTarget+1]
	EnemyHull=int(Enemies[MissileTarget+6])
	EnemyHull=EnemyHull-PlayerMissileDamage
	if EnemyHull < 1:
		EnemyLevel=int(Enemies[MissileTarget])
		EnemyName=Enemies[MissileTarget+1]
		EnemyDamageLaser=int(Enemies[MissileTarget+3])
		EnemySpeed=int(Enemies[MissileTarget+4])
		EnemyMissiles=int(Enemies[MissileTarget+8])
		EnemyScan=int(Enemies[MissileTarget+5])
		EnemyDef=int(Enemies[MissileTarget+8])
		EnemyHealth=int(Enemies[MissileTarget+6])
		EnemyX=int(Enemies[MissileTarget+10])
		EnemyY=int(Enemies[MissileTarget+11])
		Xdiff=EnemyX-PlayerX
		Ydiff=EnemyY-PlayerY
		EnemyDanger=int(((EnemyDamageLaser/10)+EnemySpeed+EnemyLevel+EnemyMissiles)/4)

		EnemyXp=EnemyDanger
		EnemyKills=EnemyKills+EnemyXp
		Nexp=Nexp+EnemyXp
		Exp[0]=Nexp
		Counter=0
		while Counter < 13:
			del Enemies[MissileTarget]
			Counter=Counter+1
		Blast.play()
#		print(str(EnemyName).rstrip(), 'destroyed by missile...')
		Status=EnemyName.rstrip()+' destroyed by missile, press enter'
		ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
		EnemyStatus=GetEnemyStatus (Enemies, PlayerX, PlayerY, ClosestEnemy)
		VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
		DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
	else:
		Enemies[MissileTarget+6]=EnemyHull
		Beep.play()
#		print(str(EnemyName).rstrip(), 'hit by missile for ', SPlayerMissileDamage, ' damage...')
		Status=EnemyName.rstrip()+' hit by missile for '+SPlayerMissileDamage+' damage'
		ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
		EnemyStatus=GetEnemyStatus (Enemies, PlayerX, PlayerY, ClosestEnemy)
		DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
	return(Enemies, Exp)

def FireLaser (Enemies, Stars, Asteroids, LaserTarget, PlayerLevel, Exp, Nexp):
	global EnemyKills
	Nexp=int(Exp[0])
	PlayerLaserDamage=PlayerLevel*10
	SPlayerLaserDamage=str(PlayerLaserDamage)
	EnemyName=Enemies[LaserTarget+1]
	EnemyHull=int(Enemies[LaserTarget+6])
	EnemyHull=EnemyHull-PlayerLaserDamage
	Enemies[LaserTarget+6]=EnemyHull
	if EnemyHull < 1:
		Vaporize.play()
#		print(str(EnemyName).rstrip(), 'destroyed by laser...')
		EnemyLevel=int(Enemies[LaserTarget])
		EnemyName=Enemies[LaserTarget+1]
		EnemyDamageLaser=int(Enemies[LaserTarget+3])
		EnemySpeed=int(Enemies[LaserTarget+4])
		EnemyMissiles=int(Enemies[LaserTarget+8])
		EnemyScan=int(Enemies[LaserTarget+5])
		EnemyDef=int(Enemies[LaserTarget+8])
		EnemyHealth=int(Enemies[LaserTarget+6])
		EnemyX=int(Enemies[LaserTarget+10])
		EnemyY=int(Enemies[LaserTarget+11])
		Xdiff=EnemyX-PlayerX
		Ydiff=EnemyY-PlayerY
		EnemyDanger=int(((EnemyDamageLaser/10)+EnemySpeed+EnemyLevel+EnemyMissiles)/4)

		EnemyXp=EnemyDanger
		EnemyKills=EnemyKills+EnemyXp
		Nexp=Nexp+EnemyXp
		Exp[0]=Nexp
		Counter=0
		while Counter < 13:
			del Enemies[LaserTarget]
			Counter=Counter+1
	else:
		Laser.play()
#		print(str(EnemyName).rstrip(), 'hit by laser for ', PlayerLaserDamage, ' damage...')
	return(Enemies, Exp)

def ScanAsteroid (EnemyX, EnemyY):
	Counter=0
	MaxCounter=len(Asteroids)
	while Counter < MaxCounter:
		AsteroidX=int(Asteroids[Counter+1])
		AsteroidY=int(Asteroids[Counter+2])
		XDiff=AsteroidX-EnemyX
		YDiff=AsteroidY-EnemyY
		if ((-4) <= XDiff) and ( XDiff <= 4) and ((-4) <= YDiff) and (YDiff <= 4):
			AsteroidScan[0]=Counter
			AsteroidScan[1]=int(Asteroids[Counter])
			AsteroidScan[2]=AsteroidX
			AsteroidScan[3]=AsteroidY
			break
		Counter=Counter+3
	return (AsteroidScan)

while Level < 31:
	SpeedSetting=3
	CXdiff=200
	CYdiff=200
	ClosestAsteroid=[200, 200]
	CollideStar=list()
	ClosestEnemy=1000
	Stars=list()
	Asteroids=list()
	Enemies=list()
	ScreenRange=list()
	PlayerDamage=PlayerLevel*10
	ExpNeeded=PlayerLevel*5
	Spawn=random.randint(1,4)
	if Spawn==1:
		PlayerX=random.randint(1,200)
		PlayerY=200
	elif Spawn==2:
		PlayerX=200
		PlayerY=random.randint(1,200)
	elif Spawn==3:
		PlayerY=1
		PlayerX=random.randint(1,200)
	elif Spawn==4:
		PlayerX=1
		PlayerY=random.randint(1,200)
	WormholeX=100
	WormholeY=100
	# Main loop
	#Create list of stars in current level
	del Stars[:]
	del Asteroids[:]
	del Enemies[:]
	for Item in range(1, 100):
		StarType=random.randint(1,3)
		StarX=random.randint(1,200)
		StarY=random.randint(1,200)
		Stars.append(StarType)
		Stars.append(StarX)
		Stars.append(StarY)
	# Create a list of asteroids in current level
	for Item in range(1,100):
		AsteroidType=random.randint(1,3)
		AsteroidX=random.randint(1,200)
		AsteroidY=random.randint(1,200)
		Asteroids.append(AsteroidType)
		Asteroids.append(AsteroidX)
		Asteroids.append(AsteroidY)
	# Create list of enemies in current level
	EnemyFile=open('enemylist', 'r')
	Enemylist=list(EnemyFile)
	EnemyFile.close()
	GeneratedEnemies=0
	Counter=0
	MaxCounter=len(Enemylist)
	while Counter < MaxCounter:
		Enemy=Enemylist[Counter].rstrip()
		EnemyLevel=int(Enemylist[Counter])
		NumberofRepeats=int(Level / EnemyLevel)
		if NumberofRepeats > 5:
			NumberofRepeats=5
		EnemyCounter=0
		while  NumberofRepeats > EnemyCounter:
			Enemies.append(Enemylist[Counter])
			if EnemyCounter==0:
				Suffix=' A'
			elif EnemyCounter==1:
				Suffix=' B'
			elif EnemyCounter==2:
				Suffix=' C'
			elif EnemyCounter==3:
				Suffix=' D'
			elif EnemyCounter==4:
				Suffix=' E'
			EnemyName=Enemylist[Counter+1].rstrip()+Suffix
			Enemies.append(EnemyName)
			Enemies.append(Enemylist[Counter+2])
			Enemies.append(Enemylist[Counter+3])
			Enemies.append(Enemylist[Counter+4])
			Enemies.append(Enemylist[Counter+5])
			Enemies.append(Enemylist[Counter+6])
			Enemies.append(Enemylist[Counter+7])
			Enemies.append(Enemylist[Counter+7])
			Enemies.append(Enemylist[Counter+8])
			EnemyX=random.randint(1,200)
			EnemyY=random.randint(1,200)
			Enemies.append(EnemyX)
			Enemies.append(EnemyY)
			Enemies.append('On patrol')
			GeneratedEnemies=GeneratedEnemies+int(Enemylist[Counter])
			EnemyCounter=EnemyCounter+1
		Counter=Counter+9
	if Level == 6:
		Enemies.append(6)
		Enemies.append('Teleporter')
		Enemies.append('Teleporter\n')
		Enemies.append(60)
		Enemies.append(6)
		Enemies.append(120)
		Enemies.append(600)
		Enemies.append(6)
		Enemies.append(6)
		Enemies.append(40)
		EnemyX=random.randint(1,200)
		EnemyY=random.randint(1,200)
		Enemies.append(EnemyX)
		Enemies.append(EnemyY)
		Enemies.append('On patrol')
		GeneratedEnemies=GeneratedEnemies+6
	elif Level == 12:
		Enemies.append(12)
		Enemies.append('Eye')
		Enemies.append('Eye\n')
		Enemies.append(120)
		Enemies.append(12)
		Enemies.append(120)
		Enemies.append(1200)
		Enemies.append(12)
		Enemies.append(12)
		Enemies.append(40)
		EnemyX=random.randint(1,200)
		EnemyY=random.randint(1,200)
		Enemies.append(EnemyX)
		Enemies.append(EnemyY)
		Enemies.append('On patrol')
		GeneratedEnemies=GeneratedEnemies+12

	elif Level == 18:
		Enemies.append(18)
		Enemies.append('Leech')
		Enemies.append('Leech\n')
		Enemies.append(180)
		Enemies.append(18)
		Enemies.append(180)
		Enemies.append(1800)
		Enemies.append(18)
		Enemies.append(18)
		Enemies.append(40)
		EnemyX=random.randint(1,200)
		EnemyY=random.randint(1,200)
		Enemies.append(EnemyX)
		Enemies.append(EnemyY)
		Enemies.append('On patrol')
		GeneratedEnemies=GeneratedEnemies+18

	elif Level == 24:
		Enemies.append(24)
		Enemies.append('Ramjet')
		Enemies.append('Ramjet\n')
		Enemies.append(240)
		Enemies.append(120)
		Enemies.append(120)
		Enemies.append(2400)
		Enemies.append(24)
		Enemies.append(24)
		Enemies.append(40)
		EnemyX=random.randint(1,200)
		EnemyY=random.randint(1,200)
		Enemies.append(EnemyX)
		Enemies.append(EnemyY)
		Enemies.append('On patrol')
		GeneratedEnemies=GeneratedEnemies+24

	elif Level == 30:
		Enemies.append(30)
		Enemies.append('Mothership')
		Enemies.append('Mothership\n')
		Enemies.append(300)
		Enemies.append(30)
		Enemies.append(120)
		Enemies.append(3000)
		Enemies.append(30)
		Enemies.append(30)
		Enemies.append(40)
		EnemyX=random.randint(1,200)
		EnemyY=random.randint(1,200)
		Enemies.append(EnemyX)
		Enemies.append(EnemyY)
		Enemies.append('On patrol')
		GeneratedEnemies=GeneratedEnemies+30


	EnemyKills=0
	EnemyKillTarget=int(GeneratedEnemies*0.5)
	if EnemyKillTarget==0 and len(Enemies)>0:
		EnemyKillTarget=1
	NumberofEnemies=int(len(Enemies)/12)
#	print('Nomber of enemies: ',NumberofEnemies)

	NewLevel(Level)
	WormholeOpenPlayed=0
	ScanEnemy=1000000
	Action=0
	MissilePosX=-50
	MissilePosY=-50
	ExplosionX=-50
	ExplosionY=-50
	MaxMove=PlayerLevel
	SPlayerLevel=str(PlayerLevel)
	Move=PlayerLevel
	SMove=str(Move)
	Radar=2*PlayerLevel
	Nexp=0
	SLevel=str(Level)
	if Radar < 20:
		Radar=20
	SMove=str(Move)
	SLevel=str(Level)
	SPlayerLevel=str(PlayerLevel)
	PlayerDamage=PlayerLevel*10
	PlayerHullMax=str(PlayerLevel*100)
	SPlayerHull=str(int(PlayerHull))
	SPlayerMissiles=str(PlayerMissiles)
	SExp=str(Exp[0])
	SExpNeeded=str(ExpNeeded)
	SLevel=str(Level)
	ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
	EnemyStatus=GetEnemyStatus (Enemies, PlayerX, PlayerY, ClosestEnemy)
	Status=SetStatus()
	VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
	DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

	running=True
	while running:
#		print('-Player-')
		Action=0
		ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
#		print(ClosestEnemy)
		while Action < 3:
#			print('Playerturn: ', Action)
			EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
			ScreenAction=0
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					Direction=5
					if event.key == pygame.K_KP1 or event.key == pygame.K_z:
						Direction=1
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=1
					elif event.key == pygame.K_KP2 or event.key == pygame.K_x:
						Direction=2
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=1
					elif event.key == pygame.K_KP3 or event.key == pygame.K_c:
						Direction=3
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=1
					elif event.key == pygame.K_KP4 or event.key == pygame.K_a:
						Direction=4
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=1
					elif event.key == pygame.K_KP5 or event.key == pygame.K_s:
						Direction=5
						Action=3
						SAction=str(Action+1)
						ScreenAction=1
					elif event.key == pygame.K_KP6 or event.key == pygame.K_d:
						Direction=6
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=1
					elif event.key == pygame.K_KP7 or event.key == pygame.K_q:
						Direction=7
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=1
					elif event.key == pygame.K_KP8 or event.key == pygame.K_w:
						Direction=8
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=1
					elif event.key == pygame.K_KP9 or event.key == pygame.K_e:
						Direction=9
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=1
					elif event.key == pygame.K_KP_PLUS or event.key == pygame.K_t:
						Move=Move+1
						if Move > PlayerLevel:
							Move=PlayerLevel
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
						Status=SetStatus()
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_KP_MINUS or event.key == pygame.K_r:
						Move=Move-1
						if Move < 1:
							Move=1
						EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
						Status=SetStatus()
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_KP0 or event.key == pygame.K_SPACE:
						if PlayerMissiles > 0:
							MissileTarget=20000000
							MissileScan(Enemies, MissileTargetList)
#							print('Missile targets: ', MissileTargetList)
							if len(MissileTargetList) > 0:
								MissileTarget=SelectMissileEnemy(MissileTargetList, Enemies)
							if MissileTarget < len(Enemies):
								PlayerMissiles=PlayerMissiles-1
								MissileTargetX=int(Enemies[MissileTarget+10])
								MissileTargetY=int(Enemies[MissileTarget+11])
								MissilePosX=PlayerX
								MissilePosY=PlayerY
								ScreenItem=Bomb
								for item in range(1, 20):
									if (MissilePosX < MissileTargetX) and (MissilePosY < MissileTargetY):
										MissilePosX=MissilePosX+1
										MissilePosY=MissilePosY+1
									if (MissilePosX < MissileTargetX) and (MissilePosY == MissileTargetY):
										MissilePosX=MissilePosX+1
									if (MissilePosX < MissileTargetX) and (MissilePosY > MissileTargetY):
										MissilePosX=MissilePosX+1
										MissilePosY=MissilePosY-1
									if (MissilePosX == MissileTargetX) and (MissilePosY > MissileTargetY):
										MissilePosY=MissilePosY-1
									if (MissilePosX > MissileTargetX) and (MissilePosY > MissileTargetY):
										MissilePosX=MissilePosX-1
										MissilePosY=MissilePosY-1
									if (MissilePosX > MissileTargetX) and (MissilePosY == MissileTargetY):
										MissilePosX=MissilePosX-1
									if (MissilePosX > MissileTargetX) and (MissilePosY < MissileTargetY):
										MissilePosX=MissilePosX-1
										MissilePosY=MissilePosY+1
									if (MissilePosX == MissileTargetX) and (MissilePosY < MissileTargetY):
										MissilePosY=MissilePosY+1
									MissileScreenX=MissilePosX-PlayerX
									MissileScreenY=MissilePosY-PlayerY
									if (MissileTargetX==MissilePosX) and (MissileTargetY==MissilePosY):
										break
									VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
									Status=SetStatus()
									DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

								Action=Action+1
								ExplosionX=MissileTargetX
								ExplosionY=MissileTargetY
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
								Status=SetStatus()
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
								MissilePosX=-50
								MissilePosY=-50
								ExplosionX=-50
								ExplosionY=-50
								FireMissile(Enemies, Stars, Asteroids, MissileTarget, PlayerLevel, Exp, Nexp)
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
								Status=SetStatus()
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							else:
								Status='No Missile Targets, Press Enter'
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
								wait()		
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
								Status=SetStatus()
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
						else:
							Status='No Missiles, Press Enter'
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							wait()		
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							Status=SetStatus()
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_KP_DIVIDE or event.key == pygame.K_LCTRL:
						LaserTarget=20000000
						LaserScan(Enemies, LaserTargetList)
						if len(LaserTargetList) > 0:
							LaserTarget=SelectLaserEnemy(LaserTargetList, Enemies)
						if LaserTarget < len(Enemies):
							LaserTargetX=int(Enemies[LaserTarget+10])
							LaserTargetY=int(Enemies[LaserTarget+11])
							ExplosionX=LaserTargetX
							ExplosionY=LaserTargetY
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							Status=SetStatus()
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							MissilePosX=-50
							MissilePosY=-50
							ExplosionX=-50
							ExplosionY=-50
							FireLaser(Enemies, Stars, Asteroids, LaserTarget, PlayerLevel, Exp, Nexp)
							Action=Action+1
							SAction=str(Action+1)
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							Status=SetStatus()
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							ScreenAction=1
						else:
							Status='No Laser Targets'
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							wait()		
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							Status=SetStatus()
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif (event.key == pygame.K_KP_MULTIPLY or event.key == pygame.K_l) and len(Enemies) > 0:
						DoEnemyInfo(Enemies, PlayerX, PlayerY, ClosestEnemy)
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
						Status=SetStatus()
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif (event.key == pygame.K_KP_PERIOD or event.key == pygame.K_DELETE) and len(Enemies) > 0:
						DoEnemyXL(Enemies, PlayerX, PlayerY)
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
						Status=SetStatus()
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_END:
						CollectedEnemies=[None]*7
						DoEnemyList(Enemies,CollectedEnemies, PlayerX, PlayerY)
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
						Status=SetStatus()
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_h:
						DoHelp()
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
						Status=SetStatus()
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_ESCAPE:
						sys.exit()
					MoveCounter=0
					while MoveCounter < Move:
						if Direction==1:
							PlayerX=PlayerX-1
							PlayerY=PlayerY-1
						elif Direction==2:
							PlayerY=PlayerY-1
						elif Direction==3:
							PlayerX=PlayerX+1
							PlayerY=PlayerY-1
						elif Direction==4:
							PlayerX=PlayerX-1
						elif Direction==6:
							PlayerX=PlayerX+1
						elif Direction==7:
							PlayerX=PlayerX-1
							PlayerY=PlayerY+1
						elif Direction==8:
							PlayerY=PlayerY+1
						elif Direction==9:
							PlayerX=PlayerX+1
							PlayerY=PlayerY+1
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						# Check if player has hit star
						CrashStar=0
						Damage=0
						CrashStar=StarDetect(Stars, PlayerX, PlayerY)
						if not CrashStar==0:
							if CrashStar==1:
								Damage=100
							elif CrashStar==2:
								Damage=200
							elif CrashStar==3:
								Damage=300
							ExplosionX=PlayerX
							ExplosionY=PlayerY
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							Status=SetStatus()
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							MissilePosX=-50
							MissilePosY=-50
							ExplosionX=-50
							ExplosionY=-50
							PlayerHull=PlayerHull-Damage
							if PlayerHull < 1:
								Blast.play()
								Status='You Crashed into a Star, press enter'
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
								wait()
								running=False
								sys.exit()
							else:
								if PlayerHull<(PlayerLevel*50):
									Hurt.play()
								else:
									Sizzle.play()

						Counter=0
						CrashAsteroid=0
						MaxCounter=len(Asteroids)
						while Counter < MaxCounter:
							AsteroidType=Asteroids[Counter]
							AsteroidX=Asteroids[Counter+1]
							AsteroidY=Asteroids[Counter+2]
							if (PlayerX == AsteroidX) and (PlayerY == AsteroidY):
								if PlayerHull <= PlayerLevel*50:
									Yeah.play()
								else:
									Eating.play()
								CrashAsteroid=AsteroidType
								WipeCounter=0
								while WipeCounter < 3:
									del Asteroids[Counter]
									WipeCounter=WipeCounter+1
								MaxCounter=len(Asteroids)
							Counter=Counter+3
						Health=0
						ExtraMissiles=0
						if not CrashAsteroid==0:
							if CrashAsteroid==1:
								Health=100
								ExtraMissiles=2
							elif CrashAsteroid==2:
								Health=200
								ExtraMissiles=3
							elif CrashAsteroid==3:
								Health=300
								ExtraMissiles=5
							PlayerHull=PlayerHull+Health
							PlayerMissiles=PlayerMissiles+ExtraMissiles
#							print('Player harvests asteroid...')
							if PlayerHull > (PlayerLevel*100):
								PlayerHull = (PlayerLevel*100)
							if PlayerMissiles > PlayerLevel:
								PlayerMissiles = PlayerLevel
	
						if ScreenAction==1:
							Nexp=int(Exp[0])
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							Status=SetStatus()
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

						MoveCounter=MoveCounter+1

		Nexp=int(Exp[0])
		if Nexp >= ExpNeeded:
			Nexp=Nexp-ExpNeeded
			PlayerLevel=PlayerLevel+1
			ExpNeeded=PlayerLevel*5
			PlayerHull=PlayerLevel*100
			PlayerMissiles=PlayerLevel
			Status='Ship leveled up, press enter'
			if PlayerLevel > 20:
				PlayerLevel=20
				PlayerHull=PlayerLevel*100
				PlayerMissiles=PlayerLevel
				Status='Player restored, press enter'
			if Nexp < 0:
				NExp=0
			Exp[0]=Nexp
			Move=PlayerLevel
			PlayerHullMax=PlayerLevel*100
			LevelUp.play()

			ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
			EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
			VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
			DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
			wait()

#		print(EnemyKills, ' of ', EnemyKillTarget)

		if len(Enemies) > 0 and running:
#			print()
#			print('--ENEMY TURN--')
			EnemyDir=5
			Status='Enemy Turn'
			EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
			VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
			DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
			Counter=0
			EnemyName='Enemy'
			MaxCounter=len(Enemies)
			while Counter < MaxCounter and running:
				EnemyActive=0
				Fleeing=0
				LaserFired=0
				MissileFired=0
				EnemyMoves=0
				EnemyDir=5
				EnemyName=str(Enemies[Counter+1]).rstrip()
				#print(EnemyName)
				EnemyAction=0
				Message=0
				while EnemyAction < 2:
					EnemyLevel=int(Enemies[Counter])
					EnemyName=str(Enemies[Counter+1]).rstrip()
					EnemyLaserDamage=int(Enemies[Counter+3])
					EnemyHull=int(Enemies[Counter+6])
					EnemyScan=int(Enemies[Counter+5])
					EnemyMaxSpeed=int(Enemies[Counter+4])
					EnemyMaxMissiles=int(Enemies[Counter+8])
					EnemyDef=int(Enemies[Counter+9])
					EnemyX=int(Enemies[Counter+10])
					EnemyY=int(Enemies[Counter+11])
					XDiff=PlayerX-EnemyX
					YDiff=PlayerY-EnemyY
					if EnemyHull < (EnemyLevel*EnemyDef):
						Enemies[Counter+12]='Scared'
					if (-4 <= XDiff) and ( XDiff <= 4) and (-4 <= YDiff) and (YDiff <= 4) and running:
						if LaserFired==0:
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyActive=1
							EnemyLaserDamage=int(Enemies[Counter+3])
							PlayerHull=PlayerHull-EnemyLaserDamage
							Enemies[Counter+12]='Fired laser'
							Message=1
							SEnemyLaserDamage=str(EnemyLaserDamage)
							EnemyAction=EnemyAction+1
							ExplosionX=PlayerX
							ExplosionY=PlayerY
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							Status=SetStatus()
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							MissilePosX=-50
							MissilePosY=-50
							ExplosionX=-50
							ExplosionY=-50
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							Status=SetStatus()
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							if PlayerHull <= 0:
								Vaporize.play()
								Status='Player destroyed by '+EnemyName+' laser'
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
								wait()
								running=False
								sys.exit()
							else:
								if PlayerHull<(PlayerLevel*50):
									Hurt.play()
								else:
									Laser.play()
							Status=str(EnemyName).rstrip()+' fires laser...'
							LaserFired=1
					if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20) and running:
						EnemyMissiles=int(Enemies[Counter+7])
						if EnemyMissiles > 0:
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyActive=1
							if MissileFired==0:
								if EnemyName=='Mothership':
									#print('enemy appended')
									Enemies.append('3')
									Enemies.append('Hunter Drone')
									Enemies.append('HunterDrone\n')
									Enemies.append('70')
									Enemies.append('12')
									Enemies.append('30')
									Enemies.append('300')
									Enemies.append('3')
									Enemies.append('3')
									Enemies.append('9')
									OffSetX=EnemyX+random.randint(-1,1)
									OffSetY=EnemyY+random.randint(-1,1)
									Enemies.append(OffSetX)
									Enemies.append(OffSetY)
									Enemies.append('On patrol')
									MaxCounter=len(Enemies)
									Launch.play()
									Status='Mothership A launches Hunter Drone...'
									Enemies[Counter+12]='Launched a drone'
									Message=1
									EnemyMissiles=EnemyMissiles-1
									Enemies[Counter+7]=EnemyMissiles
									EnemyAction=EnemyAction+1
								elif EnemyName=='Leech':
									Status='Leech steals life from you...'
									Enemies[Counter+12]='Leech steals life...'
									Message=1
									EnemyMissiles=EnemyMissiles-1
									PlayerHull=PlayerHull-EnemyMissileDamage
									EnemyHull=EnemyHull+EnemyMissileDamage
									Enemies[Counter+6]=EnemyHull
									Enemies[Counter+7]=EnemyMissiles
									EnemyAction=EnemyAction+1
									Steal.play()
								elif EnemyName=='Eye':
									if EnemyHull > (EnemyLevel*EnemyDef):
										Status='Eye jumps you...'
										Enemies[Counter+12]='Eye jumps you...'
										Message=1
										EnemyMissiles=EnemyMissiles-1
										PlayerHull=PlayerHull-EnemyLaserDamage
										EnemyX=PlayerX+random.randint(-1,1)
										EnemyY=PlayerY+random.randint(-1,1)
										Enemies[Counter+7]=EnemyMissiles
										Enemies[Counter+10]=EnemyX
										Enemies[Counter+11]=EnemyY
										EnemyAction=EnemyAction+1
										Teleport.play()
								elif EnemyName=='Teleporter':
									Status='Teleporter teleports you...'
									Enemies[Counter+12]='Teleporter teleported you'
									Message=1
									EnemyMissiles=EnemyMissiles-1
									PlayerX=random.randint(1,200)
									PlayerY=random.randint(1,200)
									Enemies[Counter+7]=EnemyMissiles
									EnemyAction=EnemyAction+1
									Teleport.play()
								else:
									MissileTargetX=PlayerX
									MissileTargetY=PlayerY
									MissilePosX=int(Enemies[Counter+10])
									MissilePosY=int(Enemies[Counter+11])
									ScreenItem=Bomb
									MissileCounter=0
									while MissileCounter < 20:
										if (MissilePosX < MissileTargetX) and (MissilePosY < MissileTargetY):
											MissilePosX=MissilePosX+1
											MissilePosY=MissilePosY+1
										if (MissilePosX < MissileTargetX) and (MissilePosY == MissileTargetY):
											MissilePosX=MissilePosX+1
										if (MissilePosX < MissileTargetX) and (MissilePosY > MissileTargetY):
											MissilePosX=MissilePosX+1
											MissilePosY=MissilePosY-1
										if (MissilePosX ==MissileTargetX) and (MissilePosY > MissileTargetY):
											MissilePosY=MissilePosY-1
										if (MissilePosX > MissileTargetX) and (MissilePosY > MissileTargetY):
											MissilePosX=MissilePosX-1
											MissilePosY=MissilePosY-1
										if (MissilePosX > MissileTargetX) and (MissilePosY == MissileTargetY):
											MissilePosX=MissilePosX-1
										if (MissilePosX > MissileTargetX) and (MissilePosY < MissileTargetY):
											MissilePosX=MissilePosX-1
											MissilePosY=MissilePosY+1
										if (MissilePosX == MissileTargetX) and (MissilePosY < MissileTargetY):
											MissilePosY=MissilePosY+1
										MissileScreenX=MissilePosX-PlayerX
										MissileScreenY=MissilePosY-PlayerY
										ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
										EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
										VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
										DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
										if (MissilePosX == MissileTargetX) and (MissilePosY == MissileTargetY):
											break
									
									MissilePosX=-50
									MissilePosY=-50
									ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
									EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							
									ExplosionX=PlayerX
									ExplosionY=PlayerY
									ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
									EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
									VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
									Status=SetStatus()
									DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
									MissilePosX=-50
									MissilePosY=-50
									ExplosionX=-50
									ExplosionY=-50
													
									VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
									DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

									EnemyAction=EnemyAction+1
									EnemyMissiles=EnemyMissiles-1
									Enemies[Counter+7]=EnemyMissiles
									EnemyName=Enemies[Counter+1]
									EnemyMissileDamage=int(Enemies[Counter+3])*1.5
									PlayerHull=PlayerHull-EnemyMissileDamage
									if Message==0:
										Enemies[Counter+12]='Fired a missile'
										Message=1
									SEnemyMissileDamage=str(EnemyMissileDamage)
								if PlayerHull <= 0:
									Blast.play()
									Status='Player destroyed by '+EnemyName+' missile'
									EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
									VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
									ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
									DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
									EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
									wait()
									running=False
									sys.exit()
								else:
									if PlayerHull<(PlayerLevel*50):
										Hurt.play()
									else:
										Beep.play()
								MissileFired=1
								Status=str(EnemyName).rstrip()+' fires missile...'
					if EnemyHull < (EnemyLevel*50) or EnemyHull < (EnemyLevel*EnemyDef) and running:
						Fleeing=1
						AsteroidScan=[None]*4
						AsteroidScan=ScanAsteroid(EnemyX, EnemyY)
						if not AsteroidScan[0]==None:
							Enemies[Counter+12]='Ate an asteroid'
							EnemyActive=1
							Message=1
							if EnemyHull < (EnemyLevel*EnemyDef):
								Ahh.play()
							else:
								Eating.play()
							AsteroidCounter=int(AsteroidScan[0])
							CrashAsteroid=int(AsteroidScan[1])
							EnemyX=int(AsteroidScan[2])
							EnemyY=int(AsteroidScan[3])
							if not CrashAsteroid==0:
								if CrashAsteroid==1:	
									Health=100
									ExtraMissiles=1
								elif CrashAsteroid==2:
									Health=200
									ExtraMissiles=2
								elif CrashAsteroid==3:
									Health=300
									ExtraMissiles=3
								EnemyHull=EnemyHull+Health
								if EnemyHull > (EnemyLevel*100):
									EnemyHull = (EnemyLevel*100)
								EnemyMissiles=int(Enemies[Counter+7])
								EnemyMissiles=EnemyMissiles+ExtraMissiles
								if EnemyMissiles > EnemyMaxMissiles:
									EnemyMissiles = EnemyMaxMissiles
								Enemies[Counter+6]=EnemyHull
								Enemies[Counter+7]=EnemyMissiles
								Enemies[Counter+10]=EnemyX
								Enemies[Counter+11]=EnemyY
								WipeCounter=0
								Status=str(EnemyName).rstrip()+' ate asteroid'
								screen.blit(AsteroidHarvest,(300,300))
								ObjectImage=str(Enemies[Counter+2])
								ScreenItemA=GetScreenItem(ObjectImage)
								if CrashAsteroid==1:
									ScreenItemB=Asteroid
									Size=' small '
								elif CrashAsteroid==2:
									ScreenItemB=Asteroid2
									Size=' medium '
								elif CrashAsteroid==3:
									ScreenItemB=Asteroid3
									Size=' large '
								Crashtext=EnemyName+' eats'+Size+'asteroid'
								text01 = myfont.render(Crashtext, False, green)
								textEnter='Press enter'
								text02 = myfont.render(textEnter, False, green)
								screen.blit(text01,(300,300))
								screen.blit(text02,(300,680))
								screen.blit(ScreenItemB,(525,475))
								screen.blit(ScreenItemA,(425,475))
								pygame.display.flip()
								wait()
								while WipeCounter < 3:
									del Asteroids[AsteroidCounter]
									WipeCounter=WipeCounter+1
								AsteroidMaxCounter=len(Asteroids)
							EnemyAction=EnemyAction+1

					PDist=PlayerDistance(EnemyX, EnemyY, PlayerX, PlayerY)
					if EnemyHull <= (EnemyLevel*EnemyDef):
						Status=str(EnemyName).rstrip()+' Looking for asteroids'
						Enemies[Counter+12]='Looking for asteroids'
						EnemyActive=1
						Message=1
						EnemyDir=random.randint(1, 9)
						if EnemyMaxSpeed >= 10:
							EnemyMoveCounter=10
						else:
							EnemyMoveCounter=EnemyMaxSpeed

					if (-1*EnemyScan <= XDiff) and ( XDiff <= EnemyScan) and (-1*EnemyScan <= YDiff) and (YDiff <= EnemyScan) and running:
						if EnemyHull <= (EnemyLevel*EnemyDef):
							if (-40 <= XDiff) and ( XDiff <= 40) and (-40 <= YDiff) and (YDiff <= 40) and running:
								Status=str(EnemyName).rstrip()+' flees...'
								Enemies[Counter+12]='Running away'
								EnemyActive=1
								Message=1
								EnemyMoveCounter=EnemyMaxSpeed
								if (EnemyX < PlayerX) and (EnemyY < PlayerY):
									EnemyDir=1
								if (EnemyX < PlayerX) and (EnemyY == PlayerY):
									EnemyDir=4
								if (EnemyX < PlayerX) and (EnemyY > PlayerY):
									EnemyDir=7
								if (EnemyX == PlayerX) and (EnemyY > PlayerY):
									EnemyDir=8
								if (EnemyX > PlayerX) and (EnemyY > PlayerY):
									EnemyDir=9
								if (EnemyX > PlayerX) and (EnemyY == PlayerY):
									EnemyDir=6
								if (EnemyX > PlayerX) and (EnemyY < PlayerY):
									EnemyDir=3
								if (EnemyX == PlayerX) and (EnemyY < PlayerY):
									EnemyDir=2
							else:
								Status=str(EnemyName).rstrip()+' scared'
								Enemies[Counter+12]='scared'
								Message=1
								EnemyActive=1
								EnemyDir=random.randint(1, 9)
								if EnemyMaxSpeed >= 10:
									EnemyMoveCounter=10
								else:
									EnemyMoveCounter=EnemyMaxSpeed
						else:
							if (-1*EnemyScan <= XDiff) and ( XDiff <= EnemyScan) and (-1*EnemyScan <= YDiff) and (YDiff <= EnemyScan) and running:
								Status=str(EnemyName).rstrip()+' hunts...'
								if Message==0:
									Enemies[Counter+12]='hunting you'
								EnemyActive=1
								EnemyMoveCounter=EnemyMaxSpeed
								if PDist <= 10:
									EnemyMoveCounter=4
								elif PDist <= 20 and EnemyMaxSpeed >= 10:
									EnemyMoveCounter=10
								elif PDist < EnemyMaxSpeed:
									EnemyMoveCounter=PDist

								if (EnemyX < PlayerX) and (EnemyY < PlayerY):
									EnemyDir=9
								if (EnemyX < PlayerX) and (EnemyY == PlayerY):
									EnemyDir=6
								if (EnemyX < PlayerX) and (EnemyY > PlayerY):
									EnemyDir=3
								if (EnemyX == PlayerX) and (EnemyY > PlayerY):
									EnemyDir=2
								if (EnemyX > PlayerX) and (EnemyY > PlayerY):
									EnemyDir=1
								if (EnemyX > PlayerX) and (EnemyY == PlayerY):
									EnemyDir=4
								if (EnemyX > PlayerX) and (EnemyY < PlayerY):
									EnemyDir=7
								if (EnemyX == PlayerX) and (EnemyY < PlayerY):
									EnemyDir=8
								

						if (EnemyX < 0) and (EnemyY < 0):
							EnemyDir=9
						if (EnemyX < 0) and (0 < EnemyY < 200):
							EnemyDir=6
						if (EnemyX < 0) and (EnemyY > 200):
							EnemyDir=3
						if (0 <EnemyX < 200) and (EnemyY > 200):
							EnemyDir=2
						if (EnemyX > 200) and (EnemyY > 200):
							EnemyDir=1
						if (EnemyX > 200) and (0 < EnemyY < 200):
							EnemyDir=4
						if (EnemyX > 200) and (EnemyY < 0):
							EnemyDir=7
						if (0 < EnemyX < 200) and (EnemyY < 0):
							EnemyDir=8

					
					if EnemyDir!=5:					
						EnemyMove=0
						EnemyAction=EnemyAction+1
						while EnemyMove <= EnemyMoveCounter:
							if EnemyDir==1:
								EnemyX=EnemyX-1
								EnemyY=EnemyY-1
							elif EnemyDir==2:
								EnemyY=EnemyY-1
							elif EnemyDir==3:
								EnemyX=EnemyX+1
								EnemyY=EnemyY-1
							elif EnemyDir==4:
								EnemyX=EnemyX-1
							elif EnemyDir==6:
								EnemyX=EnemyX+1
							elif EnemyDir==7:
								EnemyX=EnemyX-1
								EnemyY=EnemyY+1
							elif EnemyDir==8:
								EnemyY=EnemyY+1
							elif EnemyDir==9:
								EnemyX=EnemyX+1
								EnemyY=EnemyY+1
							Enemies[Counter+10]=EnemyX
							Enemies[Counter+11]=EnemyY
#							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
#							AsteroidCounter=0
#							CrashAsteroid=0
#							EnemyHull=int(Enemies[Counter+6])
#							EnemyMissiles=int(Enemies[Counter+7])
#							AsteroidMaxCounter=len(Asteroids)
#							while AsteroidCounter < AsteroidMaxCounter:
#								AsteroidType=Asteroids[AsteroidCounter]
#								AsteroidX=Asteroids[AsteroidCounter+1]
#								AsteroidY=Asteroids[AsteroidCounter+2]
#								if (EnemyX == AsteroidX) and (EnemyY == AsteroidY):
#									Enemies[Counter+12]='Ate asteroid'
#									Eating.play()
#									CrashAsteroid=AsteroidType
#									WipeCounter=0
#									while WipeCounter < 3:
#										del Asteroids[AsteroidCounter]
#										WipeCounter=WipeCounter+1
#									AsteroidMaxCounter=len(Asteroids)
#									Health=0
#									ExtraMissiles=0
#									if not CrashAsteroid==0:
#										if CrashAsteroid==1:	
#											Health=100
#											ExtraMissiles=1
#										elif CrashAsteroid==2:
#											Health=200
#											ExtraMissiles=2
#										elif CrashAsteroid==3:
#											Health=300
#											ExtraMissiles=3
#										EnemyHull=EnemyHull+Health
#										if EnemyHull > EnemyLevel*100:
#											EnemyHull = EnemyLevel*100
#										EnemyMissiles=EnemyMissiles+ExtraMissiles
#										if EnemyMissiles > EnemyMaxMissiles:
#											EnemyMissiles = EnemyMaxMissiles
#										Status=str(EnemyName).rstrip()+' ate asteroid...'
#										Enemies[Counter+6]=EnemyHull
#										Enemies[Counter+7]=EnemyMissiles
#								AsteroidCounter=AsteroidCounter+3
	
						# Check if player has hit star
							EnemyHull=int(Enemies[Counter+6])
							CrashStar=0
							Damage=0
							Crashed=0
							CrashStar=StarDetect(Stars, EnemyX, EnemyY)
							if not CrashStar==0:
								ExplosionX=EnemyX
								ExplosionY=EnemyY
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
								Status=SetStatus()
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
								MissilePosX=-50
								MissilePosY=-50
								ExplosionX=-50
								ExplosionY=-50
								Enemies[Counter+12]='Hurt by star'
								EnemyActive=1
								if CrashStar==1:
									Damage=100
								elif CrashStar==2:
									Damage=200
								elif CrashStar==3:
									Damage=300
								EnemyHull=EnemyHull-Damage
								if EnemyHull < 1:
									Blast.play()
									screen.blit(SunCrash,(300,300))
									Crashtext=EnemyName+' crashes into star'
									text01 = myfont.render(Crashtext, False, black)
									textEnter='Press enter'
									text02 = myfont.render(textEnter, False, black)
									if CrashStar==1:
										ScreenItemB=RedStar
									elif CrashStar==2:
										ScreenItemB=YellowStar
									elif CrashStar==3:
										ScreenItemB=BlueStar
									ObjectImage=str(Enemies[Counter+2])
									ScreenItemA=GetScreenItem(ObjectImage)
									screen.blit(text01,(300,300))
									screen.blit(text02,(300,680))
									screen.blit(ScreenItemB,(525,475))
									screen.blit(ScreenItemA,(425,475))
									pygame.display.flip()
									wait()
									WipeCounter=0
									while WipeCounter < 13:
										del Enemies[Counter]
										WipeCounter=WipeCounter+1
									MaxCounter=len(Enemies)
									Status=str(EnemyName).rstrip()+' crashes into star'
									break
								else:
									Sizzle.play()
									Enemies[Counter+6]=EnemyHull
									Status=str(EnemyName).rstrip()+' hurt by star'
	
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
		
							EnemyMove=EnemyMove+1
						
						
					

					if EnemyActive==1:
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					else:
						Enemies[Counter+12]='On Patrol'	


					EnemyAction=EnemyAction+1

				Counter=Counter+13




		if PlayerX==WormholeX and PlayerY==WormholeY:
			if EnemyKills >= EnemyKillTarget:
				Teleport.play()
				Level=Level+1
				if Level < 31:
					SLevel=str(Level)
					SPlayerLevel=str(PlayerLevel)
					SPlayerHull=str(int(PlayerHull))
					SPlayerMissiles=str(PlayerMissiles)
					Nexp=int(Exp[0])
					SNexp=str(Nexp)
				else:
					SLevel='1'
					SPlayerLevel='4'
					SPlayerHull='400'
					SPlayerMissiles='4'
					SNexp='0'
				Action=3
				running=False
				LoadList[SaveCounter]=SLevel
				LoadList[SaveCounter+1]=SPlayerLevel
				LoadList[SaveCounter+2]=SPlayerHull
				LoadList[SaveCounter+3]=SPlayerMissiles
				LoadList[SaveCounter+4]=SNexp
				os.system('rm Jumpwar.sav')
				Save=open('Jumpwar.sav', 'a')
#				print('WELCOME TO LEVEL ', SLevel)
				WriteCounter=0
				while WriteCounter < len(LoadList):
					Line=str(LoadList[WriteCounter]).strip()
					SLine=Line+'\n'
					Save.write(SLine)
					WriteCounter=WriteCounter+1
				Save.close()
			else:
				Status='Too many enemies left to advance, press enter'
				ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
				EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
				VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
				DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
				wait()				
			
			
		Action=0
		EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
		VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
		Status=SetStatus()
		DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
			

DoVictory()
sys.exit()



