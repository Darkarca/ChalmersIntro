import sys, pygame, math


speed = 2
pygame.init()

size = width, height = 360, 720

screen = pygame.display.set_mode(size)
pygame.mixer.music.load("tetris-gameboy-02.mp3")
pygame.mixer.music.play(loops=-1, start=0.0)
while 1:
    xi = float(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

       # sleep(speed)



pygame.display.flip()