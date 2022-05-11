import sys
import pygame


class Map:

    def __init__(self):
        self.rabbit = pygame.image.load("assets/rabbit.jpg")
        self.rabbit_girl = pygame.image.load("assets/rabbit-girl.png")
        self.wood_box = pygame.image.load("assets/wood-box.png")
        self.grass = pygame.image.load("assets/grass.png")
        self.carrot = pygame.image.load("assets/carrot.png")
        # self.location = self.getLocation()
        self.map = self.generateMap()

    def generateMap(self):
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 3, 0, 2, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
    
    def getLocation(self, screen, value, a, i):
        return screen.blit(value, (value.get_width() * a, value.get_height() * i))

    def loopMap(self, screen):
        rabbit = pygame.transform.scale(self.rabbit, (40, 40))
        rabbit_girl = pygame.transform.scale(self.rabbit_girl, (40, 40))
        wood_box = pygame.transform.scale(self.wood_box, (40, 40))
        grass = pygame.transform.scale(self.grass, (40, 40))
        carrot = pygame.transform.scale(self.carrot, (40, 40))


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self.map[5][5] = 2
                self.map[4][5] = 0


            i = 0
            while i < len(self.map):

                # print(i,"ordonné")    
                a = 0
                while a < len(self.map[i]):
                    # print(a, "abscisse")
                    if self.map[i][a] == 0:
                        self.getLocation(screen, grass, a, i)
                    elif self.map[i][a] == 1:
                        self.getLocation(screen, wood_box, a , i)
                    elif self.map[i][a] == 2:
                        self.getLocation(screen, rabbit, a, i)
                    elif self.map[i][a] == 3:
                        self.getLocation(screen, carrot, a, i)
                    elif self.map[i][a] == 4:
                        self.getLocation(screen, rabbit_girl, a, i)
                    a += 1
                i += 1
            i = 0
