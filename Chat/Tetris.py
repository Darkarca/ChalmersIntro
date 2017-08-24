import sys, pygame, math, random


speed = 30
pygame.init()

size = width, height = 360, 720
dontburncpu = pygame.time.Clock()
screen = pygame.display.set_mode(size)
blockisselected = False
blockpos = []
slectedpos = [0, 0]
slectedpos.append([0, 0])
pygame.mixer.music.load("tetris-gameboy-02.mp3")
pygame.mixer.music.play(loops=-1, start=0.0)

while 1:
    if(blockisselected == False):
            rand = random.randint(1,1) #1,7
            if(rand == 1):
                print()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        print (slectedpos[1])
        dontburncpu.tick(30)




pygame.display.flip()