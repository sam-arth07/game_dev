import pygame
import math 
from random import randint
from pygame import mixer

# initialise game
pygame.init()

# create game window 
screen = pygame.display.set_mode((800,600))

# Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Background
bg = pygame.image.load("bg.png")

# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1) 

# PLayer
player_img= pygame.image.load('player.png')
playerX=370
playerY=470
playerX_change = 0

# Enemy
no_of_enemies = 7
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for enemy in range(no_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemyX.append(randint(0, 736))
    enemyY.append(randint(50, 200))
    enemyX_change.append(10)
    enemyY_change.append(randint(20,50))

# missile
missile_img= pygame.image.load('missile.png')
missileX=0
missileY=470
missileY_change = 30
# ready - missile isnt visible 
# fire - missile is currently moving
missile_state='ready'

def player(x,y):
    screen.blit(player_img,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))

def fire_missile(x,y):
    global missile_state
    missile_state = 'fire'
    screen.blit(missile_img,(x+16,y+10))

def iscollision(x1,y1,x2,y2):
    distance = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
    if distance < 30:
        return True
    return False

# points / no of kills
score_val = 0 
font =  pygame.font.Font('freesansbold.ttf',40)
textX = 10
textY = 10

#fps
FPS = 45
clock = pygame.time.Clock()

#Game over text
over_font = pygame.font.Font('freesansbold.ttf',70)

def show_score(x,y):
    score = font.render('Score : ' + str(score_val), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render('GAME OVER',True,(255,255,255))
    screen.blit(over_text,(200,250))


# Game Loop
run = True
while run:
    clock.tick(FPS) 
    # Bottom most layer - everything lies above this
    screen.fill((0,100,150))
    # Bg img
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                playerX_change = -9
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                playerX_change = 9
            if event.key == pygame.K_SPACE:
                if missile_state=='ready':
                    # missile_sound=mixer.Sound('laser.wav')
                    # missile_sound.play()
                    missileX = playerX
                    fire_missile(missileX,missileY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == ord('a') or event.key == ord('d'):
                playerX_change = 0


    playerX += playerX_change
    # Creating Boundaries for player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement

    for i in range(no_of_enemies):
        #Game Over
        if enemyY[i] > 440:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 10
            enemyY[i] += enemyY_change[i] 
        elif enemyX[i] >= 736:
            enemyX_change[i] = -10
            enemyY[i] += enemyY_change[i] 
    
        # Collision
        collision = iscollision(enemyX[i],enemyY[i],missileX,missileY)
        if collision:
            # explosion_Sound=mixer.Sound('explosion.wav')
            # explosion_Sound.play()
            missileY = 470
            missile_state = 'ready'
            score_val += 1
            enemyX[i]=randint(0, 736)
            enemyY[i]=randint(50, 200)    
        enemy(enemyX[i],enemyY[i],i)
    # Missile Movement
    if missileY <= 0:
        missileY = 470
        missile_state = 'ready'
    if missile_state is 'fire':
        fire_missile(missileX,missileY)
        missileY-=missileY_change
    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()