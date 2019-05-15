# Import necessary modules
import pygame
import sys
import random
import os
import math

 
pygame.mixer.pre_init()
pygame.init()
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

Frigat=pygame.image.load('Frigat.png')
Frigat2=pygame.image.load('Frigat2.png')
Frigat3=pygame.image.load('Frigat3.png')
Frigat4=pygame.image.load('Frigat4.png')
Frigat5=pygame.image.load('Frigat5.png')
Frigat6=pygame.image.load('Frigat6.png')

MissilePlatform=pygame.image.load('MissilePlatform.png')
MissilePlatform2=pygame.image.load('MissilePlatform2.png')

Liberator=pygame.image.load('Liberator.png')

Mothership=pygame.image.load('Mothership.png')

Bomb=pygame.image.load('Bomb.png')
Stop=pygame.image.load('Stop.png')
JGrid = pygame.image.load('JGrid.png')
Galaxy=pygame.image.load('Galaxy.png')
GalaxySmall=pygame.image.load('GalaxySmall.png')

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
	Status = myfont.render('Press enter', False, yellow)		
	text1 = myfont.render('Numpad Numbers or q,w,e,a,d,z,x,c: Jump direction:', False, green)
	text2 = myfont.render('Numpad / or left ctrl                        : Fire Laser', False, green)
	text3 = myfont.render('Numpad 0 or space                          : Fire Missile', False, green)
	text4 = myfont.render('Numpad + and - or r and t                : Set Jump Distance', False, green)
	text5 = myfont.render('Numpad * or l                                   : Closest Enemy Info', False, green)
	text6 = myfont.render('Numpad 5 or s                                  : End Turn', False, green)
	text7 = myfont.render('ESC                                                  : Quit Game', False, green)
	text8 = myfont.render('- Reach the wormhole in the center of the map and skip turns to progress', False, green)
	text9 = myfont.render('- Avoid stars', False, green)
	text10 = myfont.render('- Move over asteroids to regain health and missiles', False, green)
	text11 = myfont.render('- Kill enemies to get EXP and open the wormhole', False, green)
	text12 = myfont.render('Stars (cool/medium/hot)             :', False, green)
	text13 = myfont.render('Asteroids (Small/medium/large):', False, green)
	text14 = myfont.render("- When ship severely damaged, closest asteroid will be shown upper left corner", False, green)
	text15 = myfont.render("- Player has 3 moves before it is the enemie's turn, use this to your advantage... :)", False, green)

