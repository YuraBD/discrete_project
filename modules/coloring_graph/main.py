import pygame
from ColoringGraph import Graph

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Coloring graph")

with open("graph.txt", "r") as info:
    lines = info.readlines()

graph = []
for i in lines:
    line = []
    for j in (i.split(" ")):
        line.append(int(j))
    graph.append(line)


colorrange = []
l = len(graph)
for i in range(1, 1+l):
    if i % 2 == 0:
        colorrange.append((i*(255/l), i, i*(255/l)))
    elif i % 3 == 0:
        colorrange.append((i*(255/l), i*(255/l), i))
    else:
        colorrange.append((i, i*(255/l), i*(255/l)))

run = True
while run:

    pygame.time.delay(100)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False

    win.fill((204, 119, 34))
    x,y = 50,50
    coords = []
    for i in range(l):
        if i % 3 == 0 and i != 0:
            y += 150
            x = 50
        coords.append((x, y))
        pygame.draw.circle(win, (0, 0, 0), (x, y), 20)
        x = x + 150

    for i in range(l):
        for j in range(l):
            if graph[i][j] == 1:
                pygame.draw.line(win, (0, 0, 0), coords[i], coords[j])
            
            pygame.draw.circle(win, (204, 119, 34), coords[j], 15)
    
    g = Graph(l)
    g.graph = graph
    m = l
    color = g.graphColouring(m)

    for i in range(len(color)):
        color[i] = colorrange[color[i] - 1]
    for i in range(l):
        pygame.draw.circle(win, color[i], coords[i], 15)
    col = []
    for i in color:
        if i not in col:
            col.append(i)
    message = f'Number of colors = {len(col)}'

    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render(message, True, (0, 0, 0))
    textRect = text.get_rect()
    
    textRect.center = (200, coords[-1][1] + 100)

    win.blit(text, textRect)

    pygame.display.update()
