from tkinter import Y
import pygame
from pygame.locals import *
import sys
import math
import random
w, h, s, rw, rh, r = 700, 500, 20, 10, 50, 10
x1, y1, x2, y2 ,yv = s, h / 2, w - s, h / 2, 10
bx, by = w / 2, h / 2
vx, vy, xmin, ymin, xmax, ymax = -10, 5, 10, -5, 26 , 8
s1, s2, smax = 0, 0, 10
level = 0.4
pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.mouse.set_visible(False)  
while 1:
    screen.fill((0, 0, 0)) # fill screen with black R:0 G:0 B:0
    # center line
    for i in range(s, h, h // 20):
         if i % 2 == 1:
            continue
         pygame.draw.line(screen, (255, 255, 255),(w // 2 - 5, i), (w // 2 - 5, i + h // 20), 10)
    # racket
    pygame.draw.line(screen, (255, 255, 255), (x1, y1 - rh // 2), (x1, y1 + rh // 2), rw)
    pygame.draw.line(screen, (255, 255, 255), (x2, y2 - rh // 2), (x2, y2 + rh // 2), rw)
    # score
    f = pygame.font.SysFont(None, 64)                     
    t = f.render(f"{s1}  {s2}", True, (255, 255, 255))
    screen.blit(t,(w // 2 - t.get_width() // 2, 20))
    # game over
    if s1 == smax or s2 == smax:
        f=pygame.font.SysFont(None,120)                     
        t=f.render("WIN", True, (255, 0, 0))
        screen.blit(t, (int(w * (0.25 if s1 == smax else 0.75) - t.get_width() / 2), h // 3))
        pygame.display.update() 
        pygame.time.wait(6000)
        pygame.quit()
        sys.exit()
    # ball
    pygame.draw.circle(screen, (255, 0, 0), (bx, by), r)
    # racket movement
    x, y2 = pygame.mouse.get_pos()
    y1 += (max(by - y1, -yv) if by - y1 < 0 else min(by - y1, yv)) if vx < 0 and (bx - x1) / (x2 - x1) <= level else 0
    # racket inside window
    y1 = rh / 2 if y1 < rh / 2 else h - rh / 2 if y1 > h - rh / 2 else y1
    y2 = rh / 2 if y2 < rh / 2 else h - rh / 2 if y2 > h - rh / 2 else y2 
    # ball movement
    bx += vx
    by += vy
    # ball inside window
    if (0 > by and vy < 0) or (by > h and vy > 0):
        vy = -vy
    # racket hit
    if (y1 - rh < by < y1 + rh and vx < 0 and bx < s + rw + r) or (y2 - rh < by < y2 + rh and vx > 0 and bx > w - s - rw - r):
        vx = -vx*1.1
        vx = -xmax if vx < -xmax else xmax if vx > xmax else vx
        vy = random.randrange(ymin, ymax)
    # ball went outside
    if bx < -xmax -r or bx > w + xmax + r:
        pygame.time.wait(1000)
        if bx < -xmax :
            s2 += 1
        else:
            s1 += 1
        vx, vy = random.randrange(xmin, xmax // 2) * (1 if bx > w else -1), random.randrange(ymin, ymax)
        bx, by = s + rw + r if bx > w else w - s - rw - r, y1 if bx > w else y2
    for event in pygame.event.get():
            # close button pushed
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # escape key pressed
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    pygame.display.update() # update display
    pygame.time.wait(30) # interval of updating