#	pygame.display.set_icon(Galaxy)
#	pygame.display.set_caption('Jumpwar')
#	Width=int(1000)
#	Heigth=int(1000)
#	screen = pygame.display.set_mode((Width, Heigth))

	screen.blit(Galaxy,(0,0))
	screen.blit(text1,(0,0))
	screen.blit(text2,(0,50))
	screen.blit(text3,(0,100))
	screen.blit(text4,(0,150))
	screen.blit(text5,(0,200))
	screen.blit(text6,(0,250))
	screen.blit(text7,(0,300))
	screen.blit(text8,(0,400))
	screen.blit(text9,(0,450))
	screen.blit(text10,(0,500))
	screen.blit(text11,(0,550))
	screen.blit(text12,(0,600))
	screen.blit(text13,(0,650))
	screen.blit(text14,(0,700))
	screen.blit(text15,(0,750))

	screen.blit(RedStar,(500,600))
	screen.blit(YellowStar,(560,600))
	screen.blit(BlueStar,(620,600))

	screen.blit(Asteroid,(500,650))
	screen.blit(Asteroid2,(560,650))
	screen.blit(Asteroid3,(620,650))

	screen.blit(Status,(0,960))
	pygame.display.flip()
	Selection=False
	wait()
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


	Save1Status='Save slot 1, level: '+SLevelSave1
	Save2Status='Save slot 2, level: '+SLevelSave2
	Save3Status='Save slot 3, level: '+SLevelSave3
	Save4Status='Save slot 4, level: '+SLevelSave4
	Save5Status='Save slot 5, level: '+SLevelSave5
	Save6Status='Save slot 6, level: '+SLevelSave6


	Save1Text = myfont.render(Save1Status, False, green)
	Save2Text = myfont.render(Save2Status, False, green)
	Save3Text = myfont.render(Save3Status, False, green)
	Save4Text = myfont.render(Save4Status, False, green)
	Save5Text = myfont.render(Save5Status, False, green)
	Save6Text = myfont.render(Save6Status, False, green)
	Status = myfont.render('Or press ESC to quit', False, yellow)
	
	screen.blit(Galaxy,(0,0))
	screen.blit(Save1Text,(0,0))
	screen.blit(Save2Text,(0,50))
	screen.blit(Save3Text,(0,100))
	screen.blit(Save4Text,(0,150))
	screen.blit(Save5Text,(0,200))
	screen.blit(Save6Text,(0,250))
	screen.blit(Status,(0,980))

	pygame.display.flip()

	Selection=False
	while Selection==False:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP1 or event.key == pygame.K_1:
					SaveCounter=0
					Level=int(LoadList[0].rstrip())
					PlayerLevel=int(LoadList[1].rstrip())
					PlayerHull=int(LoadList[2].rstrip())
					PlayerMissiles=int(LoadList[3].rstrip())
					Exp[0]=LoadList[4].rstrip()
					Selection=True
				if event.key == pygame.K_KP2 or event.key == pygame.K_2:
					SaveCounter=5
					Level=int(LoadList[5].rstrip())
					PlayerLevel=int(LoadList[6].rstrip())
					PlayerHull=int(LoadList[7].rstrip())
					PlayerMissiles=int(LoadList[8].rstrip())
					Exp[0]=LoadList[9].rstrip()
					Selection=True
				if event.key == pygame.K_KP3 or event.key == pygame.K_3:
					SaveCounter=10
					Level=int(LoadList[10].rstrip())
					PlayerLevel=int(LoadList[11].rstrip())
					PlayerHull=int(LoadList[12].rstrip())
					PlayerMissiles=int(LoadList[13].rstrip())
					Exp[0]=LoadList[14].rstrip()
					Selection=True
				if event.key == pygame.K_KP4 or event.key == pygame.K_4:
					SaveCounter=15
					Level=int(LoadList[15].rstrip())
					PlayerLevel=int(LoadList[16].rstrip())
					PlayerHull=int(LoadList[17].rstrip())
					PlayerMissiles=int(LoadList[18].rstrip())
					Exp[0]=LoadList[19].rstrip()
					Selection=True
				if event.key == pygame.K_KP5 or event.key == pygame.K_5:
					SaveCounter=20
					Level=int(LoadList[20].rstrip())
					PlayerLevel=int(LoadList[21].rstrip())
					PlayerHull=int(LoadList[22].rstrip())
					PlayerMissiles=int(LoadList[23].rstrip())
					Exp[0]=LoadList[24].rstrip()
					Selection=True
				if event.key == pygame.K_KP6 or event.key == pygame.K_6:
					SaveCounter=25
					Level=int(LoadList[25].rstrip())
					PlayerLevel=int(LoadList[26].rstrip())
					PlayerHull=int(LoadList[27].rstrip())
					PlayerMissiles=int(LoadList[28].rstrip())
					Exp[0]=LoadList[29].rstrip()
					Selection=True
				if event.key == pygame.K_ESCAPE:
					sys.exit()
	DoHelp()
	return

	
LoadGame()
Action=0
ScreenRange=list()
MissileTargetList=list()
LaserTargetList=list()


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
		EnemyX=int(Enemies[Counter+9])
		EnemyY=int(Enemies[Counter+10])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if (-10 <= XDiff) and ( XDiff <= 10) and (-10 <= YDiff) and (YDiff <= 10):
			ScreenRange.append(EnemyType)
			ScreenRange.append(XDiff)
			ScreenRange.append(YDiff)
		Counter=Counter+12
	
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
				AsteroidText=AsteroidName+str(ShowX)+' '+str(ShowY)
		Counter=Counter+3

	return (AsteroidText)

