import pygame
#creating game using python

pygame.init()

screen = pygame.display.set_mode((800,600))


#player

playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
def player(x,y):
    screen.blit(playerImg,(x,y))


#game loop

#title and icon
pygame.display.set_caption("space invader")
icon = pygame.image.load('rocket-icon.png')
pygame.display.set_icon(icon)



running = True
while running:
    #RGB = red green blue

    screen.fill((0,0,0))
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


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("key storke has been released")
                playerX_change = 0     

    player(playerX,playerY)
    playerX += playerX_change
    pygame.display.update()
            

#movement and mechanics in game

#49 min on 