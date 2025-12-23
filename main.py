import pygame
#creating game using python

pygame.init()

screen = pygame.display.set_mode((800,600))

#game loop

#title and icon
pygame.display.set_caption("space invader")
icon = pygame.image.load('rocket-icon.png')
pygame.display.set_icon(icon)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#RGB = red green blue
    screen.fill((255,0,0))
    pygame.display.update()
            