def SetStatus():
	global Exp
	global ExpNeeded
	global Action
	SAction=str(Action+1)
	ExpInt=int(Exp[0])
	NeededInt=int(ExpNeeded)
	PlayerLaserDamage=PlayerLevel*10
	PlayerMissileDamage=PlayerLevel*15
	if PlayerLevel < 20:
		Levelup=' Level up: '
	else:
		Levelup=' Healing: '
	LevelUpProgress=str(int((ExpInt/NeededInt)*100))
	Status='Level: '+str(Level)+' Ship Level: '+str(PlayerLevel)+' Jump Dist: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '+str(int(PlayerHull))+'/'+\
str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+Levelup+LevelUpProgress+'% move: '+SAction+'/3'
	return (Status)

def DoScreen (ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus):
	WXdiff=100-PlayerX
	WYdiff=100-PlayerY
	global WormholeOpenPlayed
	PlayerHealth=str(int((PlayerHull/(PlayerLevel*100))*100))+'%'
	if EnemyKills >= EnemyKillTarget:
		WormholeText='Wormhole open at: '+str(WXdiff)+' '+str(WYdiff)
	else:
		WormholeText='Progress until wormhole open: '+str(int((EnemyKills/EnemyKillTarget)*100))+'%'
	if PlayerHull > PlayerLevel*50 and PlayerMissiles >0:
		StatusColor=green
		AsteroidText='Ship hull '+PlayerHealth
	else:
		if PlayerHull > PlayerLevel*50:
			StatusColor=green
		else:
			StatusColor=red
		AsteroidText=ScanClosestAsteroid(PlayerX, PlayerY)
	textsurface3 = myfont.render(WormholeText, False, StatusColor)
	textsurface4 = myfont.render(AsteroidText, False, StatusColor)
	textsurface = myfont.render(Status, False, StatusColor)
	textsurface2 = myfont.render(EnemyStatus, False, yellow)
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
		elif ObjectImage == 'Stop':
			ScreenItem=Stop
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
		elif ObjectImage == 'HunterDrone\n':
			ScreenItem=HunterDrone
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
		elif ObjectImage == 'Mothership\n':
			ScreenItem=Mothership
		elif ObjectImage == 'Bomb':
			ScreenItem=Bomb
		elif ObjectImage == 'Explosion':
			ScreenItem=Explosion
		XDiff=ScreenRange[Counter+1]
		YDiff=ScreenRange[Counter+2]
		ScreenX=(XDiff+10)*47.5
		YConvert=YDiff*-1
		ScreenY=(YConvert+10)*47.5
		screen.blit(ScreenItem, (ScreenX,ScreenY))
		Counter=Counter+3
	screen.blit(textsurface3,(0,0))
	screen.blit(textsurface4,(0,20))
	screen.blit(textsurface,(0,960))
	screen.blit(textsurface2,(0,940))
	if EnemyKills >= EnemyKillTarget:
		if WormholeOpenPlayed==False:
			screen.blit(GalaxySmall,(300,300))
			textWormhole='Wormhole now open'
			text01 = myfont.render(textWormhole, False, (255, 255, 0))
			textEnter='Press enter'
			text02 = myfont.render(textEnter, False, (255, 255, 0))

			screen.blit(text01,(300,480))
			screen.blit(text02,(300,580))
			Yay.play()
			WormholeOpenPlayed=True
			pygame.display.flip()
			wait()

	pygame.display.flip()
	return

