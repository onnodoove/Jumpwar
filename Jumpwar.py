# Import necessary modules
import pygame
import sys
import random
import os
import math

 
pygame.init()
pygame.font.init()
pygame.mixer.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
Exp=[0]

Load=open('Jumpwar.txt', 'r')
LoadList=list(Load)
Load.close()
LevelSave1=int(LoadList[0].rstrip())
LevelSave2=int(LoadList[3].rstrip())
LevelSave3=int(LoadList[6].rstrip())
LevelSave4=int(LoadList[9].rstrip())
LevelSave5=int(LoadList[12].rstrip())
LevelSave6=int(LoadList[15].rstrip())


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


Save1Text = myfont.render(Save1Status, False, (255, 255, 0))
Save2Text = myfont.render(Save2Status, False, (255, 255, 0))
Save3Text = myfont.render(Save3Status, False, (255, 255, 0))
Save4Text = myfont.render(Save4Status, False, (255, 255, 0))
Save5Text = myfont.render(Save5Status, False, (255, 255, 0))
Save6Text = myfont.render(Save6Status, False, (255, 255, 0))

logo = pygame.image.load('Galaxy.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('Jumpwar')
Width=int(1000)
Heigth=int(1000)
screen = pygame.display.set_mode((Width, Heigth))

screen.blit(logo,(0,0))
screen.blit(Save1Text,(0,0))
screen.blit(Save2Text,(0,50))
screen.blit(Save3Text,(0,100))
screen.blit(Save4Text,(0,150))
screen.blit(Save5Text,(0,200))
screen.blit(Save6Text,(0,250))


pygame.display.flip()

Selection=False
while Selection==False:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP1:
				SaveCounter=0
				Level=int(LoadList[0].rstrip())
				PlayerLevel=int(LoadList[1].rstrip())
				Exp[0]=LoadList[2].rstrip()
				Selection=True
			if event.key == pygame.K_KP2:
				SaveCounter=3
				Level=int(LoadList[3].rstrip())
				PlayerLevel=int(LoadList[4].rstrip())
				Exp[0]=LoadList[5].rstrip()
				Selection=True
			if event.key == pygame.K_KP3:
				SaveCounter=6
				Level=int(LoadList[6].rstrip())
				PlayerLevel=int(LoadList[7].rstrip())
				Exp[0]=LoadList[8].rstrip()
				Selection=True
			if event.key == pygame.K_KP4:
				SaveCounter=9
				Level=int(LoadList[9].rstrip())
				PlayerLevel=int(LoadList[10].rstrip())
				Exp[0]=LoadList[11].rstrip()
				Selection=True
			if event.key == pygame.K_KP5:
				SaveCounter=12
				Level=int(LoadList[12].rstrip())
				PlayerLevel=int(LoadList[13].rstrip())
				Exp[0]=LoadList[14].rstrip()
				Selection=True
			if event.key == pygame.K_KP3:
				SaveCounter=15
				Level=int(LoadList[15].rstrip())
				PlayerLevel=int(LoadList[16].rstrip())
				Exp[0]=LoadList[17].rstrip()
				Selection=True

ScreenRange=list()
MissileTargetList=list()
LaserTargetList=list()


def wait():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER:
	                		return
	
def DoHelp ():
	Status = myfont.render('Press enter', False, (255, 255, 0))		
	text1 = myfont.render('Numpad Numbers: Jump direction:', False, (255, 255, 0))
	text2 = myfont.render('Numpad /      : Fire Laser', False, (255, 255, 0))
	text3 = myfont.render('Numpad 0      : Fire Missile', False, (255, 255, 0))
	text4 = myfont.render('Numpad + and -: Set Jump Distance', False, (255, 255, 0))
	text5 = myfont.render('Numpad *      : Legend', False, (255, 255, 0))
	text6 = myfont.render('Numpad 5      : Skip Turn', False, (255, 255, 0))
	text7 = myfont.render('ESC           : Quit Game', False, (255, 255, 0))
	text8 = myfont.render('- Reach the wormhole in the center of the map and skip turns to progress', False, (255, 255, 0))
	text9 = myfont.render('- Avoid stars', False, (255, 255, 0))
	text10 = myfont.render('- Move over asteroids to regain health and missiles', False, (255, 255, 0))
	text11 = myfont.render('- Kill enemies to get EXP and level up', False, (255, 255, 0))
	text12 = myfont.render('- Enter=Numpad Enter', False, (255, 255, 0))

	logo = pygame.image.load('Galaxy.png')
	pygame.display.set_icon(logo)
	pygame.display.set_caption('Jumpwar')
	Width=int(1000)
	Heigth=int(1000)
	screen = pygame.display.set_mode((Width, Heigth))

	screen.blit(logo,(0,0))
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

	screen.blit(Status,(0,980))
	pygame.display.flip()
	wait()
	return

DoHelp()
SpeedSetting=3
CXdiff=200
CYdiff=200
ClosestAsteroid=[200, 200]
CollideStar=list()
ClosestEnemy=list()
Stars=list()
Asteroids=list()
Enemies=list()
ScreenRange=list()
while Level < 22:
	PlayerDamage=PlayerLevel*10
	PlayerHull=PlayerLevel*100
	PlayerMissiles=PlayerLevel
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
	Counter=0
	MaxCounter=len(Enemylist)
	while Counter < MaxCounter:
		Enemy=Enemylist[Counter].rstrip()
		Enemylevel=int(Enemy)
		NumerofRepeats=int(Level / Enemylevel)
		if NumerofRepeats > 10:
			NumerofRepeats=10
		if not NumerofRepeats == 0:
			for Item in range(1, NumerofRepeats):
				Enemies.append(Enemylist[Counter])
				Enemies.append(Enemylist[Counter+1])
				Enemies.append(Enemylist[Counter+2])
				Enemies.append(Enemylist[Counter+3])
				Enemies.append(Enemylist[Counter+4])
				Enemies.append(Enemylist[Counter+5])
				Enemies.append(Enemylist[Counter+6])
				Enemies.append(Enemylist[Counter+7])
				EnemyX=random.randint(1,200)
				EnemyY=random.randint(1,200)
				Enemies.append(EnemyX)
				Enemies.append(EnemyY)
		Counter=Counter+8

	def VisualScan (Stars, Asteroids, Enemies, MissilePosX, MissilePosY):
		del ScreenRange[:]
		# Get items in range of screen
		XDiff=MissilePosX-PlayerX
		YDiff=MissilePosY-PlayerY
		ScreenRange.append('Bomb')
		ScreenRange.append(XDiff)
		ScreenRange.append(YDiff)
		
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
			AsteroidsType=Asteroids[Counter]
			AsteroidsX=Asteroids[Counter+1]
			AsteroidsY=Asteroids[Counter+2]
			XDiff=AsteroidsX-PlayerX
			YDiff=AsteroidsY-PlayerY
			if (-10 <= XDiff) and ( XDiff <= 10) and (-10 <= YDiff) and (YDiff <= 10):
				AsteroidsImage='Asteroid'
				ScreenRange.append(AsteroidsImage)
				ScreenRange.append(XDiff)
				ScreenRange.append(YDiff)
			Counter=Counter+3
		
		# Then enemies
		Counter=0
		MaxCounter=len(Enemies)
		while Counter < MaxCounter:
			EnemyType=Enemies[Counter+2]
			EnemyX=int(Enemies[Counter+8])
			EnemyY=int(Enemies[Counter+9])
			XDiff=EnemyX-PlayerX
			YDiff=EnemyY-PlayerY
			if (-10 <= XDiff) and ( XDiff <= 10) and (-10 <= YDiff) and (YDiff <= 10):
				ScreenRange.append(EnemyType)
				ScreenRange.append(XDiff)
				ScreenRange.append(YDiff)
			Counter=Counter+10
	
		# Then Wormhole
		XDiff=WormholeX-PlayerX
		YDiff=WormholeY-PlayerY
		if (-10 <= XDiff) and ( XDiff <= 10) and (-10 <= YDiff) and (YDiff <= 10):
			ScreenRange.append('Wormhole')
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


	def DoScreen (ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus):
		textsurface = myfont.render(Status, False, (255, 255, 0))
		textsurface2 = myfont.render(EnemyStatus, False, (255, 255, 0))
		logo = pygame.image.load('JGrid.png')
		if PlayerHull > PlayerLevel*50:
			PlayerImage=pygame.image.load('Happy.png')
		elif PlayerHull > 0:
			PlayerImage=pygame.image.load('Sad.png')
		else:
			PlayerImage=pygame.image.load('Blast.png')
		pygame.display.set_icon(logo)
		pygame.display.set_caption('Jumpwar')
		Width=int(1000)
		Heigth=int(1000)
		screen = pygame.display.set_mode((Width, Heigth))
		screen.blit(logo, (0,0))
		screen.blit(PlayerImage, (475,475))
		pygame.display.flip()
		Counter=0
		MaxCounter=len(ScreenRange)
		while Counter < MaxCounter:
			ObjectImage=ScreenRange[Counter]
			if ObjectImage == 'RedStar':
				ScreenItem=pygame.image.load('RedStar.png')
			elif ObjectImage == 'YellowStar':
				ScreenItem=pygame.image.load('YellowStar.png')
			elif ObjectImage == 'BlueStar':
				ScreenItem=pygame.image.load('BlueStar.png')
			elif ObjectImage == 'Asteroid':
				ScreenItem=pygame.image.load('Asteroid.png')
			elif ObjectImage == 'Wormhole':
				ScreenItem=pygame.image.load('Wormhole.png')
			elif ObjectImage == 'Drone\n':
				ScreenItem=pygame.image.load('Drone.png')
			elif ObjectImage == 'Drone2\n':
				ScreenItem=pygame.image.load('Drone2.png')
			elif ObjectImage == 'Drone3\n':
				ScreenItem=pygame.image.load('Drone3.png')
			elif ObjectImage == 'Drone4\n':
				ScreenItem=pygame.image.load('Drone4.png')
			elif ObjectImage == 'Drone5\n':
				ScreenItem=pygame.image.load('Drone5.png')
			elif ObjectImage == 'Interceptor\n':
				ScreenItem=pygame.image.load('Interceptor.png')
			elif ObjectImage == 'Interceptor3\n':
				ScreenItem=pygame.image.load('Interceptor3.png')
			elif ObjectImage == 'Interceptor4\n':
				ScreenItem=pygame.image.load('Interceptor4.png')
			elif ObjectImage == 'Interceptor5\n':
				ScreenItem=pygame.image.load('Interceptor5.png')
			elif ObjectImage == 'Frigat\n':
				ScreenItem=pygame.image.load('Frigat.png')
			elif ObjectImage == 'Frigat4\n':
				ScreenItem=pygame.image.load('Frigat4.png')
			elif ObjectImage == 'Frigat5\n':
				ScreenItem=pygame.image.load('Frigat5.png')
			elif ObjectImage == 'MissilePlatform\n':
				ScreenItem=pygame.image.load('MissilePlatform.png')
			elif ObjectImage == 'Liberator\n':
				ScreenItem=pygame.image.load('Liberator.png')
			elif ObjectImage == 'Mothership\n':
				ScreenItem=pygame.image.load('Mothership.png')
			elif ObjectImage == 'Bomb':
				ScreenItem=pygame.image.load('Bomb.png')
			XDiff=ScreenRange[Counter+1]
			YDiff=ScreenRange[Counter+2]
			ScreenX=(XDiff+10)*47.5
			YConvert=YDiff*-1
			ScreenY=(YConvert+10)*47.5
			screen.blit(ScreenItem, (ScreenX,ScreenY))
			Counter=Counter+3
		screen.blit(textsurface,(0,980))
		screen.blit(textsurface2,(0,960))
		pygame.display.flip()
		return

	def DoLegend ():
		Status = myfont.render('Press enter', False, (255, 255, 0))		
		textAsteroid = myfont.render('Asteroid:', False, (255, 255, 0))
		textStars = myfont.render('Stars:', False, (255, 255, 0))
		textDrones = myfont.render('Drones:', False, (255, 255, 0))
		textInterceptors = myfont.render('Interceptors:', False, (255, 255, 0))
		textFrigats = myfont.render('Frigats:', False, (255, 255, 0))
		textMissilePlatforms = myfont.render('Missile Platforms:', False, (255, 255, 0))
		textMothership = myfont.render('Mothership:', False, (255, 255, 0))
		textWormhole = myfont.render('Wormhole:', False, (255, 255, 0))

		logo = pygame.image.load('JGrid.png')
		pygame.display.set_icon(logo)
		pygame.display.set_caption('Jumpwar')
		Width=int(1000)
		Heigth=int(1000)
		screen = pygame.display.set_mode((Width, Heigth))


		screen.blit(textAsteroid,(0,0))
		ScreenItem=pygame.image.load('Asteroid.png')
		screen.blit(ScreenItem, (0,50))

		screen.blit(textStars,(0,100))
		ScreenItem=pygame.image.load('RedStar.png')
		screen.blit(ScreenItem, (0,150))
		ScreenItem=pygame.image.load('YellowStar.png')
		screen.blit(ScreenItem, (50,150))
		ScreenItem=pygame.image.load('BlueStar.png')
		screen.blit(ScreenItem, (100,150))

		screen.blit(textDrones,(0,200))
		ScreenItem=pygame.image.load('Drone.png')
		screen.blit(ScreenItem, (0,250))
		ScreenItem=pygame.image.load('Drone2.png')
		screen.blit(ScreenItem, (50,250))
		ScreenItem=pygame.image.load('Drone3.png')
		screen.blit(ScreenItem, (100,250))
		ScreenItem=pygame.image.load('Drone4.png')
		screen.blit(ScreenItem, (150,250))
		ScreenItem=pygame.image.load('Drone5.png')
		screen.blit(ScreenItem, (200,250))

		screen.blit(textInterceptors,(0,300))
		ScreenItem=pygame.image.load('Interceptor.png')
		screen.blit(ScreenItem, (0,350))
		ScreenItem=pygame.image.load('Interceptor3.png')
		screen.blit(ScreenItem, (50,350))
		ScreenItem=pygame.image.load('Interceptor4.png')
		screen.blit(ScreenItem, (100,350))
		ScreenItem=pygame.image.load('Interceptor5.png')
		screen.blit(ScreenItem, (150,350))

		screen.blit(textFrigats,(0,400))
		ScreenItem=pygame.image.load('Frigat.png')
		screen.blit(ScreenItem, (0,450))
		ScreenItem=pygame.image.load('Frigat4.png')
		screen.blit(ScreenItem, (50,450))
		ScreenItem=pygame.image.load('Frigat5.png')
		screen.blit(ScreenItem, (100,450))

		screen.blit(textMissilePlatforms,(0,500))
		ScreenItem=pygame.image.load('MissilePlatform.png')
		screen.blit(ScreenItem, (0,550))

		screen.blit(textMothership,(0,600))
		ScreenItem=pygame.image.load('Mothership.png')
		screen.blit(ScreenItem, (0,650))

		screen.blit(textWormhole,(0,700))
		ScreenItem=pygame.image.load('Wormhole.png')
		screen.blit(ScreenItem, (0,750))

		screen.blit(Status,(0,980))
		pygame.display.flip()
		wait()
		return

	def NewLevel (Level):
		Status = myfont.render('Press enter', False, (255, 255, 0))		
		text1 = myfont.render('Welcome to Level: '+str(Level), False, (255, 255, 0))

		logo = pygame.image.load('Galaxy.png')
		pygame.display.set_icon(logo)
		pygame.display.set_caption('Jumpwar')
		Width=int(1000)
		Heigth=int(1000)
		screen = pygame.display.set_mode((Width, Heigth))
		screen.blit(logo, (0,0))
		screen.blit(text1,(300,300))
		screen.blit(Status,(0,980))
		pygame.display.flip()
		wait()
		return

	def DoVictory ():
		Status = myfont.render('Press enter', False, (255, 255, 0))		
		text1 = myfont.render('Congratulations on beating Jumpwar!', False, (255, 255, 0))

		logo = pygame.image.load('Galaxy.png')
		pygame.display.set_icon(logo)
		pygame.display.set_caption('Jumpwar')
		Width=int(1000)
		Heigth=int(1000)
		screen = pygame.display.set_mode((Width, Heigth))
		screen.blit(logo, (0,0))
		screen.blit(text1,(300,300))
		screen.blit(Status,(0,980))
		pygame.display.flip()
		wait()
		return


	def ScanEnemies (Enemies, PlayerX, PlayerY, Radar, ScanEnemy):
		Counter=0
		SetEnemyDistance=20000000
		MaxCounter=len(Enemies)
		WdiffX=100-PlayerX
		WdiffY=100-PlayerY
		while Counter < MaxCounter:
			EnemyLevel=int(Enemies[Counter])
			EnemyName=Enemies[Counter+1]
			EnemyHealth=Enemies[Counter+6]
			EnemyX=int(Enemies[Counter+8])
			EnemyY=int(Enemies[Counter+9])
			Xdiff=EnemyX-PlayerX
			Ydiff=EnemyY-PlayerY
			if ((-1*Radar) <= Xdiff <= Radar) and ((-1*Radar) <= Ydiff <= Radar):
				if (Xdiff==0) and (Ydiff==0):
					EnemyDistance=0
				else:
					EnemyDistance=math.sqrt((Xdiff**2+Ydiff**2))
				if EnemyDistance < SetEnemyDistance:
					SetEnemyDistance=EnemyDistance
					ScanEnemy[0]=EnemyName
					ScanEnemy[1]=EnemyHealth
					ScanEnemy[2]=Xdiff
					ScanEnemy[3]=Ydiff
			Counter=Counter+10
		if SetEnemyDistance==20000000:
			ScanEnemy[0]='Wormhole'
			ScanEnemy[1]='N/A'
			ScanEnemy[2]=WdiffX
			ScanEnemy[3]=WdiffY
		return (ScanEnemy)

	def MissileScan (Enemies, MissileTargetList, PlayerScan):
		Counter=0
		NumberofTargets=0
		del MissileTargetList[:]
		MaxCounter=len(Enemies)
		while Counter < MaxCounter:
			EnemyX=int(Enemies[Counter+8])
			EnemyY=int(Enemies[Counter+9])
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
			Counter=Counter+10
		return (MissileTargetList)

	def LaserScan (Enemies, laserTargetList):
		Counter=0
		NumberofTargets=0
		del LaserTargetList[:]
		MaxCounter=len(Enemies)
		while Counter < MaxCounter:
			EnemyX=int(Enemies[Counter+8])
			EnemyY=int(Enemies[Counter+9])
			XDiff=EnemyX-PlayerX
			YDiff=EnemyY-PlayerY
			if ((-4) <= XDiff) and ( XDiff <= 4) and ((-4) <= YDiff) and (YDiff <= 4):
				if NumberofTargets < 3:
					laserTargetList.append(Counter)
					NumberofTargets=NumberofTargets+1
				else:
					break
			Counter=Counter+10
		return (laserTargetList)

	def SelectLaserEnemy (LaserTargetList, Enemies):
		EnemyOneName='empty'
		EnemyTwoName='empty'
		EnemyThreeName='empty'
		FirstEnemy=LaserTargetList[0]
		EnemyOneName=Enemies[FirstEnemy+1]
		if len(LaserTargetList) > 1:
			SecondEnemy=LaserTargetList[1]
			EnemyTwoName=Enemies[SecondEnemy+1]
			if len(LaserTargetList) > 2:
				ThirdEnemy=LaserTargetList[2]
				EnemyThreeName=Enemies[ThirdEnemy+1]
		Status='Select laser target: 1: '+EnemyOneName.rstrip()+' 2: '+EnemyTwoName.rstrip()+' 3: '+EnemyThreeName.rstrip()
		VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
		DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
		Selection=False
		while Selection==False:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					LaserTarget=LaserTargetList[0]
					if event.key == pygame.K_KP1:
						LaserTarget=LaserTargetList[0]
						Selection=True
					if event.key == pygame.K_KP2:
						if len(LaserTargetList) > 1:
							LaserTarget=LaserTargetList[1]
						Selection=True
					if event.key == pygame.K_KP3:
						if len(LaserTargetList) > 2:
							LaserTarget=LaserTargetList[2]
						Selection=True
					if event.key == pygame.K_KP_MULTIPLY:
						DoLegend()
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
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
		Status='Missile target: 1: '+EnemyOneName.rstrip()+' ('+Loc1+') 2: '+EnemyTwoName.rstrip()+' ('+Loc2+') 3: '+EnemyThreeName.rstrip()+' ('+Loc3+')'
		VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
		DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
		Selection=False
		while Selection==False:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					MissileTarget=MissileTargetList[0]
					if event.key == pygame.K_KP1:
						MissileTarget=MissileTargetList[0]
						Selection=True
					if event.key == pygame.K_KP2:
						if len(MissileTargetList) > 3:
							MissileTarget=MissileTargetList[3]
						Selection=True
					if event.key == pygame.K_KP3:
						if len(MissileTargetList) > 6:
							MissileTarget=MissileTargetList[6]
						Selection=True
					if event.key == pygame.K_KP_MULTIPLY:
						DoLegend()
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
		return(MissileTarget)
		
			


	def FireMissile (Enemies, Stars, Asteroids, MissileTarget, PlayerLevel, Exp, Nexp):
		Nexp=int(Exp[0])
		PlayerMissileDamage=PlayerLevel*15
		SPlayerMissileDamage=str(PlayerMissileDamage)
		EnemyName=Enemies[MissileTarget+1]
		EnemyHull=int(Enemies[MissileTarget+6])
		EnemyHull=EnemyHull-PlayerMissileDamage
		if EnemyHull < 1:
			EnemyXp=int(Enemies[MissileTarget])
			Nexp=Nexp+EnemyXp
			Exp[0]=Nexp
			Counter=0
			while Counter < 10:
				del Enemies[MissileTarget]
				Counter=Counter+1
			pygame.mixer.music.load('Boom.wav')
			pygame.mixer.music.play()
			Status=EnemyName.rstrip()+' destroyed by missile, press enter'
			ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
			EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
			VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
			DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
			DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
		else:
			Enemies[MissileTarget+6]=EnemyHull
			pygame.mixer.music.load('Beep.wav')
			pygame.mixer.music.play()
			Status=EnemyName.rstrip()+' hit by missile for '+SPlayerMissileDamage+' damage'
			ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
			EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
			DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
		return(Enemies, Exp)

	def FireLaser (Enemies, Stars, Asteroids, LaserTarget, PlayerLevel, Exp, Nexp):
		Nexp=int(Exp[0])
		PlayerLaserDamage=PlayerLevel*10
		SPlayerLaserDamage=str(PlayerLaserDamage)
		EnemyName=Enemies[LaserTarget+1]
		EnemyHull=int(Enemies[LaserTarget+6])
		EnemyHull=EnemyHull-PlayerLaserDamage
		pygame.mixer.music.load('Beep.wav')
		pygame.mixer.music.play()
		Enemies[LaserTarget+6]=EnemyHull
		if EnemyHull < 1:
			pygame.mixer.music.load('Boom.wav')
			pygame.mixer.music.play()
			EnemyXp=int(Enemies[LaserTarget])
			Nexp=Nexp+EnemyXp
			Exp[0]=Nexp
			Counter=0
			while Counter < 10:
				del Enemies[LaserTarget]
				Counter=Counter+1
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


	NewLevel(Level)
	Action=0
	MissilePosX=-50
	MissilePosY=-50
	ScanEnemy=[None]*4
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
	SPlayerHull=str(PlayerHull)
	SPlayerMissiles=str(PlayerMissiles)
	SExp=str(Exp[0])
	SExpNeeded=str(ExpNeeded)
	SLevel=str(Level)
	ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
	Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '+str(PlayerHull)+'/'+str(PlayerHullMax)+' Missiles: '\
+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
	EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
	VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
	DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

	running=True
	while running==True:
		SPlayerLevel=str(PlayerLevel)
		Action=0
		ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
		Move=PlayerLevel
		print('Player turn...')
		while Action < 3:
			SAction=str(Action+1)
			EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
			ScreenAction=False
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					Direction=5
					if event.key == pygame.K_KP1:
						Direction=1
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP2:
						Direction=2
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP3:
						Direction=3
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP4:
						Direction=4
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP5:
						Direction=5
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP6:
						Direction=6
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP7:
						Direction=7
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP8:
						Direction=8
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP9:
						Direction=9
						Action=Action+1
						SAction=str(Action+1)
						ScreenAction=True
					elif event.key == pygame.K_KP_PLUS:
						Move=Move+1
						if Move > PlayerLevel:
							Move=PlayerLevel
						SLevel=str(Level)
						SMove=str(Move)
						SLevel=str(Level)
						SPlayerLevel=str(PlayerLevel)
						PlayerDamage=PlayerLevel*10
						SPlayerHullMax=str(PlayerLevel*100)
						SPlayerHull=str(PlayerHull)
						SPlayerMissiles=str(PlayerMissiles)
						SExp=str(Exp[0])
						SExpNeeded=str(ExpNeeded)
						Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '+str(PlayerHull)+'/'\
+str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_KP_MINUS:
						Move=Move-1
						if Move < 1:
							Move=1
						SMove=str(Move)
						SLevel=str(Level)
						SPlayerLevel=str(PlayerLevel)
						PlayerDamage=PlayerLevel*10
						SPlayerHullMax=str(PlayerLevel*100)
						SPlayerHull=str(PlayerHull)
						SPlayerMissiles=str(PlayerMissiles)
						SExp=str(Exp[0])
						SExpNeeded=str(ExpNeeded)
						SLevel=str(Level)
						Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '+str(PlayerHull)+'/'\
+str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
						EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_KP0:
						if not PlayerMissiles < 1:
							MissileTarget=20000000
							PlayerScan=PlayerLevel*2
							MissileScan(Enemies, MissileTargetList, PlayerScan)
							if len(MissileTargetList) > 0:
								MissileTarget=SelectMissileEnemy(MissileTargetList, Enemies)
							if MissileTarget < len(Enemies):
								PlayerMissiles=PlayerMissiles-1
								MissileTargetX=int(Enemies[MissileTarget+8])
								MissileTargetY=int(Enemies[MissileTarget+9])
								MissilePosX=PlayerX
								MissilePosY=PlayerY
								ScreenItem=pygame.image.load('Bomb.png')
								for item in range(1, 20):
									Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '\
+str(PlayerHull)+'/'+str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+' Exp: '+SExp+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
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
									VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
									DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

								MissilePosX=-50
								MissilePosY=-50
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
								logo = pygame.image.load('JGrid.png')
								pygame.display.set_icon(logo)
								pygame.display.set_caption('Jumpwar')
								Width=int(1000)
								Heigth=int(1000)
								screen = pygame.display.set_mode((Width, Heigth))
								screen.blit(logo, (0,0))
								if PlayerHull > PlayerLevel*50:
									PlayerImage=pygame.image.load('Happy.png')
								else:
									PlayerImage=pygame.image.load('Sad.png')
								
								screen.blit(PlayerImage, (475,475))
								pygame.display.flip()
								ScreenX=(MissileScreenX+10)*47.5
								YConvert=MissileScreenY*-1
								ScreenY=(YConvert+10)*47.5
								ScreenItem=pygame.image.load('Blast.png')
								screen.blit(ScreenItem, (ScreenX,ScreenY))
								pygame.display.flip()

								FireMissile(Enemies, Stars, Asteroids, MissileTarget, PlayerLevel, Exp, Nexp)
								Action=Action+1
								SAction=str(Action+1)
								Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '\
+str(PlayerHull)+'/'+str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							else:
								Status='No Missile Targets, Press Enter'
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
								wait()		
								Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '\
+str(PlayerHull)+'/'+str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
						else:
							Status='No Missiles, Press Enter'
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							wait()		
							Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '\
+str(PlayerHull)+'/'+str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_KP_DIVIDE:
						LaserTarget=20000000
						LaserScan(Enemies, LaserTargetList)
						if len(LaserTargetList) > 0:
							LaserTarget=SelectLaserEnemy(LaserTargetList, Enemies)
						if LaserTarget < len(Enemies):
							LaserTargetX=int(Enemies[LaserTarget+8])
							LaserTargetY=int(Enemies[LaserTarget+9])
							LaserScreenX=LaserTargetX-PlayerX
							LaserScreenY=LaserTargetY-PlayerY
							logo = pygame.image.load('JGrid.png')
							if PlayerHull > PlayerLevel*50:
								PlayerImage=pygame.image.load('Happy.png')
							else:
								PlayerImage=pygame.image.load('Sad.png')
							pygame.display.set_icon(logo)
							pygame.display.set_caption('Jumpwar')
							Width=int(1000)
							Heigth=int(1000)
							screen = pygame.display.set_mode((Width, Heigth))
							screen.blit(logo, (0,0))
							screen.blit(PlayerImage, (475,475))
							pygame.display.flip()
							ScreenX=(LaserScreenX+10)*47.5
							YConvert=LaserScreenY*-1
							ScreenY=(YConvert+10)*47.5
							ScreenItem=pygame.image.load('Blast.png')
							screen.blit(ScreenItem, (ScreenX,ScreenY))
							pygame.display.flip()
							FireLaser(Enemies, Stars, Asteroids, LaserTarget, PlayerLevel, Exp, Nexp)
							Action=Action+1
							SAction=str(Action+1)
							ScreenAction=True
						else:
							Status='No Laser Targets'
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							wait()		
							Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '\
+str(PlayerHull)+'/'+str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_KP_MULTIPLY:
						DoLegend()
						Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '+str(PlayerHull)+'/'\
+str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
					elif event.key == pygame.K_h:
						DoHelp()
						Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '+str(PlayerHull)+'/'\
+str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
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
							PlayerHull=PlayerHull-Damage
							if PlayerHull < 1:
								pygame.mixer.music.load('Boom.wav')
								pygame.mixer.music.play()
								Status='You Crashed into a Star, press enter'
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
								wait()
								sys.exit()

						Counter=0
						CrashAsteroid=0
						MaxCounter=len(Asteroids)
						while Counter < MaxCounter:
							AsteroidType=Asteroids[Counter]
							AsteroidX=Asteroids[Counter+1]
							AsteroidY=Asteroids[Counter+2]
							if (PlayerX == AsteroidX) and (PlayerY == AsteroidY):
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
							if PlayerHull > (PlayerLevel*100):
								PlayerHull = (PlayerLevel*100)
							if PlayerMissiles > PlayerLevel:
								PlayerMissiles = PlayerLevel
	
						if ScreenAction==True:
							Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '\
+str(PlayerHull)+'/'+str(PlayerHullMax)+' Missiles: '+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
							Nexp=int(Exp[0])
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

						MoveCounter=MoveCounter+1

		if len(Enemies) > 0:
			EnemyDir=0
			Status='Enemy Turn'
			print('Enemy turn...')
			EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
			VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
			DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
			Counter=0
			EnemyName='Enemy'
			MaxCounter=len(Enemies)
			while Counter < MaxCounter:
				EnemyActive=False
				EnemyName=Enemies[Counter+1]
				EnemyAction=0
				while EnemyAction < 2:
					EnemyLevel=int(Enemies[Counter])
					EnemyName=str(Enemies[Counter+1]).rstrip()
					EnemyHull=int(Enemies[Counter+6])
					EnemyScan=int(Enemies[Counter+5])
					EnemyX=int(Enemies[Counter+8])
					EnemyY=int(Enemies[Counter+9])
					XDiff=PlayerX-EnemyX
					YDiff=PlayerY-EnemyY
					if (-4 <= XDiff) and ( XDiff <= 4) and (-4 <= YDiff) and (YDiff <= 4):
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyActive=True
						EnemyLaserDamage=int(Enemies[Counter+3])
						PlayerHull=PlayerHull-EnemyLaserDamage
						pygame.mixer.music.load('Beep.wav')
						pygame.mixer.music.play()
						print(EnemyName, ' fires laser...')
						SEnemyLaserDamage=str(EnemyLaserDamage)
						EnemyAction=EnemyAction+1
						MissileScreenX=MissilePosX-PlayerX
						MissileScreenY=MissilePosY-PlayerY
						logo = pygame.image.load('JGrid.png')
						PlayerImage=pygame.image.load('Blast.png')
						pygame.display.set_icon(logo)
						pygame.display.set_caption('Jumpwar')
						Width=int(1000)
						Heigth=int(1000)
						screen = pygame.display.set_mode((Width, Heigth))
						screen.blit(logo, (0,0))
						screen.blit(PlayerImage, (475,475))
						pygame.display.flip()
						if PlayerHull <= 0:
							pygame.mixer.music.load('Boom.wav')
							pygame.mixer.music.play()
							Status='Player destroyed by '+EnemyName+' laser'
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
							wait()
							sys.exit()
					if ((-20) <= XDiff) and ( XDiff <= 20) and ((-20) <= YDiff) and (YDiff <= 20):
						EnemyMissiles=int(Enemies[Counter+7])
						if EnemyMissiles > 0:
							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyActive=True
							if EnemyMissiles > random.randint(0, 19):
								print(EnemyName, ' fires missile...')
								MissileTargetX=PlayerX
								MissileTargetY=PlayerY
								MissilePosX=int(Enemies[Counter+8])
								MissilePosY=int(Enemies[Counter+9])
								ScreenItem=pygame.image.load('Bomb.png')
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
									EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
									VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
									DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
									if (MissilePosX == MissileTargetX) and (MissilePosY == MissileTargetY):
										break
								
								MissilePosX=-50
								MissilePosY=-50
								ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
								EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
								logo = pygame.image.load('JGrid.png')
								PlayerImage=pygame.image.load('Blast.png')
						
								pygame.display.set_icon(logo)
								pygame.display.set_caption('Jumpwar')
								Width=int(1000)
								Heigth=int(1000)
								screen = pygame.display.set_mode((Width, Heigth))
								screen.blit(logo, (0,0))
								if PlayerHull > PlayerLevel*50:
									PlayerImage=pygame.image.load('Happy.png')
								else:
									PlayerImage=pygame.image.load('Sad.png')
								screen.blit(PlayerImage, (475,475))
								pygame.display.flip()
								ScreenX=(MissileScreenX+10)*47.5
								YConvert=MissileScreenY*-1
								ScreenY=(YConvert+10)*47.5
								ScreenItem=pygame.image.load('Blast.png')
								screen.blit(ScreenItem, (ScreenX,ScreenY))
								pygame.display.flip()
													
								VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
								DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

								EnemyAction=EnemyAction+1
								EnemyMissiles=EnemyMissiles-1
								Enemies[Counter+7]=EnemyMissiles
								EnemyName=Enemies[Counter+1]
								EnemyMissileDamage=int(Enemies[Counter+3])*1.5
								PlayerHull=PlayerHull-EnemyMissileDamage
								pygame.mixer.music.load('Beep.wav')
								pygame.mixer.music.play()
								SEnemyMissileDamage=str(EnemyMissileDamage)
								if PlayerHull <= 0:
									pygame.mixer.music.load('Boom.wav')
									pygame.mixer.music.play()
									Status='Player destroyed by '+EnemyName+' missile'
									EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
									VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
									ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
									DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
									EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
									wait()
									sys.exit()

					if EnemyHull < (EnemyLevel*30):
						AsteroidScan=[None]*4
						AsteroidScan=ScanAsteroid(EnemyX, EnemyY)
						if not AsteroidScan[0]==None:
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
								print(EnemyName, ' eats asteroid...')
								if EnemyHull > (EnemyLevel*100):
									EnemyHull = (EnemyLevel*100)
								EnemyMissiles=EnemyMissiles+ExtraMissiles
								Enemies[Counter+6]=EnemyHull
								Enemies[Counter+7]=EnemyMissiles
								Enemies[Counter+8]=EnemyX
								Enemies[Counter+9]=EnemyY
								WipeCounter=0
								while WipeCounter < 3:
									del Asteroids[AsteroidCounter]
									WipeCounter=WipeCounter+1
								AsteroidMaxCounter=len(Asteroids)
							EnemyAction=EnemyAction+1

					if ((-1*EnemyScan) <= XDiff) and ( XDiff <= (EnemyScan)) and ((-1*EnemyScan) <= YDiff) and (YDiff <= (EnemyScan)):
						EnemyActive=True
						if (EnemyX < PlayerX) and (EnemyY < PlayerY):
							if EnemyHull > (EnemyLevel*30):
								EnemyDir=9
							else:
								EnemyDir=1
						if (EnemyX < PlayerX) and (EnemyY == PlayerY):
							if EnemyHull > (EnemyLevel*30):
								EnemyDir=6
							else:
								EnemyDir=4
						if (EnemyX < PlayerX) and (EnemyY > PlayerY):
							if EnemyHull > (EnemyLevel*30):
								EnemyDir=3
							else:
								EnemyDir=7
						if (EnemyX == PlayerX) and (EnemyY > PlayerY):
							if EnemyHull > (EnemyLevel*30):
								EnemyDir=2
							else:
								EnemyDir=8
						if (EnemyX > PlayerX) and (EnemyY > PlayerY):
							if EnemyHull > (EnemyLevel*30):
								EnemyDir=1
							else:
								EnemyDir=9
						if (EnemyX > PlayerX) and (EnemyY == PlayerY):
							if EnemyHull > (EnemyLevel*30):
								EnemyDir=4
							else:
								EnemyDir=6
						if (EnemyX > PlayerX) and (EnemyY < PlayerY):
							if EnemyHull > (EnemyLevel*30):
								EnemyDir=7
							else:
								EnemyDir=3
						if (EnemyX == PlayerX) and (EnemyY < PlayerY):
							if EnemyHull > (EnemyLevel*30):
								EnemyDir=8
							else:
								EnemyDir=2

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

						EnemyMoveCounter=int(Enemies[Counter+4])
						if (-10 <= XDiff) and ( XDiff <= 10) and (-10 <= YDiff) and (YDiff <= 10):
							if EnemyHull > (EnemyLevel*30):
								EnemyMoveCounter=4
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

							Enemies[Counter+8]=EnemyX
							Enemies[Counter+9]=EnemyY
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
										print(EnemyName, ' eats asteroid...')
										if EnemyHull > EnemyLevel*100:
											EnemyHull = EnemyLevel*100
										EnemyMissiles=EnemyMissiles+ExtraMissiles
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
								if CrashStar==1:
									Damage=100
								elif CrashStar==2:
									Damage=200
								elif CrashStar==3:
									Damage=300
								EnemyHull=EnemyHull-Damage
								if EnemyHull < 1:
									print(EnemyName, ' crashes into star...')
									pygame.mixer.music.load('Boom.wav')
									pygame.mixer.music.play()
									WipeCounter=0
									while WipeCounter < 10:
										del Enemies[Counter]
										WipeCounter=WipeCounter+1
										MaxCounter=len(Enemies)
									break
								else:
									Enemies[Counter+6]=EnemyHull

							ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
							EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
							VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
							DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

							EnemyMove=EnemyMove+1

						
					

						Status='Enemy Turn'

					if EnemyActive==True:
						ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
						EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
						VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
						DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)

					EnemyAction=EnemyAction+1

				Counter=Counter+10

		Nexp=int(Exp[0])
		if Nexp >= ExpNeeded:
			Nexp=Nexp-ExpNeeded
			PlayerLevel=PlayerLevel+1
			ExpNeeded=PlayerLevel*4
			if PlayerLevel > 20:
				PlayerLevel=20
			if Nexp < 0:
				NExp=0
			Exp[0]=Nexp
			Move=PlayerLevel
			PlayerHullMax=PlayerLevel*100
			pygame.mixer.music.load('Applause.wav')
			pygame.mixer.music.play()
			Status='Ship leveled up, press enter'
			ClosestEnemy=ScanEnemies(Enemies, PlayerX, PlayerY, Radar, ScanEnemy)
			EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
			VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
			DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
			wait()
		



		if PlayerX==WormholeX and PlayerY==WormholeY:
			Level=Level+1
			SLevel=str(Level)
			SPlayerLevel=str(PlayerLevel)
			Nexp=int(Exp[0])
			SNexp=str(Nexp)
			Action=3
			running=False
			LoadList[SaveCounter]=SLevel
			LoadList[SaveCounter+1]=SPlayerLevel
			LoadList[SaveCounter+2]=SNexp
			os.system('rm Jumpwar.txt')
			Save=open('Jumpwar.txt', 'a')
			WriteCounter=0
			while WriteCounter < len(LoadList):
				Line=str(LoadList[WriteCounter]).strip()
				SLine=Line+'\n'
				Save.write(SLine)
				WriteCounter=WriteCounter+1
			Save.close()
			
		Move=PlayerLevel
		Action=0
		Status='Level: '+str(Level)+' Player Level: '+str(PlayerLevel)+' Jump Distance: '+str(Move)+'/'+str(PlayerLevel)+' Hull: '+str(PlayerHull)+'/'+str(PlayerHullMax)+' Missiles: '\
+str(PlayerMissiles)+' Exp: '+str(Exp[0])+'/'+str(ExpNeeded)+' Turn: '+str(Action+1)
		EnemyStatus=str(ClosestEnemy[0]).rstrip()+' at: '+str(ClosestEnemy[2])+' '+str(ClosestEnemy[3])+' Hull: '+str(ClosestEnemy[1]).rstrip()
		VisualScan(Stars, Asteroids, Enemies, MissilePosX, MissilePosY)
		DoScreen(ScreenRange, Move, Level, PlayerLevel, Exp, ExpNeeded, Status, EnemyStatus)
			

DoVictory()
sys.exit()



