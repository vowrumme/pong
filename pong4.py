import pygame,sys,random
from pygame.locals import *

(width, height, mergin) = ( 700, 500, 10 )
(WHITE,BLACK,RED,GREEN,BLUE) = ((255,255,255), (0,0,0), (255,0,0), (0,255,0), (0,0,255))
(rw, rh, rv) = (10, 50, 10)
(cx, cy, ps) = (mergin, height//2 - rh//2, 0)
(px, py, cs) = (width - mergin - rw, height//2 - rh//2, 0)
(bx, by, br, bvx, bvy, bvxmin, bvymin, bvxmax, bvymax)  = ( width//2, height//2, 5, 8, 5, 8, 5, 20, 15)
pygame.init()
screen=pygame.display.set_mode((width, height))
font=pygame.font.SysFont(None,64)
run=True
while run:
    screen.fill(WHITE)
    # Show Score
    text=font.render(f"{cs} - {ps}", True, BLACK)
    screen.blit(text,(width//2-40, 50))
    # Show Game Over
    if ps == 10 or cs == 10:
        font=pygame.font.SysFont(None,128)
        text=font.render("Game Over", True, BLUE)
        screen.blit(text,(width//2-text.get_width()//2, height * 1//3))

        font=pygame.font.SysFont(None,64)
        text=font.render("You Win !!" if ps==10 else "You Lost !!", True, RED)
        screen.blit(text,(width//2-text.get_width()//2, height * 2//3))
        run = False
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
    #  If intersecting with Computer
    if bx - br < cx + rw and by > cy and by < cy+ rh:
        bx = cx + rw + br
        bvx *= -1.1 # Invert and increase velocity by 10%
        bvy = random.random() * bvymax * 2 - bvymax # Random y velocity between -bvymax and bvymax
    #  If intersecting with Player
    elif bx + br > px and by > py and by < py + rh: 
        bx = px - br
        bvx *= -1.1 # Invert and increase velocity by 10%
        bvy = random.random() * bvymax * 2 - bvymax # Random y velocity between -bvymax and bvymax
    if bvx > bvxmax:
        bvx = bvxmax
    elif bvx < -bvxmax:
        bvx = -bvxmax
    # Move Paddle of Player
    pressed_key=pygame.key.get_pressed()
    if pressed_key[K_UP] and py > 0:
        py += -rv
    if pressed_key[K_DOWN] and py < height - rh:
        py += rv
    # Computer AI
    dx = bx - cx
    # Move paddle of Computer
    if bvx < 0 and dx < ( width - 2 * mergin ) * 0.3: # move when the distace is less than 30%
        if by < cy + rh//2 and cy > 0:
            cy += -rv
        if by > cy + rh//2 and cy < height - rh:
            cy += rv
    # Update Score
    if bx  < 0:
        ps +=1
        (bx, by, bvx, bvy, cy, py) = (px - br, py + rh//2, -bvxmin, bvymin, height//2 - rh//2, height//2 - rh//2)
        pygame.time.wait(1000)
    elif bx > width:
        cs +=1
        (bx, by, bvx, bvy, cy, py) = (cx + br, cy + rh//2, bvxmin, bvymin, height//2 - rh//2, height//2 - rh//2)
        pygame.time.wait(1000)
    # Move the ball
    bx += bvx
    by += bvy
    pygame.display.update()
    pygame.time.wait(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
pygame.time.wait(3000)
pygame.quit()
sys.exit()
        
        