def DoEnemyInfo (Enemies, PlayerX, PlayerY, ClosestEnemy):
	EnemyLevel=int(Enemies[ClosestEnemy])
	EnemyName=str(Enemies[ClosestEnemy+1]).rstrip()
	EnemyDamageLaser=int(Enemies[ClosestEnemy+3])
	EnemyDamageMissile=int(EnemyDamageLaser*1.5)

	EnemyArmor=EnemyLevel*100
	PlayerDamage=PlayerLevel*15
	if EnemyArmor >= PlayerDamage*5:
		Armor='Very heavy'
	elif EnemyArmor >= PlayerDamage*4:
		Armor='Heavy'
	elif EnemyArmor >= PlayerDamage*3:
		Armor='Medium'
	elif EnemyArmor >= PlayerDamage*2:
		Armor='Light'
	else:
		Armor='Very light'

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
	EnemyX=int(Enemies[ClosestEnemy+9])
	EnemyY=int(Enemies[ClosestEnemy+10])
	XDiff=EnemyX-PlayerX
	YDiff=EnemyY-PlayerY
	PDist=PlayerDistance(EnemyX, EnemyY, PlayerX, PlayerY)
	Mood=str(Enemies[ClosestEnemy+11]).rstrip()
	ObjectImage=str(Enemies[ClosestEnemy+2])
	EnemyHealth=str(int((EnemyHull/(EnemyLevel*100))*100))+'%'
	if ObjectImage == 'Drone\n':
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
	elif ObjectImage == 'Mothership\n':
		ScreenItem=Mothership

	textEnemyPic='Enemy        : '
	text01 = myfont.render(textEnemyPic, False, EnemyColor)
	textEnemyName='Name          : '+EnemyName
	text02 = myfont.render(textEnemyName, False, EnemyColor)
	textEnemyDamage='Damage      : '+EnemyDanger
	text03 = myfont.render(textEnemyDamage, False, EnemyColor)
	textEnemySpeed='Speed         : '+EnemySpeed
	text04 = myfont.render(textEnemySpeed, False, EnemyColor)
	textEnemyScan='Scan Range: '+str(EnemyScan)
	text05 = myfont.render(textEnemyScan, False, EnemyColor)
	textEnemyHull='Hull             : '+Armor+' '+EnemyHealth
	text06 = myfont.render(textEnemyHull, False, EnemyColor)
	textEnemyMissiles='Missiles      : '+EnemyMissiles
	text07 = myfont.render(textEnemyMissiles, False, EnemyColor)
	textEnemyPosition='Position      : '+str(XDiff)+' '+str(YDiff)
	text08 = myfont.render(textEnemyPosition, False, EnemyColor)
	textEnemyMood='Status         : '+Mood
	text09 = myfont.render(textEnemyMood, False, EnemyColor)
	text10 = myfont.render('Press enter', False, yellow)

	Width=int(1000)
	Heigth=int(1000)

	Status=SetStatus()

	DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

	screen.blit(GalaxySmall,(300,300))
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

#	pygame.display.set_icon(Galaxy)
#	pygame.display.set_caption('Jumpwar')
#	Width=int(1000)
#	Heigth=int(1000)
#	screen = pygame.display.set_mode((Width, Heigth))
	screen.blit(Galaxy, (0,0))
	screen.blit(text1,(300,300))
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
		EnemyX=int(Enemies[Counter+9])
		EnemyY=int(Enemies[Counter+10])
		Xdiff=EnemyX-PlayerX
		Ydiff=EnemyY-PlayerY
		if (Xdiff==0) and (Ydiff==0):
			EnemyDistance=0
		else:
			EnemyDistance=math.sqrt((Xdiff**2+Ydiff**2))
		if EnemyDistance < SetEnemyDistance:
			SetEnemyDistance=EnemyDistance
			ScanEnemy=Counter
		Counter=Counter+12
	return (ScanEnemy)

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
		EnemyX=int(Enemies[Counter+9])
		EnemyY=int(Enemies[Counter+10])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			if NumberofTargets < 3:
				MissileTargetList.append(Counter)
				MissileTargetList.append(XDiff)
				MissileTargetList.append(YDiff)
				NumberofTargets=NumberofTargets+1
			else:
				break
		Counter=Counter+12
	return (MissileTargetList)

