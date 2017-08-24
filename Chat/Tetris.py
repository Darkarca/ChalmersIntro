import sys, pygame, math


speed = 1
pygame.init()

size = width, height = 360, 720

screen = pygame.display.set_mode(size)

while 1:
    xi = float(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        sleep(speed)



pygame.display.flip()