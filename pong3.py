import pygame,sys,random
from pygame.locals import *

(width, height, mergin) = ( 700, 500, 30 )
(WHITE,BLACK,RED) = ((255,255,255), (0,0,0), (255,0,0))
(rw, rh, rv) = (10, 50, 10)
(cx, cy, ps) = (mergin, 250, 0)
(px, py, cs) = (width - mergin - rw, 250, 0)
(bx, by, br, bvx, bvy, bvxmin, bvymin, bvxmax, bvymax)  = ( width//2, height//2, 5, 8, 5, 8, 5, 16, 10)
pygame.init()
screen=pygame.display.set_mode((width, height))
font=pygame.font.SysFont(None,64)
while True:
    screen.fill(WHITE)
    # Show Score
    text=font.render(f"{cs} - {ps}", True, BLACK)
    screen.blit(text,(width//2-40, 100))
    # Draw ball
    pygame.draw.circle(screen, RED, (bx, by), br)
    # Draw paddles
    pygame.draw.rect(screen, BLACK, (px, py, rw, rh))
    pygame.draw.rect(screen, BLACK, (cx, cy, rw, rh))
    # Bounce off top and bottom
    if by > height - br * 2:
        by = height - br * 2
        bvy *= -1
    elif by < br:
        by = br
        bvy *= -1
    #  If intersecting with Paddle #1
    if  bx - br < cx + rw and bx + br > cx and by > cy and by < cy+ rh:
        bx = cx + rw + br
        bvx *= -1.1 # Invert and increase velocity by 10%
        bvy = random.random() * bvymax * 2 - bvymax # Random y velocity between -bvymax and bvymax
    #  If intersecting with Paddle #2
    elif  bx - br < px + rw and bx + br > px and by > py and by < py + rh: 
        bx = px - br
        bvx *= -1.1 # Invert and increase velocity by 10%
        bvy = random.random() * bvymax * 2 - bvymax # Random y velocity between -bvymax and bvymax
    if bvx > bvxmax:
        bvx = bvxmax
    elif bvx < -bvxmax:
        bvx = -bvxmax
    # Move Paddles
    pressed_key=pygame.key.get_pressed()
    if pressed_key[K_w] and cy > 0:
        cy -= rv
    if pressed_key[K_s] and cy < height - rh:
        cy += rv
    if pressed_key[K_UP] and py > 0:
        py -= rv
    if pressed_key[K_DOWN] and py < height - rh:
        py += rv
    # Update Score
    if bx  < 0:
        cs +=1
        (bx, by, bvx, bvy) = (width//2, height//2, bvxmin, bvymin)
        pygame.time.wait(1000)
    elif bx > width:
        ps +=1
        (bx, by, bvx, bvy) = (width//2, height//2, -bvxmin, bvymin)
        pygame.time.wait(1000)
    # Move the ball
    bx += bvx
    by += bvy
    pygame.display.update()
    pygame.time.wait(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


