import pygame
import random
import math
from pygame import mixer
#creating game using python

pygame.init()

screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load("background.jpg")

#background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

#SCORE: 

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#game over font
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))

def show_score(x,y):
    score = font.render("Score :" + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

#player

playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
def player(x,y):
    screen.blit(playerImg,(x,y))

#creating enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6
for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load('game.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)
def enemy(x,y):
           screen.blit(enemyImg[i],(x,y))


#fucntion for bullet collision 
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance =  math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance <27:
        return True
    else:
        return False




#game loop

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = -0.5
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))


#title and icon
pygame.display.set_caption("space invader")
icon = pygame.image.load('rocket-icon.png')
pygame.display.set_icon(icon)


running = True
while running:
    #RGB = red green blue
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left is pressed")
                playerX_change = -0.3

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("right is pressed")
                playerX_change = 0.3

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    #get the current x cordinate of the spaceship

                    bulletX = playerX
                    bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("key storke has been released")
                playerX_change = 0     

    player(playerX,playerY)
    for i in range(number_of_enemies):
        enemy(enemyX[i],enemyY[i])

    #checking boundaries of player
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
#movement of enemy
    for i in range(number_of_enemies):
        #game over
        if enemyY[i] > 400:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i] 

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_change
    #collision 

    for i in range(number_of_enemies):
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()    
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        


    # Reset bullet when it goes off screen
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"


   
    show_score(textX,textY)
    
    pygame.display.update()
            



