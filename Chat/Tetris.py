import sys, pygame, math


speed = 500
pygame.init()

size = width, height = 360, 720
dontburncpu = pygame.time.Clock()
screen = pygame.display.set_mode(size)

while 1:
    xi = float(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        print ("test")
        dontburncpu.tick(30)



pygame.display.flip()