def LaserScan (Enemies, laserTargetList):
	Counter=0
	NumberofTargets=0
	del LaserTargetList[:]
	MaxCounter=len(Enemies)
	while Counter < MaxCounter:
		EnemyX=int(Enemies[Counter+9])
		EnemyY=int(Enemies[Counter+10])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-4) <= XDiff) and ( XDiff <= 4) and ((-4) <= YDiff) and (YDiff <= 4):
			if NumberofTargets < 3:
				laserTargetList.append(Counter)
				laserTargetList.append(XDiff)
				laserTargetList.append(YDiff)
				NumberofTargets=NumberofTargets+1
			else:
				break
		Counter=Counter+12
	return (laserTargetList)

def SelectLaserEnemy (LaserTargetList, Enemies):
	EnemyOneName='empty'
	EnemyTwoName='empty'
	EnemyThreeName='empty'
	Loc1=''
	Loc2=''
	Loc3=''
	FirstEnemy=LaserTargetList[0]
	EnemyOneName=Enemies[FirstEnemy+1]
	Loc1=str(LaserTargetList[1])+' '+str(LaserTargetList[2])
	if len(LaserTargetList) > 3:
		SecondEnemy=LaserTargetList[3]
		EnemyTwoName=Enemies[SecondEnemy+1]
		Loc2=str(LaserTargetList[4])+' '+str(LaserTargetList[5])
		if len(LaserTargetList) > 6:
			ThirdEnemy=LaserTargetList[6]
			EnemyThreeName=Enemies[ThirdEnemy+1]
			Loc3=str(LaserTargetList[7])+' '+str(LaserTargetList[8])
	Status='Target: 1: '+EnemyOneName.rstrip()+' ('+Loc1+') 2: '+EnemyTwoName.rstrip()+' ('+Loc2+') 3: '+EnemyThreeName.rstrip()+' ('+Loc3+')'
	VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
	DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
	Selection=False
	while Selection==False:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP1 or event.key == pygame.K_1:
					LaserTarget=LaserTargetList[0]
					Selection=True
				if event.key == pygame.K_KP2 or event.key == pygame.K_2:
					if len(LaserTargetList) > 3:
						LaserTarget=LaserTargetList[3]
						Selection=True
				if event.key == pygame.K_KP3 or event.key == pygame.K_3:
					if len(LaserTargetList) > 6:
						LaserTarget=LaserTargetList[6]
						Selection=True
	return(LaserTarget)


def SelectMissileEnemy (MissileTargetList, Enemies):
	EnemyOneName='empty'
	EnemyTwoName='empty'
	EnemyThreeName='empty'
	Loc1=''
	Loc2=''
	Loc3=''
	FirstEnemy=MissileTargetList[0]
	Loc1=str(MissileTargetList[1])+' '+str(MissileTargetList[2])
	EnemyOneName=Enemies[FirstEnemy+1]
	if len(MissileTargetList) > 3:
		SecondEnemy=MissileTargetList[3]
		EnemyTwoName=Enemies[SecondEnemy+1]
		Loc2=str(MissileTargetList[4])+' '+str(MissileTargetList[5])
		if len(MissileTargetList) > 6:
			ThirdEnemy=MissileTargetList[6]
			EnemyThreeName=Enemies[ThirdEnemy+1]
			Loc3=str(MissileTargetList[7])+' '+str(MissileTargetList[8])
	Status='Target: 1: '+EnemyOneName.rstrip()+' ('+Loc1+') 2: '+EnemyTwoName.rstrip()+' ('+Loc2+') 3: '+EnemyThreeName.rstrip()+' ('+Loc3+')'
	VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
	DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
	Selection=False
	while Selection==False:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP1 or event.key == pygame.K_1:
					MissileTarget=MissileTargetList[0]
					Selection=True
				if event.key == pygame.K_KP2 or event.key == pygame.K_2:
					if len(MissileTargetList) > 3:
						MissileTarget=MissileTargetList[3]
						Selection=True
				if event.key == pygame.K_KP3 or event.key == pygame.K_3:
					if len(MissileTargetList) > 6:
						MissileTarget=MissileTargetList[6]
						Selection=True
	return(MissileTarget)
		
			
