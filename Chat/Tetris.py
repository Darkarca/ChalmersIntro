import sys, pygame, math, random


speed = 30
pygame.init()

size = width, height = 360, 720
dontburncpu = pygame.time.Clock()
screen = pygame.display.set_mode(size)
blockisselected = False
blockposx = []
blockposy = []
slectedposx = []
selectedposy = []
slectedposx.append(0)
pygame.mixer.music.load("tetris-gameboy-02.mp3")
pygame.mixer.music.play(loops=-1, start=0.0)

while 1:
    if(blockisselected == False):
            rand = random.randint(1,1) #1,7
            if(rand == 1):
                slectedposx[1] = 4
                slectedposx[2] = 5
                slectedposx[3] = 6
                slectedposx[4] = 7
                slectedposy[1] = 1
                slectedposy[2] = 1
                slectedposy[3] = 1
                slectedposy[4] = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        print (slectedposx[0])
        dontburncpu.tick(30)




pygame.display.flip()