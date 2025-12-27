import pygame
import random
#creating game using python

pygame.init()

screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load("background.jpg")


#player

playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
def player(x,y):
    screen.blit(playerImg,(x,y))

#creating enemy
enemyImg = pygame.image.load('game.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40
def enemy(x,y):
    screen.blit(enemyImg,(x,y))

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
                playerX_change = -0.1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("right is pressed")
                playerX_change = 0.1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("key storke has been released")
                playerX_change = 0     

    player(playerX,playerY)
    enemy(enemyX,enemyY)

    #checking boundaries of player
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
#movement of enemy

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change 

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_change
    
    # Reset bullet when it goes off screen
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    pygame.display.update()
            