def GetEnemyStatus (Enemies, PlayerX, PlayerY, ClosestEnemy):
	EnemyDistance=1000000
	if ClosestEnemy > (len(Enemies)*10):
		EnemyStatus='No enemies'
	else:
		EnemyX=int(Enemies[ClosestEnemy+9])
		EnemyY=int(Enemies[ClosestEnemy+10])
		XDiff=EnemyX-PlayerX
		YDiff=EnemyY-PlayerY
		if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
			if ((-4) <= XDiff) and ( XDiff <= 4) and ((-4) <= YDiff) and (YDiff <= 4):
				EnemyStatus=str(Enemies[ClosestEnemy+1]).rstrip()+' at: '+str(XDiff)+' '+str(YDiff)+' LASER LOCK'
			else:
				if PlayerMissiles > 0:
					EnemyStatus=str(Enemies[ClosestEnemy+1]).rstrip()+' at: '+str(XDiff)+' '+str(YDiff)+' MISSILE LOCK'
				else:
					EnemyStatus=str(Enemies[ClosestEnemy+1]).rstrip()+' at: '+str(XDiff)+' '+str(YDiff)+' NO MISSILES'
		else:
			EnemyStatus=str(Enemies[ClosestEnemy+1]).rstrip()+' at: '+str(XDiff)+' '+str(YDiff)+' OUT OF RANGE'
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
		EnemyXp=int(Enemies[MissileTarget])
		EnemyKills=EnemyKills+EnemyXp
		Nexp=Nexp+EnemyXp
		Exp[0]=Nexp
		Counter=0
		while Counter < 12:
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
		EnemyXp=int(Enemies[LaserTarget])
		EnemyKills=EnemyKills+EnemyXp
		Nexp=Nexp+EnemyXp
		Exp[0]=Nexp
		Counter=0
		while Counter < 12:
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
	ExpNeeded=PlayerLevel*4
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
		Enemylevel=int(Enemylist[Counter])
		NumberofRepeats=int(Level / Enemylevel)
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
			EnemyX=random.randint(1,200)
			EnemyY=random.randint(1,200)
			Enemies.append(EnemyX)
			Enemies.append(EnemyY)
			Enemies.append('On patrol')
			GeneratedEnemies=GeneratedEnemies+int(Enemylist[Counter])
			EnemyCounter=EnemyCounter+1
		Counter=Counter+8
	EnemyKills=0
	EnemyKillTarget=int(GeneratedEnemies*0.3)
	if EnemyKillTarget==0 and len(Enemies)>0:
		EnemyKillTarget=1
	NumberofEnemies=int(len(Enemies)/11)
#	print('Nomber of enemies: ',NumberofEnemies)

	NewLevel(Level)
	WormholeOpenPlayed=False
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
	while running==True:
#		print('-Player-')
		Action=0
		ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
#		print(ClosestEnemy)
		while Action < 3:
