import pygame
import random
import math

#initialise game
pygame.init()

#create game window
screen = pygame.display.set_mode((800,600))

#Title and icon
pygame.display.set_caption("BRICK BREAKER")
ICON = pygame.image.load('assets/icon/brick-breaker.png')
pygame.display.set_icon(ICON)

FPS = 60
clock = pygame.time.Clock()

def display_fn():
    pygame.display.update()

def main():
    run = True
    screen.fill((255,255,255))
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    display_fn()    

main()          