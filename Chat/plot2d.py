import sys, pygame

function = str(raw_input("Enter function: "))
function = function.replace("x", "x/24")
function3 = function.replace("x", "xi")
print function
func2 = "pygame.draw.line(screen, [9,205,218], [i,240-("+function+")*24] , [i-1,240-("+function3+")*24], 1)"
pygame.init()

size = width, height = 480, 480

screen = pygame.display.set_mode(size)
back = pygame.image.load("back2.gif")
backrect = back.get_rect()
screen.blit(back,backrect)
while 1:
    xi = float(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    for i in range(480):
        x = float(i-240)
        #xstart = 240-(pow(x/24,2)*24)
        #xend = 240-(pow(xi/24,2)*24)
        #pygame.draw.line(screen, [9,205,218], [i,xstart] , [i-1,xend], 1)

        exec(func2)
        xi = x

    pygame.display.flip()