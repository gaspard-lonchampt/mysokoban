import pygame
import sys
from game import Game
import random
import os
os.environ["SDL_VIDEODRIVER"] = "x11"

import sys, pygame

pygame.init()

width = 480
height = 400
size = [width, height]
pygame.display.set_caption("A rabbit Sokoban")
screen = pygame.display.set_mode(size)


game = Game()
myMap = game.map.generateMap()


while 1:

    #injection de l'image du personnage
    # screen.blit(game.player.image, game.player.rect)

    # game.map.getLocation(screen)
    game.map.loopMap(screen)

    #mettre a jour mon ecran
    pygame.display.flip()

    # for event in pygame.event.get():

    #     if event.type == pygame.QUIT:
    #         sys.exit()
