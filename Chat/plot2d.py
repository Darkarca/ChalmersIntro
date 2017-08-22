import sys, pygame, math

functions = []
functions_x = []
functions_xi = []
exec_functions = []
colors = []

functioncount = raw_input("How many functions would you like to plot? ")

for n in range(int(functioncount)):
    functions.append(str(raw_input("Enter function: ")))
    colors.append(raw_input("R, G, B: "))

for func in range(len(functions)):
    functions_x.append(functions[func].replace("x", "x/24"))
    functions_xi.append(functions[func].replace("x", "xi/24"))
    exec_functions.append("pygame.draw.line(screen, ["+colors[func]+"], [i,240-("+functions_x[func]+")*24] , [i-1,240-("+functions_xi[func]+")*24], 3)")

pygame.init()

size = width, height = 480, 480

screen = pygame.display.set_mode(size)
back = pygame.image.load("back3.gif")
backrect = back.get_rect()
screen.blit(back,backrect)

while 1:
    xi = float(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    for i in range(480):
        x = float(i-240)
        for function in exec_functions:
            exec(function)
        xi = x
        pygame.draw.rect(screen, [9, 205, 218], [0, 0, 480, 480], 3)

    pygame.display.flip()