#			print('Playerturn: ', Action)
			EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
			ScreenAction=False
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					Direction=5
					if event.key == pygame.K_KP1 or event.key == pygame.K_z:
						Direction=1
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP2 or event.key == pygame.K_x:
						Direction=2
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP3 or event.key == pygame.K_c:
						Direction=3
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP4 or event.key == pygame.K_a:
						Direction=4
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP5 or event.key == pygame.K_s:
						Direction=5
						Action=3
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP6 or event.key == pygame.K_d:
						Direction=6
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP7 or event.key == pygame.K_q:
						Direction=7
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP8 or event.key == pygame.K_w:
						Direction=8
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP9 or event.key == pygame.K_e:
						Direction=9
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
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
								MissileTargetX=int(Enemies[MissileTarget+9])
								MissileTargetY=int(Enemies[MissileTarget+10])
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
							LaserTargetX=int(Enemies[LaserTarget+9])
							LaserTargetY=int(Enemies[LaserTarget+10])
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
							ScreenAction=True
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
					elif event.key == pygame.K_KP_MULTIPLY or event.key == pygame.K_l:
						DoEnemyInfo(Enemies, PlayerX, PlayerY, ClosestEnemy)
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
	
						if ScreenAction==True:
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
			ExpNeeded=PlayerLevel*4
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

		if len(Enemies) > 0 and running==True:
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
			while Counter < MaxCounter and running==True:
				EnemyActive=False
				Fleeing=False
				LaserFired=False
				MissileFired=False
				EnemyMoves=False
				EnemyName=str(Enemies[Counter+1]).rstrip()
				#print(EnemyName)
				Enemies[Counter+11]='On patrol'
				EnemyAction=0
				while EnemyAction < 2:
					EnemyLevel=int(Enemies[Counter])
					EnemyName=str(Enemies[Counter+1]).rstrip()
					EnemyHull=int(Enemies[Counter+6])
					EnemyScan=int(Enemies[Counter+5])
					EnemyMaxSpeed=int(Enemies[Counter+4])
					EnemyMaxMissiles=int(Enemies[Counter+8])
					EnemyX=int(Enemies[Counter+9])
					EnemyY=int(Enemies[Counter+10])
					XDiff=PlayerX-EnemyX
					YDiff=PlayerY-EnemyY
					if EnemyHull < (EnemyLevel*30):
						Enemies[Counter+11]='Scared'
					if (-4 <= XDiff) and ( XDiff <= 4) and (-4 <= YDiff) and (YDiff <= 4) and running==True:
						if LaserFired==False:
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyActive=True
							EnemyLaserDamage=int(Enemies[Counter+3])
							PlayerHull=PlayerHull-EnemyLaserDamage
							Enemies[Counter+11]='Fired laser'
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
							LaserFired=True
					if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20) and running==True:
						EnemyMissiles=int(Enemies[Counter+7])
						if EnemyMissiles > 0:
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyActive=True
							if MissileFired==False:
								if EnemyName=='Mothership A':
									#print('enemy appended')
									Enemies.append('3')
									Enemies.append('Hunter Drone\n')
									Enemies.append('HunterDrone\n')
									Enemies.append('70')
									Enemies.append('12')
									Enemies.append('30')
									Enemies.append('300')
									Enemies.append('3')
									Enemies.append('3')
									OffSetX=EnemyY+random.randint(-1,1)
									OffSetY=EnemyY+random.randint(-1,1)
									Enemies.append(OffSetX)
									Enemies.append(OffSetY)
									Enemies.append('On patrol')
									MaxCounter=len(Enemies)
									Launch.play()
									Status='Mothership A launches Hunter Drone...'
									Enemies[Counter+11]='Launched a drone'
									EnemyMissiles=EnemyMissiles-1
									Enemies[Counter+7]=EnemyMissiles
									EnemyAction=EnemyAction+1
								else:
									MissileTargetX=PlayerX
									MissileTargetY=PlayerY
									MissilePosX=int(Enemies[Counter+9])
									MissilePosY=int(Enemies[Counter+10])
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
									Enemies[Counter+11]='Fired a missile'
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
								MissileFired=True
								Status=str(EnemyName).rstrip()+' fires missile...'
					if EnemyHull < (EnemyLevel*30) and running==True:
						Fleeing=True
						AsteroidScan=[None]*4
						AsteroidScan=ScanAsteroid(EnemyX, EnemyY)
						if not AsteroidScan[0]==None:
							Enemies[Counter+11]='Ate an asteroid'
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
								Enemies[Counter+9]=EnemyX
								Enemies[Counter+10]=EnemyY
								WipeCounter=0
								Status=str(EnemyName).rstrip()+' ate asteroid'
								while WipeCounter < 3:
									del Asteroids[AsteroidCounter]
									WipeCounter=WipeCounter+1
								AsteroidMaxCounter=len(Asteroids)
							EnemyAction=EnemyAction+1

					PDist=PlayerDistance(EnemyX, EnemyY, PlayerX, PlayerY)
					if (-1*EnemyScan <= XDiff) and ( XDiff <= EnemyScan) and (-1*EnemyScan <= YDiff) and (YDiff <= EnemyScan) and running==True:
						if EnemyHull <= (EnemyLevel*30):
							if (-30 <= XDiff) and ( XDiff <= 30) and (-30 <= YDiff) and (YDiff <= 30) and running==True:
								Status=str(EnemyName).rstrip()+' flees...'
								Enemies[Counter+11]='Running away'
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
							if (-1*EnemyScan <= XDiff) and ( XDiff <= EnemyScan) and (-1*EnemyScan <= YDiff) and (YDiff <= EnemyScan) and running==True:
								Status=str(EnemyName).rstrip()+' hunts...'
								Enemies[Counter+11]='hunting you'
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

						EnemyMoveCounter=EnemyMaxSpeed
						if EnemyHull > (EnemyLevel*30):
							if PDist <= 10:
								EnemyMoveCounter=4
							elif PDist <= 20 and EnemyMaxSpeed >= 10:
								EnemyMoveCounter=10
							elif PDist < EnemyMaxSpeed:
								EnemyMoveCounter=PDist

					
						if EnemyMoves==False:					
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

								Enemies[Counter+9]=EnemyX
								Enemies[Counter+10]=EnemyY
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								AsteroidCounter=0
								CrashAsteroid=0
								EnemyHull=int(Enemies[Counter+6])
								EnemyMissiles=int(Enemies[Counter+7])
								AsteroidMaxCounter=len(Asteroids)
								while AsteroidCounter < AsteroidMaxCounter:
									AsteroidType=Asteroids[AsteroidCounter]
									AsteroidX=Asteroids[AsteroidCounter+1]
									AsteroidY=Asteroids[AsteroidCounter+2]
									if (EnemyX == AsteroidX) and (EnemyY == AsteroidY):
										Enemies[Counter+11]='Ate asteroid'
										Eating.play()
										CrashAsteroid=AsteroidType
										WipeCounter=0
										while WipeCounter < 3:
											del Asteroids[AsteroidCounter]
											WipeCounter=WipeCounter+1
										AsteroidMaxCounter=len(Asteroids)
										Health=0
										ExtraMissiles=0
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
											if EnemyHull > EnemyLevel*100:
												EnemyHull = EnemyLevel*100
											EnemyMissiles=EnemyMissiles+ExtraMissiles
											if EnemyMissiles > EnemyMaxMissiles:
												EnemyMissiles = EnemyMaxMissiles
											Status=str(EnemyName).rstrip()+' ate asteroid...'
											Enemies[Counter+6]=EnemyHull
											Enemies[Counter+7]=EnemyMissiles
									AsteroidCounter=AsteroidCounter+3
	
							# Check if player has hit star
								EnemyHull=int(Enemies[Counter+6])
								CrashStar=0
								Damage=0
								Crashed=False
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
									Enemies[Counter+11]='Hurt by star'
									if CrashStar==1:
										Damage=100
									elif CrashStar==2:
										Damage=200
									elif CrashStar==3:
										Damage=300
									EnemyHull=EnemyHull-Damage
									if EnemyHull < 1:
										Blast.play()
										WipeCounter=0
										while WipeCounter < 12:
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
							
							EnemyMoves=True
						
					

					if EnemyActive==True:
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=GetEnemyStatus(Enemies, PlayerX, PlayerY, ClosestEnemy)
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY, ExplosionX, ExplosionY)
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

					EnemyAction=EnemyAction+1

				Counter=Counter+12




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



