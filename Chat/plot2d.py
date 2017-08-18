import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    for i in range(640):
        y = i-320
        pygame.draw.line(screen, [9,205,218], [i,480-(pow(y/24,2)*24)] , [i,480-(pow(y/24,2)*24)], 1)

    pygame.display.flip()